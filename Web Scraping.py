import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import Scraper_db

parser= argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="Enter the number of pages to parse", type=int)
parser.add_argument("--dbname", help="Enter the number of pages to parse", type=int)
args= parser.parse_args()

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num_max = args.page_num_max
scraped_info_list = []
Scraper_db.connect(args.dbname)
for page_num in range(3,page_num_max):
    req = requests.get(oyo_url+str[page_num])
    content = req.content

    Soup = BeautifulSoup(content, "html.parser")

    all_hotels = Soup.find_all("div", {"class":"hotelCardListing"})

    for hotel in all_hotels:
        hotel_dict ={}
        hotel_dict["name"]  = hotel.find("h3", {"class":"ListingHotelDescription__hotelName"}.text
        hotel_dict["address"] = hotel.find("span", {"itemprop":"streetAddress"}).text
        hotel_dict["price"] = hotel.find("span", {"class":"ListingPrice__finalPrice"}).text
        try:
            hotel_dict["rating"] = hotel.find("span", {"class":"hotelRating__ratingSummary"}).text
        except AttributeError:
            pass

        parent_amenities_element = hotel.find("div", {"class":"amenityWrapper"})

        amenities_list ={}
        for amenity in parent_amenities_element.find_all("div", {"class":"amenityWrapper__amenity"}):
            amenities_list.append(amenity.find("span",{"class":"d-body-sm"}).text.strip()))

        hotel_dict["amenities"] = ',' .join(amenities_list[:-1])
        scraped_info_list.append(hotel_dict)
        Scraper_db.insert_into_table(args.dbname,tuple(hotel_dict.values()))

dataframe = pandas.DataFrame(scraped_info_list)
dataframe.to_csv("Oyo.csv")
Scraper_db.get_hotel_info(args.dbname)