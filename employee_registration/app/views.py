from django.core.mail import send_mail
from employee_registration import settings as se
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
from .models import Manager_Login,Employee_Personal_Information,Employee_X_Education,Employee_Intermediate_Education,Employee_UG_Education,Employee_PG_Education,Employee_Experience

data = Employee_Personal_Information.objects.all()

def showindex(request):
    return render(request,"home.html")

class ShowAdmin(TemplateView):
    template_name1="Manager_Login.html"

class Main(TemplateView):
    template_name = "home.html"

class employee_Registration(TemplateView):
    template_name = "employee_myprofile_head.html"

class employee_Login(TemplateView):
    template_name = "Employee_Login.html"

class Manager_Login_page(TemplateView):
    template_name = "Manager_Login.html"

def store_user(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    name = first_name + " " +last_name
    birth_day = request.POST.get("birthday")
    email = request.POST.get("email")
    password = request.POST.get("password")
    phone_number = request.POST.get("phone")
    gender = request.POST.get("Gender")
    address = request.POST.get("Address")
    city = request.POST.get("City")
    pin_code = request.POST.get("Pin_Code")
    state = request.POST.get("State")
    country = request.POST.get("Country")
    image = request.FILES["image"]

    Employee_Personal_Information(FIRST_NAME=first_name,LAST_NAME=last_name,password=password,Date_of_Birth=birth_day,EMAIL_ID=email,MOBILE_NUMBER=phone_number,GENDER=gender,ADDRESS=address,CITY=city,PIN_CODE=pin_code,STATE=state,COUNTRY=country,image=image).save()

    return render(request,"employee_myprofile_head.html")
# def employee_login(request):
#     email = request.POST.get("Email")
#     password = request.POST.get("Password")
#
#     if Employee_Personal_Information.objects.filter(email=email) and Employee_Registration.objects.filter(password=password):
#
#         data = Employee_Registration.objects.filter(email=email)
#         return render(request, 'Employee_data.html', {"data":data})
#     else:
#         mess = "Invalid User name and Password"
#         return render(request, 'Employee_Login.html', {"message": mess})
#
def manager_validation(request):
    email = request.POST.get("Email")
    password = request.POST.get("Password")


    if Manager_Login.objects.filter(email=email) and Manager_Login.objects.filter(password=password):

        return render(request, 'Manager.html', {"data":data})
    else:
        mess = "Invalid User name and Password"
        return render(request, 'Manager_Login.html', {"message": mess})


def employee_data_selection(request):
    return None

# def qualificatiom(request):
#     name = request.POST.get("name")
#     data = Employee_Registration.objects.all()
#     data = Employee_Registration.objects.filter(name__exact=name).all()
#
#     return render(request,"emp_qualification.html",{"data":data})


class Employee_edu(TemplateView):
    template_name = "employee_edu.html"



class Work_experience(TemplateView):
    template_name = "employee_work_experience.html"


class Personal_information(TemplateView):
    template_name = "dummy.html"


def employee_edu(request):

    return render(request,"employee_edu.html")


def email_otp_id(request):
    email = request.POST.get("email")
    send_mail("check","this is a check mail",
              se.EMAIL_HOST_USER,[email])
    return render(request, "employee_myprofile_head.html")


def emp_education(request):
    xstart = request.POST.get("xstatrt")
    xend =request.POST.get("xend")
    xcountry =request.POST.get("xcountry")
    xstate = request.POST.get("xstate")
    xcity = request.POST.get("xcity")
    xinstitue = request.POST.get("xinstitue")
    xuniversity = request.POST.get("xuniversity")
    xcousrse_type = request.POST.get("xcousrse_type")
    interstatrt = request.POST.get("interstatrt")
    interend = request.POST.get("interend")
    intercountry = request.POST.get("intercountry")
    interstate = request.POST.get("interstate")
    intercity = request.POST.get("intercity")
    interinstitue = request.POST.get("interinstitue")
    interuniversity = request.POST.get("interuniversity")
    intercousrse_type = request.POST.get("intercousrse_type")
    ugstart = request.POST.get("ugstatrt")
    ugend = request.POST.get("ugend")
    ugcountry = request.POST.get("ugcountry")
    ugstate = request.POST.get("ugstate")
    ugcity = request.POST.get("ugcity")
    uginstitue = request.POST.get("uginstitue")
    uguniversity = request.POST.get("uguniversity")
    ugcousrse_type = request.POST.get("ugcousrse_type")
    pgstart = request.POST.get("pgstatrt")
    pgend = request.POST.get("pgend")
    pgcountry = request.POST.get("pgcountry")
    pgstate = request.POST.get("pgstate")
    pgcity = request.POST.get("pgcity")
    pginstitue = request.POST.get("pginstitue")
    pguniversity = request.POST.get("pguniversity")
    pgcousrse_type = request.POST.get("pgcousrse_type")
    id = request.POST.get("id")

    Employee_X_Education(ID_NO=id,Start_Date=xstart,Completion_Date=xend,Country=xcountry,State=xstate,City=xcity,Education_Institution=xinstitue,Board_or_University=xuniversity,Cousre_Type=xcousrse_type).save()
    Employee_Intermediate_Education(ID_NO=id, Start_Date=interstatrt, Completion_Date=interend, Country=intercountry, State=interstate, City=intercity,Education_Institution=interinstitue, Board_or_University=interuniversity,Cousre_Type=intercousrse_type).save()
    Employee_UG_Education(ID_NO=id, Start_Date=ugstart, Completion_Date=ugend, Country=ugcountry, State=ugstate, City=ugcity,Education_Institution=uginstitue, Board_or_University=uguniversity,Cousre_Type=ugcousrse_type).save()
    Employee_PG_Education(ID_NO=id, Start_Date=pgstart, Completion_Date=pgend, Country=pgcountry, State=pgstate, City=pgcity,Education_Institution=pginstitue, Board_or_University=pguniversity,Cousre_Type=pgcousrse_type).save()

    return render(request, "employee_myprofile_head.html")


def button_validation(request):
    id = request.POST.get("id")
    email = request.POST.get("email")
    button = request.POST.get("button")

    if button == "idno":
        if Employee_Personal_Information.objects.filter(ID_NO=id):
            return render(request,"employee_edu.html",{"data":id})
        else:
            msg="wrong id no"

            return render(request,"employee_edu.html",{"message":msg})
    if button == "work_experience":
        if Employee_Personal_Information.objects.filter(ID_NO=id):
            return render(request,"employee_work_experience.html",{"data":id})
        else:
            msg="wrong id no"
            return render(request,"",{"message":msg})
    if button == "idno_email":
        if Employee_Personal_Information.objects.filter(EMAIL_ID=email):
            data=Employee_Personal_Information.objects.get(EMAIL_ID=email)
            emp_i = data.ID_NO
            emp_id = str(emp_i)
            send_mail("Lucky Software Solutions : - ID_NO = ",emp_id,
                      se.EMAIL_HOST_USER, [email])
            return render(request, "employee_myprofile_head.html")
        else:
            msg="wrong Email_ID , plz check it"
            return render(request,"idno.html",{"message":msg})

    if button == "edu_details":
        xstart = request.POST.get("xstatrt")
        xend = request.POST.get("xend")
        xcountry = request.POST.get("xcountry")
        xstate = request.POST.get("xstate")
        xcity = request.POST.get("xcity")
        xinstitue = request.POST.get("xinstitue")
        xuniversity = request.POST.get("xuniversity")
        xcousrse_type = request.POST.get("xcousrse_type")
        interstatrt = request.POST.get("interstatrt")
        interend = request.POST.get("interend")
        intercountry = request.POST.get("intercountry")
        interstate = request.POST.get("interstate")
        intercity = request.POST.get("intercity")
        interinstitue = request.POST.get("interinstitue")
        interuniversity = request.POST.get("interuniversity")
        intercousrse_type = request.POST.get("intercousrse_type")
        ugstart = request.POST.get("ugstatrt")
        ugend = request.POST.get("ugend")
        ugcountry = request.POST.get("ugcountry")
        ugstate = request.POST.get("ugstate")
        ugcity = request.POST.get("ugcity")
        uginstitue = request.POST.get("uginstitue")
        uguniversity = request.POST.get("uguniversity")
        ugcousrse_type = request.POST.get("ugcousrse_type")
        pgstart = request.POST.get("pgstatrt")
        pgend = request.POST.get("pgend")
        pgcountry = request.POST.get("pgcountry")
        pgstate = request.POST.get("pgstate")
        pgcity = request.POST.get("pgcity")
        pginstitue = request.POST.get("pginstitue")
        pguniversity = request.POST.get("pguniversity")
        pgcousrse_type = request.POST.get("pgcousrse_type")
        id = request.POST.get("id")

        Employee_X_Education(ID_NO=id, Start_Date=xstart, Completion_Date=xend, Country=xcountry, State=xstate,
                             City=xcity, Education_Institution=xinstitue, Board_or_University=xuniversity,
                             Cousre_Type=xcousrse_type).save()
        Employee_Intermediate_Education(ID_NO=id, Start_Date=interstatrt, Completion_Date=interend,
                                        Country=intercountry, State=interstate, City=intercity,
                                        Education_Institution=interinstitue, Board_or_University=interuniversity,
                                        Cousre_Type=intercousrse_type).save()
        Employee_UG_Education(ID_NO=id, Start_Date=ugstart, Completion_Date=ugend, Country=ugcountry, State=ugstate,
                              City=ugcity, Education_Institution=uginstitue, Board_or_University=uguniversity,
                              Cousre_Type=ugcousrse_type).save()
        Employee_PG_Education(ID_NO=id, Start_Date=pgstart, Completion_Date=pgend, Country=pgcountry, State=pgstate,
                              City=pgcity, Education_Institution=pginstitue, Board_or_University=pguniversity,
                              Cousre_Type=pgcousrse_type).save()

        return render(request, "employee_myprofile_head.html")

    if button == "Emp_Exp":
        id = request.POST.get("id")
        years = request.POST.get("years")
        month = request.POST.get("month")
        previous_worked_here = request.POST.get("previous_worked_here")

        Employee_Experience(ID_NO=id,YEAR=years,MONTH=month,OLD_EMPLOYEE=previous_worked_here).save()
        return render(request, "employee_myprofile_head.html")



def idno(request):
    return render(request,"idno.html")

def search(request):
    people = Employee_Personal_Information.objects.all()
    return render(request, 'template.html',{"data":people})


def personalinformation(request):
    return render(request,"dummy.html")


def seemore(request):

    id = request.GET.get("id")

    if Employee_X_Education.objects.filter(ID_NO=id):
        edu_xth_details_employee = Employee_X_Education.objects.filter(ID_NO=id)
        edu_inter_details_employee = Employee_Intermediate_Education.objects.filter(ID_NO=id)
        edu_ug_details_employee = Employee_UG_Education.objects.filter(ID_NO=id)
        edu_pg_details_employee = Employee_PG_Education.objects.filter(ID_NO=id)

        education = {
            "data":data,
             "edu_xth_details_employee":edu_xth_details_employee,
            "edu_inter_details_employee":edu_inter_details_employee,
            "edu_ug_details_employee":edu_ug_details_employee,
            "edu_pg_details_employee":edu_pg_details_employee
        }

        return render(request,"Manager.html",{"edu":education})
