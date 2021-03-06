import datetime
from tkinter import *
from re import match
from tkinter import messagebox
from Controllers.CompanyController import CompanyController
from Controllers.ApplicantController import ApplicantController
from Models.Company import Company
from Models.Applicant import Applicant


class Register(Frame):
    def __init__(self, logReg):
        self.email_regex = "^[a-zA-Z0-9._]+@[a-z]+\.(com|co\.in|org|in)$"
        self.website_regex = "^www\.+[a-z]+\.(com|co\.in|org|in)$"
        self.tel_no_regex = "^[0-9]{10}$"
        self.applicant = ApplicantController()
        self.company = CompanyController()
        logReg.destroy()
        self.registerTk = Tk()
        self.registerTk.title("tinder For Jobs")
        w, h = self.registerTk.winfo_screenwidth(), self.registerTk.winfo_screenheight()
        self.registerTk.geometry("%dx%d+0+0" % (w, h))
        super().__init__()
        self.widthW = w
        self.heightH = h
        self.configure(background='blue')
        self.pack(fill='both', expand=True)
        self.createWidgets()
        self.registerTk.mainloop()

    def company_register(self):
        try:
            email = self.TextEntryEmailIDCompany.get()
            password = self.TextEntryPasswordCompany.get()
            name = self.TextEntryCompanyName.get()
            location = self.TextEntryCompanyLocation.get()
            website = self.TextEntryCompanyWebsite.get()
            description = self.TextEntryCompanyDescription.get()
            email_match = match(self.email_regex, email)
            web_match = match(self.website_regex, website)
            company_details = {
                'email_id': email,
                'password': password,
                'name': name,
                'location': location,
                'website': website,
                'description': description
            }
            if email == '' or password == '' or name == '' or location == '' or website == '' or description == '':
                raise Exception('Incomplete Fields')
            elif email_match is None and email != '':
                raise Exception('Invalid Email')
            elif web_match is None and website != '':
                raise Exception('Invalid Company Website')
            else:
                company_details['email_id'] = email_match.group(0)
                company_details['website'] = web_match.group(0)
                account = self.company.register(company_details)
                if type(account) is Company:
                    print('Success')
                    print(account)
                elif type(account) is str:
                    raise Exception(str(account))
                else:
                    raise Exception("Some Weird Error happened")
        except Exception as error:
            messagebox.showinfo("Error During Registration", str(error))

    def applicant_register(self):
        try:
            email = self.TextEntryEmailIDApplicant.get()
            password = self.TextEntryPasswordApplicant.get()
            name = self.TextEntryApplicantName.get()
            dob = f'{self.variableMonth.get()} {self.variableDay.get()}, {self.variableYear.get()}'
            dob_final = datetime.datetime.strptime(dob, '%B %d, %Y').date()
            gender = self.variableGender.get()
            age = datetime.date.today().year - dob_final.year - (
                    (datetime.date.today().month, datetime.date.today().day) > (dob_final.month, dob_final.day))
            tel_no = self.TextEntryTelNo.get()
            experience = self.variableExp.get()
            email_match = match(self.email_regex, email)
            tel_no_match = match(self.tel_no_regex, tel_no)
            applicant_details = {
                'email_id': email,
                'name': name,
                'dob': dob_final,
                'gender': gender,
                'age': age,
                'tel_no': tel_no,
                'experience': experience,
                'password': password
            }
            if email == '' or password == '' or name == '' or gender == 'Select' or tel_no == '':
                raise Exception('Incomplete Fields')
            elif email_match is None and email != '':
                raise Exception('Invalid Email')
            elif tel_no_match is None and tel_no != '':
                raise Exception('Invalid Number')
            else:
                applicant_details['email_id'] = email_match.group(0)
                applicant_details['tel_no'] = tel_no_match.group(0)
                account = self.applicant.register(applicant_details)
                if type(account) is Applicant:
                    print('Success')
                    print(account)
                elif type(account) is str:
                    raise Exception(str(account))
                else:
                    raise Exception("Some Weird Error happened")
        except Exception as error:
            messagebox.showinfo("Error During Registration", str(error))

    def createWidgets(self):
        """CREATING FRAMES"""
        textFrame = Frame(self, bg='black', width=self.widthW, height=self.heightH / 4)
        textFrame.grid(row=0, column=0, columnspan=2)

        loginFrame = Frame(self, bg='black', width=self.widthW / 2 + 1, height=self.heightH * 0.75)
        loginFrame.grid(row=1, column=0)

        registerFrame = Frame(self, bg='black', width=self.widthW / 2, height=self.heightH * 0.75)
        registerFrame.grid(row=1, column=1)

        # self.grid_columnconfigure(0, uniform='g1')
        # self.grid_columnconfigure(1, uniform='g1')
        """FRAME ONE FOR LOGO"""
        welcomeLabel1 = Label(textFrame, text="tinder", bg='black', fg='white', font=('Chalet New York', 50))
        welcomeLabel2 = Label(textFrame, text="for Jobs", bg='black', fg='white', font=('Chalet New York', 20))
        welcomeLabel1.place(x=20, y=30)
        welcomeLabel2.place(x=192, y=65)

        """FRAME TWO: Registration As Applicant"""

        applicantLabel = Label(loginFrame, text='Applicants Fill Here: ', bg='black', fg='white',
                               font=('Chalet New York', 30))
        applicantLabel.place(x=175, y=0)

        TextEmailIDApplicant = Label(loginFrame, text='Email ID: ', bg='black', fg='white',
                                     font=('Chalet New York',))
        TextEmailIDApplicant.place(x=195, y=85)

        self.TextEntryEmailIDApplicant = Entry(loginFrame, bg='#434343', fg='white', width=25,
                                               font=('Chalet New York',))
        self.TextEntryEmailIDApplicant.place(x=280, y=83, height=30)

        TextPasswordAppplicant = Label(loginFrame, text='Password: ', bg='black', fg='white',
                                       font=('Chalet New York',))
        TextPasswordAppplicant.place(x=195, y=140)

        self.TextEntryPasswordApplicant = Entry(loginFrame, show='*', bg='#434343', fg='white', width=25,
                                                font=('Chalet New York',))
        self.TextEntryPasswordApplicant.place(x=280, y=139, height=30)

        TextLabelApplicantName = Label(loginFrame, text='Applicant\nName: ', bg='black', fg='white',
                                       font=('Chalet New York',))
        TextLabelApplicantName.place(x=195, y=184)

        self.TextEntryApplicantName = Entry(loginFrame, bg='#434343', fg='white', width=25, font=('Chalet New York',))
        self.TextEntryApplicantName.place(x=280, y=193, height=30)

        MonthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                     'November', 'December']
        DayList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31]
        YearList = [1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980,
                    1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996,
                    1997, 1998, 1999, 2000]

        TextLabelDOB = Label(loginFrame, text='DOB: ', bg='black', fg='white',
                             font=('Chalet New York',))
        TextLabelDOB.place(x=195, y=253)

        self.variableDay = IntVar()
        self.variableDay.set('Day')  # default value

        self.variableMonth = StringVar()
        self.variableMonth.set('Month')  # default value

        self.variableYear = IntVar()
        self.variableYear.set('Year')  # default value

        DayOption = OptionMenu(loginFrame, self.variableDay, *DayList)
        DayOption.config(bg='#434343', fg='white', height=1, font=('Chalet New York',))
        DayOption.place(x=260, y=250)

        MonthOption = OptionMenu(loginFrame, self.variableMonth, *MonthList)
        MonthOption.config(bg='#434343', fg='white', height=1, font=('Chalet New York',))
        MonthOption.place(x=336, y=250)

        YearOption = OptionMenu(loginFrame, self.variableYear, *YearList)
        YearOption.config(bg='#434343', fg='white', height=1, font=('Chalet New York',))
        YearOption.place(x=463, y=250)

        TextLabelGender = Label(loginFrame, text='Gender: ', bg='black', fg='white',
                                font=('Chalet New York',))
        TextLabelGender.place(x=195, y=311)

        GenderList = ['Male', 'Female', 'Others']

        self.variableGender = StringVar()
        self.variableGender.set('Select')

        self.GenderOption = OptionMenu(loginFrame, self.variableGender, *GenderList)
        self.GenderOption.config(bg='#434343', fg='white', height=1, font=('Chalet New York',))
        self.GenderOption.place(x=275, y=308)

        TextLabelTelNo = Label(loginFrame, text='Tel No. : ', bg='black', fg='white',
                               font=('Chalet New York',))
        TextLabelTelNo.place(x=195, y=365)

        self.TextEntryTelNo = Entry(loginFrame, bg='#434343', fg='white', width=25, font=('Chalet New York',))
        self.TextEntryTelNo.place(x=275, y=363, height=30)

        TextExperience = Label(loginFrame, text='Experience: ', bg='black', fg='white',
                               font=('Chalet New York',))
        TextExperience.place(x=195, y=415)

        ExperienceList = ['None', '1 yr', '2 yrs', '3 yrs', '4 yrs', '4+ yrs', '10+ yrs']

        self.variableExp = StringVar()
        self.variableExp.set(ExperienceList[0])

        self.ExperienceOption = OptionMenu(loginFrame, self.variableExp, *ExperienceList)
        self.ExperienceOption.config(bg='#434343', fg='white', height=1, font=('Chalet New York',))
        self.ExperienceOption.place(x=290, y=412)

        applicantRegisterButton = Button(loginFrame, text='Register As\nApplicant', width=15, height=2, bg='#434343',
                                         fg='white', command=self.applicant_register,
                                         activebackground='#666666', font=('Chalet New York',))
        applicantRegisterButton.place(x=266, y=476)

        # TextLabelPrompt = Label(loginFrame, text='Restart Your Search By Logging In.', bg='black',
        #                         fg='white',
        #                         font=('Chalet New York', 10))
        # TextLabelPrompt.place(x=235, y=550)

        """FRAME THREE: Registration As Company"""
        TextLabelCompanyRegister = Label(registerFrame, text='Company Fill Here:', bg='black', fg='white',
                                         font=('Chalet New York', 30))
        TextLabelCompanyRegister.place(x=170, y=0)

        TextEmailIDCompany = Label(registerFrame, text='Email ID: ', bg='black', fg='white',
                                   font=('Chalet New York',))
        TextEmailIDCompany.place(x=185, y=85)

        self.TextEntryEmailIDCompany = Entry(registerFrame, bg='#434343', fg='white', width=25,
                                             font=('Chalet New York',))
        self.TextEntryEmailIDCompany.place(x=270, y=83, height=30)

        TextPasswordCompany = Label(registerFrame, text='Password: ', bg='black', fg='white',
                                    font=('Chalet New York',))
        TextPasswordCompany.place(x=185, y=140)

        self.TextEntryPasswordCompany = Entry(registerFrame, show='*', bg='#434343', fg='white', width=25,
                                              font=('Chalet New York',))
        self.TextEntryPasswordCompany.place(x=270, y=139, height=30)

        TextLabelCompanyName = Label(registerFrame, text='Company\nName: ', bg='black', fg='white',
                                     font=('Chalet New York',))
        TextLabelCompanyName.place(x=185, y=184)

        self.TextEntryCompanyName = Entry(registerFrame, bg='#434343', fg='white', width=25, font=('Chalet New York',))
        self.TextEntryCompanyName.place(x=270, y=193, height=30)

        TextCompanyWebsite = Label(registerFrame, text='Website: ', bg='black', fg='white',
                                   font=('Chalet New York',))
        TextCompanyWebsite.place(x=185, y=253)

        self.TextEntryCompanyWebsite = Entry(registerFrame, bg='#434343', fg='white', width=25,
                                             font=('Chalet New York',))
        self.TextEntryCompanyWebsite.place(x=270, y=251, height=30)

        TextCompanyLocation = Label(registerFrame, text='Location: ', bg='black', fg='white',
                                    font=('Chalet New York',))
        TextCompanyLocation.place(x=185, y=311)

        self.TextEntryCompanyLocation = Entry(registerFrame, bg='#434343', fg='white', width=25,
                                              font=('Chalet New York',))
        self.TextEntryCompanyLocation.place(x=270, y=309, height=30)

        TextCompanyDescription = Label(registerFrame, text='Description: ', bg='black', fg='white',
                                       font=('Chalet New York',))
        TextCompanyDescription.place(x=180, y=365)

        self.TextEntryCompanyDescription = Entry(registerFrame, bg='#434343', fg='white', width=25,
                                                 font=('Chalet New York',))
        self.TextEntryCompanyDescription.place(x=270, y=363, height=30)

        # TextLabelFirstSteps = Label(registerFrame, text='Take Your First Step!', bg='black',
        #                                  fg='white',
        #                                  font=('Chalet New York', 20))
        # TextLabelFirstSteps.place(x=206, y=400)

        CompanyRegisterButton = Button(registerFrame, text='Register As\nCompany', width=15, height=2, bg='#434343',
                                       fg='white', command=self.company_register,
                                       activebackground='#666666', font=('Chalet New York',))
        CompanyRegisterButton.place(x=266, y=476)

        # TextLabelPrompt = Label(registerFrame, text='Register Your Details.', bg='black',
        #                              fg='white',
        #                              font=('Chalet New York', 10))
        # TextLabelPrompt.place(x=277, y=500)


def register(logReg):
    log = Register(logReg)
