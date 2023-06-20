from django.db import models

# Create your models here.
class Memberuserdata(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255)  # Field name made lowercase.
    last_login = models.DateTimeField(db_column='Last_Login', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255, blank=True, null=True, unique=True)  # Field name made lowercase.
    is_superuser = models.BooleanField(db_column='Is_Superuser', blank=True, null=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_staff = models.BooleanField(db_column='Is_Staff', blank=True, null=True)  # Field name made lowercase.
    is_active = models.BooleanField(db_column='Is_Active', blank=True, null=True)  # Field name made lowercase.
    is_authenticated = models.BooleanField(db_column='Is_Authenticated', blank=True, null=True)  # Field name made lowercase.
    date_joined = models.DateTimeField(db_column='Date_Joined', blank=True, null=True)  # Field name made lowercase.
    is_anonymous = models.BooleanField(db_column='Is_Anonymous', blank=True, null=True)  # Field name made lowercase.
    uid = models.CharField(db_column='UID', max_length=50, blank=True, null=True)  # Field name made lowercase.

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        managed = False
        db_table = 'MemberUserData'

class Membersfull(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    uid = models.CharField(db_column='UID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    first_name = models.TextField(db_column='FIRST_NAME', blank=True, null=True)  # Field name made lowercase.
    middle_name = models.TextField(db_column='MIDDLE_NAME', blank=True, null=True)  # Field name made lowercase.
    last_name = models.TextField(db_column='LAST_NAME', blank=True, null=True)  # Field name made lowercase.
    preferred_name = models.TextField(db_column='PREFERRED_NAME', blank=True, null=True)  # Field name made lowercase.
    membergroup = models.CharField(db_column='MemberGroup', max_length=50, blank=True, null=True)  # Field name made lowercase.
    internal_position = models.IntegerField(db_column='Internal_Position', blank=True, null=True)  # Field name made lowercase.
    inner_dept = models.CharField(db_column='Inner_Dept', max_length=50, blank=True, null=True)  # Field name made lowercase.
    group_imwy = models.CharField(db_column='Group_IMWY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=50, blank=True, null=True)  # Field name made lowercase.
    scjid = models.TextField(db_column='SCJID', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    ct = models.TextField(db_column='CT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'membersfull'

class Memberdata(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    membergroup = models.CharField(db_column='MemberGroup', max_length=50, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=50, blank=True, null=True)  # Field name made lowercase.
    group_imwy = models.CharField(db_column='Group_IMWY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    condition = models.TextField(db_column='Condition', blank=True, null=True)  # Field name made lowercase.
    internal_position = models.TextField(db_column='Internal_Position', blank=True, null=True)  # Field name made lowercase.
    internal_title = models.TextField(db_column='Internal_Title', blank=True, null=True)  # Field name made lowercase.
    department = models.TextField(db_column='Department', blank=True, null=True)  # Field name made lowercase.
    department_category = models.TextField(db_column='Department_Category', blank=True, null=True)  # Field name made lowercase.
    department_title = models.TextField(db_column='Department_Title', blank=True, null=True)  # Field name made lowercase.
    tgw = models.BooleanField(db_column='TGW', blank=True, null=True)  # Field name made lowercase.
    male = models.BooleanField(db_column='Male', blank=True, null=True)  # Field name made lowercase.
    registered = models.BooleanField(db_column='Registered', blank=True, null=True)  # Field name made lowercase.
    bbt = models.BooleanField(db_column='BBT', blank=True, null=True)  # Field name made lowercase.
    btm = models.TextField(db_column='BTM', blank=True, null=True)  # Field name made lowercase.
    first_name = models.TextField(db_column='FIRST_NAME', blank=True, null=True)  # Field name made lowercase.
    middle_name = models.TextField(db_column='MIDDLE_NAME', blank=True, null=True)  # Field name made lowercase.
    last_name = models.TextField(db_column='LAST_NAME', blank=True, null=True)  # Field name made lowercase.
    preferred_name = models.TextField(db_column='PREFERRED_NAME', blank=True, null=True)  # Field name made lowercase.
    preferred_name_2 = models.TextField(db_column='PREFERRED_NAME_2', blank=True, null=True)  # Field name made lowercase.
    k_name = models.TextField(db_column='K_NAME', blank=True, null=True)  # Field name made lowercase.
    ct = models.TextField(db_column='CT', blank=True, null=True)  # Field name made lowercase.
    inner_dept = models.CharField(db_column='Inner_Dept', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.TextField(db_column='UserName', blank=True, null=True)  # Field name made lowercase.
    password = models.TextField(db_column='PassWord', blank=True, null=True)  # Field name made lowercase.
    visa = models.TextField(db_column='Visa', blank=True, null=True)  # Field name made lowercase.
    dob = models.TextField(db_column='DoB', blank=True, null=True)  # Field name made lowercase.
    scjid = models.TextField(db_column='SCJID', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    memberaddress = models.TextField(db_column='MemberAddress', blank=True, null=True)  # Field name made lowercase.
    housemates = models.TextField(db_column='Housemates', blank=True, null=True)  # Field name made lowercase.
    workhours = models.TextField(db_column='WorkHours', blank=True, null=True)  # Field name made lowercase.
    studyhours = models.TextField(db_column='StudyHours', blank=True, null=True)  # Field name made lowercase.
    expgrad = models.TextField(db_column='ExpGrad', blank=True, null=True)  # Field name made lowercase.
    languages = models.TextField(db_column='Languages', blank=True, null=True)  # Field name made lowercase.
    hobbies = models.TextField(db_column='Hobbies', blank=True, null=True)  # Field name made lowercase.
    formfilled = models.TextField(db_column='FormFilled', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    socialuser = models.TextField(db_column='SocialUser', blank=True, null=True)  # Field name made lowercase.
    unitno = models.TextField(db_column='UnitNo', blank=True, null=True)  # Field name made lowercase.
    streetno = models.TextField(db_column='StreetNo', blank=True, null=True)  # Field name made lowercase.
    streetname = models.TextField(db_column='StreetName', blank=True, null=True)  # Field name made lowercase.
    surburb = models.TextField(db_column='Surburb', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    postcode = models.TextField(db_column='PostCode', blank=True, null=True)  # Field name made lowercase.
    last_login = models.TextField(db_column='Last_Login', blank=True, null=True)  # Field name made lowercase.
    is_authenticated = models.BooleanField(db_column='Is_Authenticated', blank=True, null=True)  # Field name made lowercase.
    uid = models.CharField(db_column='UID', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MemberData'