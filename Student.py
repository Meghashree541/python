import csv
def write_info_csv (info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell==0:
             writer.writerow({"Name","Age","Contact number","Email id"})
        writer.writerow(info_list)
if __name__ == '__main__':
    condition=True
    student_num=1
    while(condition):

        student_info=input("Enter some student information in the following format(Name,Age,Contact_list,Email_id)")
        print("Entered information"+student_info)

        student_info_list=student_info.split(" ")
        print("Entered split info is:"+str(student_info_list))
        print("The entered information is:\n Name={}\n Age={}\n Contact number={}\n Email ID={}\n"
              .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check=input("If the entered number is correct(yes/no)")
        if choice_check=="yes":
            write_info_csv(student_info_list)
            condition_check=input("Enter(yes/no) if you want to continue ")
            if condition_check=="yes":
                condition=True
                student_num = student_num+1
            elif condition_check == "no":
                condition=False
        elif choice_check == "no":
            print("Please reenter the info")