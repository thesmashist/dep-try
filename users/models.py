# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Announcementdata(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    timestamp = models.TextField(db_column='Timestamp', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    image_link = models.TextField(db_column='Image_Link', blank=True, null=True)  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    target = models.TextField(db_column='Target', blank=True, null=True)  # Field name made lowercase.
    priority = models.TextField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AnnouncementData'


class Attendancedata(models.Model):
    attendanceid = models.AutoField(db_column='AttendanceID', primary_key=True)  # Field name made lowercase.
    memberid = models.IntegerField(db_column='MemberID')  # Field name made lowercase.
    expected = models.TextField(db_column='Expected', blank=True, null=True)  # Field name made lowercase.
    expectedreason = models.TextField(db_column='ExpectedReason', blank=True, null=True)  # Field name made lowercase.
    attended = models.TextField(db_column='Attended', blank=True, null=True)  # Field name made lowercase.
    attendedreason = models.TextField(db_column='AttendedReason', blank=True, null=True)  # Field name made lowercase.
    tardy = models.BooleanField(db_column='Tardy', blank=True, null=True)  # Field name made lowercase.
    tardyreason = models.TextField(db_column='TardyReason', blank=True, null=True)  # Field name made lowercase.
    notes = models.BooleanField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    serviceid = models.IntegerField(db_column='ServiceID', blank=True, null=True)  # Field name made lowercase.
    attendedtime = models.DateTimeField(db_column='AttendedTime', blank=True, null=True)  # Field name made lowercase.
    expectedtime = models.DateTimeField(db_column='ExpectedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AttendanceData'




class Dailystats(models.Model):
    statid = models.AutoField(db_column='StatID', primary_key=True)  # Field name made lowercase.
    membergroup = models.CharField(db_column='MemberGroup', max_length=255)  # Field name made lowercase.
    f = models.FloatField(db_column='F', blank=True, null=True)  # Field name made lowercase.
    m = models.FloatField(db_column='M', blank=True, null=True)  # Field name made lowercase.
    pp = models.FloatField(db_column='PP', blank=True, null=True)  # Field name made lowercase.
    p = models.FloatField(db_column='P', blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=255, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inner_department = models.CharField(db_column='Inner_Department', max_length=255, blank=True, null=True)  # Field name made lowercase.
    day = models.DateTimeField(db_column='Day', blank=True, null=True)  # Field name made lowercase.
    gyjn = models.TextField(db_column='GYJN', blank=True, null=True)  # Field name made lowercase.
    weekno = models.IntegerField(db_column='WeekNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DailyStats'


class Deptdata(models.Model):
    did = models.AutoField(db_column='DID', primary_key=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=255)  # Field name made lowercase.
    regionpos = models.IntegerField(db_column='RegionPos', blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DeptData'

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

class Evactivity(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    activityname = models.CharField(db_column='ActivityName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    activityweek = models.IntegerField(db_column='ActivityWeek', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    weekgoal = models.FloatField(db_column='WeekGoal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVActivity'


class Evgames(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    membergroup = models.CharField(db_column='MemberGroup', max_length=255)  # Field name made lowercase.
    gyjn = models.CharField(db_column='GYJN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    picking = models.FloatField(db_column='Picking', blank=True, null=True)  # Field name made lowercase.
    pre_picking = models.FloatField(db_column='Pre-Picking', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    resultweek = models.IntegerField(db_column='ResultWeek', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVGames'

class Fallendata(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fruitkey = models.IntegerField(db_column='FruitKey', blank=True, null=True)  # Field name made lowercase.
    bbtid = models.IntegerField(db_column='BBTID', blank=True, null=True)  # Field name made lowercase.
    allreasons = models.TextField(db_column='AllReasons', blank=True, null=True)  # Field name made lowercase.
    sfaenvmain = models.TextField(db_column='sFaEnvMain', blank=True, null=True)  # Field name made lowercase.
    mainreasondetails = models.TextField(db_column='MainReasonDetails', blank=True, null=True)  # Field name made lowercase.
    schedulereasons = models.TextField(db_column='ScheduleReasons', blank=True, null=True)  # Field name made lowercase.
    schedulemain = models.TextField(db_column='ScheduleMain', blank=True, null=True)  # Field name made lowercase.
    environmentreasons = models.TextField(db_column='EnvironmentReasons', blank=True, null=True)  # Field name made lowercase.
    environmentmain = models.TextField(db_column='EnvironmentMain', blank=True, null=True)  # Field name made lowercase.
    interestreasons = models.TextField(db_column='InterestReasons', blank=True, null=True)  # Field name made lowercase.
    disagreereasons = models.TextField(db_column='DisagreeReasons', blank=True, null=True)  # Field name made lowercase.
    mentalcondition = models.TextField(db_column='MentalCondition', blank=True, null=True)  # Field name made lowercase.
    migrationtype = models.TextField(db_column='MigrationType', blank=True, null=True)  # Field name made lowercase.
    migrationreason = models.TextField(db_column='MigrationReason', blank=True, null=True)  # Field name made lowercase.
    wrongintention = models.TextField(db_column='WrongIntention', blank=True, null=True)  # Field name made lowercase.
    financialreasons = models.TextField(db_column='FinancialReasons', blank=True, null=True)  # Field name made lowercase.
    visaduration = models.TextField(db_column='VisaDuration', blank=True, null=True)  # Field name made lowercase.
    understanding = models.TextField(db_column='Understanding', blank=True, null=True)  # Field name made lowercase.
    sexialityorientation = models.TextField(db_column='SexialityOrientation', blank=True, null=True)  # Field name made lowercase.
    unknowndata = models.TextField(db_column='UnknownData', blank=True, null=True)  # Field name made lowercase.
    fallenreportdate = models.TextField(db_column='FallenReportDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FallenData'


class Fbasicdata(models.Model):
    fruitkey = models.IntegerField(db_column='FruitKey', primary_key=True)  # Field name made lowercase.
    fishname = models.TextField(db_column='FishName')  # Field name made lowercase.
    fishphone = models.IntegerField(db_column='FishPhone', blank=True, null=True)  # Field name made lowercase.
    fishuser = models.TextField(db_column='FishUser', blank=True, null=True)  # Field name made lowercase.
    evplatform = models.TextField(db_column='EVPlatform', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    fruitstatus = models.TextField(db_column='FruitStatus', blank=True, null=True)  # Field name made lowercase.
    currleaf1 = models.IntegerField(db_column='CurrLeaf1', blank=True, null=True)  # Field name made lowercase.
    currleaf2 = models.IntegerField(db_column='CurrLeaf2', blank=True, null=True)  # Field name made lowercase.
    bbt = models.IntegerField(db_column='BBT', blank=True, null=True)  # Field name made lowercase.
    points1 = models.FloatField(db_column='Points1', blank=True, null=True)  # Field name made lowercase.
    points2 = models.FloatField(db_column='Points2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FBasicData'


class Fruitdata(models.Model):
    fruitkey = models.IntegerField(db_column='FruitKey', primary_key=True)  # Field name made lowercase.
    timestamp = models.TextField(db_column='Timestamp', blank=True, null=True)  # Field name made lowercase.
    f1_id = models.TextField(db_column='F1_ID', blank=True, null=True)  # Field name made lowercase.
    fishname = models.TextField(db_column='FishName', blank=True, null=True)  # Field name made lowercase.
    fishuser = models.TextField(db_column='FishUser', blank=True, null=True)  # Field name made lowercase.
    fishphone = models.TextField(db_column='FishPhone', blank=True, null=True)  # Field name made lowercase.
    church = models.TextField(db_column='Church', blank=True, null=True)  # Field name made lowercase.
    fishing_zone = models.TextField(db_column='Fishing_Zone', blank=True, null=True)  # Field name made lowercase.
    visa = models.TextField(db_column='Visa', blank=True, null=True)  # Field name made lowercase.
    ev_concept = models.TextField(db_column='EV_Concept', blank=True, null=True)  # Field name made lowercase.
    evplatform = models.TextField(db_column='EVPlatform', blank=True, null=True)  # Field name made lowercase.
    evonlineoffline = models.TextField(db_column='EVOnlineOffline', blank=True, null=True)  # Field name made lowercase.
    birthday = models.TextField(db_column='Birthday', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    l1_id = models.TextField(db_column='L1_ID', blank=True, null=True)  # Field name made lowercase.
    l2_id = models.TextField(db_column='L2_ID', blank=True, null=True)  # Field name made lowercase.
    environment = models.TextField(db_column='Environment', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    stage_f = models.TextField(db_column='Stage_F', blank=True, null=True)  # Field name made lowercase.
    stage_m = models.TextField(db_column='Stage_M', blank=True, null=True)  # Field name made lowercase.
    stage_p = models.TextField(db_column='Stage_P', blank=True, null=True)  # Field name made lowercase.
    bbt_id = models.TextField(db_column='BBT_ID', blank=True, null=True)  # Field name made lowercase.
    f2_id = models.TextField(db_column='F2_ID', blank=True, null=True)  # Field name made lowercase.
    attendee_1_id = models.TextField(db_column='Attendee_1_ID', blank=True, null=True)  # Field name made lowercase.
    attendee_2_id = models.TextField(db_column='Attendee_2_ID', blank=True, null=True)  # Field name made lowercase.
    pls = models.TextField(db_column='PLS', blank=True, null=True)  # Field name made lowercase.
    clad = models.TextField(db_column='CLAD', blank=True, null=True)  # Field name made lowercase.
    stage_pp = models.TextField(db_column='Stage_PP', blank=True, null=True)  # Field name made lowercase.
    stage = models.TextField(db_column='Stage', blank=True, null=True)  # Field name made lowercase.
    a1_points = models.FloatField(db_column='A1_Points', blank=True, null=True)  # Field name made lowercase.
    a2_points = models.FloatField(db_column='A2_Points', blank=True, null=True)  # Field name made lowercase.
    l1_points = models.FloatField(db_column='L1_Points', blank=True, null=True)  # Field name made lowercase.
    l2_points = models.FloatField(db_column='L2_Points', blank=True, null=True)  # Field name made lowercase.
    f1_points = models.FloatField(db_column='F1_Points', blank=True, null=True)  # Field name made lowercase.
    f2_points = models.FloatField(db_column='F2_Points', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.TextField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    pp1_points = models.FloatField(db_column='PP1_Points', blank=True, null=True)  # Field name made lowercase.
    pp2_points = models.FloatField(db_column='PP2_Points', blank=True, null=True)  # Field name made lowercase.
    fruitstatus = models.TextField(db_column='FruitStatus', blank=True, null=True)  # Field name made lowercase.
    pp1_id = models.TextField(db_column='PP1_ID', blank=True, null=True)  # Field name made lowercase.
    pp2_id = models.TextField(db_column='PP2_ID', blank=True, null=True)  # Field name made lowercase.
    f_time = models.DateTimeField(db_column='F_TIME', blank=True, null=True)  # Field name made lowercase.
    m_time = models.DateTimeField(db_column='M_TIME', blank=True, null=True)  # Field name made lowercase.
    p_time = models.DateTimeField(db_column='P_TIME', blank=True, null=True)  # Field name made lowercase.
    pp_time = models.DateTimeField(db_column='PP_TIME', blank=True, null=True)  # Field name made lowercase.
    holidayplan = models.TextField(db_column='HolidayPlan', blank=True, null=True)  # Field name made lowercase.
    denomination = models.TextField(db_column='Denomination', blank=True, null=True)  # Field name made lowercase.
    nationality = models.TextField(db_column='Nationality', blank=True, null=True)  # Field name made lowercase.
    residence = models.TextField(db_column='Residence', blank=True, null=True)  # Field name made lowercase.
    visanotes = models.TextField(db_column='VisaNotes', blank=True, null=True)  # Field name made lowercase.
    holidaynotes = models.TextField(db_column='HolidayNotes', blank=True, null=True)  # Field name made lowercase.
    locked = models.TextField(db_column='Locked', blank=True, null=True)  # Field name made lowercase.
    proceedable = models.TextField(db_column='Proceedable', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    unlockdate = models.TextField(db_column='UnlockDate', blank=True, null=True)  # Field name made lowercase.
    unlockable = models.TextField(db_column='Unlockable', blank=True, null=True)  # Field name made lowercase.
    mine = models.TextField(db_column='Mine', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    fishphone2 = models.BigIntegerField(db_column='FishPhone2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FruitData'


class Groupdata(models.Model):
    gid = models.AutoField(db_column='GID', primary_key=True)  # Field name made lowercase.
    membergroup = models.CharField(db_column='MemberGroup', max_length=255)  # Field name made lowercase.
    innerdeptpos = models.IntegerField(db_column='InnerDeptPos', blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GroupData'


class Innerdeptdata(models.Model):
    inid = models.AutoField(db_column='InID', primary_key=True)  # Field name made lowercase.
    innerdepartment = models.CharField(db_column='InnerDepartment', max_length=255)  # Field name made lowercase.
    deptpos = models.IntegerField(db_column='DeptPos', blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InnerDeptData'





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


class Regiondata(models.Model):
    rid = models.AutoField(db_column='RID', primary_key=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=255)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RegionData'


class Report(models.Model):
    reportid = models.AutoField(db_column='ReportId', primary_key=True)  # Field name made lowercase.
    reportdate = models.CharField(db_column='ReportDate', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    classdate = models.CharField(db_column='ClassDate', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    fruitkey = models.IntegerField(db_column='FruitKey')  # Field name made lowercase.
    createdby = models.IntegerField(db_column='CreatedBy')  # Field name made lowercase.
    topic = models.CharField(db_column='Topic', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    beforeclass = models.CharField(db_column='BeforeClass', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    duringclass = models.CharField(db_column='DuringClass', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    afterclass = models.CharField(db_column='AfterClass', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    general = models.CharField(db_column='General', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    obedience = models.CharField(db_column='Obedience', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    friendcircumstances = models.CharField(db_column='FriendCircumstances', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    nextclassdate = models.DateTimeField(db_column='NextClassDate', blank=True, null=True)  # Field name made lowercase.
    attendee_1 = models.TextField(db_column='Attendee_1', blank=True, null=True)  # Field name made lowercase.
    attendee_2 = models.TextField(db_column='Attendee_2', blank=True, null=True)  # Field name made lowercase.
    additionalinfo = models.TextField(db_column='AdditionalInfo', blank=True, null=True)  # Field name made lowercase.
    reaction = models.TextField(db_column='Reaction', blank=True, null=True)  # Field name made lowercase.
    attitude = models.TextField(db_column='Attitude', blank=True, null=True)  # Field name made lowercase.
    environment = models.TextField(db_column='Environment', blank=True, null=True)  # Field name made lowercase.
    bbt_feedback = models.TextField(db_column='BBT_Feedback', blank=True, null=True)  # Field name made lowercase.
    label = models.TextField(db_column='Label', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Report'


class Serviceabsentdata(models.Model):
    aid = models.AutoField(db_column='AID', primary_key=True)  # Field name made lowercase.
    memberid = models.IntegerField(db_column='MemberID', blank=True, null=True)  # Field name made lowercase.
    absentcounter = models.IntegerField(db_column='AbsentCounter', blank=True, null=True)  # Field name made lowercase.
    absentcumulative = models.IntegerField(db_column='AbsentCumulative', blank=True, null=True)  # Field name made lowercase.
    lastreport = models.CharField(db_column='LastReport', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServiceAbsentData'


class Servicedata(models.Model):
    sid = models.AutoField(db_column='SID', primary_key=True)  # Field name made lowercase.
    servicedate = models.DateField(db_column='ServiceDate', blank=True, null=True)  # Field name made lowercase.
    serviceday = models.CharField(db_column='ServiceDay', max_length=50, blank=True, null=True)  # Field name made lowercase.
    servicetitle = models.TextField(db_column='ServiceTitle', blank=True, null=True)  # Field name made lowercase.
    maintime = models.CharField(db_column='MainTime', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServiceData'


class Sessions(models.Model):
    sid = models.CharField(primary_key=True, max_length=255)
    session = models.TextField()
    expires = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sessions'


class Stagefdata(models.Model):
    fruitkey = models.IntegerField(db_column='FruitKey', primary_key=True)  # Field name made lowercase.
    f_time = models.DateTimeField(db_column='F_TIME')  # Field name made lowercase.
    member1 = models.IntegerField(db_column='Member1', blank=True, null=True)  # Field name made lowercase.
    member2 = models.IntegerField(db_column='Member2', blank=True, null=True)  # Field name made lowercase.
    f1_point = models.FloatField(db_column='F1_Point', blank=True, null=True)  # Field name made lowercase.
    f2_point = models.FloatField(db_column='F2_Point', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StageFData'


class Stagemdata(models.Model):
    fruitkey = models.IntegerField(db_column='FruitKey', primary_key=True)  # Field name made lowercase.
    m_time = models.DateTimeField(db_column='M_TIME')  # Field name made lowercase.
    member1 = models.IntegerField(db_column='Member1', blank=True, null=True)  # Field name made lowercase.
    member2 = models.IntegerField(db_column='Member2', blank=True, null=True)  # Field name made lowercase.
    m1_point = models.FloatField(db_column='M1_Point', blank=True, null=True)  # Field name made lowercase.
    m2_point = models.FloatField(db_column='M2_Point', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StageMData'


class Stagepdata(models.Model):
    fruitkey = models.IntegerField(db_column='FruitKey', primary_key=True)  # Field name made lowercase.
    p_time = models.DateTimeField(db_column='P_TIME')  # Field name made lowercase.
    member1 = models.IntegerField(db_column='Member1', blank=True, null=True)  # Field name made lowercase.
    member2 = models.IntegerField(db_column='Member2', blank=True, null=True)  # Field name made lowercase.
    p1_point = models.FloatField(db_column='P1_Point', blank=True, null=True)  # Field name made lowercase.
    p2_point = models.FloatField(db_column='P2_Point', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StagePData'


class Stageppdata(models.Model):
    fruitkey = models.IntegerField(db_column='FruitKey', primary_key=True)  # Field name made lowercase.
    pp_time = models.DateTimeField(db_column='PP_TIME')  # Field name made lowercase.
    member1 = models.IntegerField(db_column='Member1', blank=True, null=True)  # Field name made lowercase.
    member2 = models.IntegerField(db_column='Member2', blank=True, null=True)  # Field name made lowercase.
    pp1_point = models.FloatField(db_column='PP1_Point', blank=True, null=True)  # Field name made lowercase.
    pp2_point = models.FloatField(db_column='PP2_Point', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StagePPData'


class Todo(models.Model):
    taskid = models.AutoField(db_column='TaskID', primary_key=True)  # Field name made lowercase.
    memberid = models.IntegerField(db_column='MemberId', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    completedate = models.DateTimeField(db_column='CompleteDate', blank=True, null=True)  # Field name made lowercase.
    tasktitle = models.CharField(db_column='TaskTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    taskdescription = models.CharField(db_column='TaskDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    iscompleted = models.TextField(db_column='IsCompleted', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    participants = models.CharField(db_column='Participants', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Todo'


class Watchlistdata(models.Model):
    watchid = models.AutoField(db_column='WatchID', primary_key=True)  # Field name made lowercase.
    memberid = models.IntegerField(db_column='MemberID', blank=True, null=True)  # Field name made lowercase.
    addeddate = models.DateField(db_column='AddedDate', blank=True, null=True)  # Field name made lowercase.
    addedby = models.IntegerField(db_column='AddedBy', blank=True, null=True)  # Field name made lowercase.
    unwatched = models.BooleanField(db_column='Unwatched', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WatchListData'


class Whitelistdata(models.Model):
    wid = models.AutoField(db_column='WID', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    data = models.TextField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WhiteListData'


class Whitelistrecdata(models.Model):
    wid = models.AutoField(db_column='WID', primary_key=True)  # Field name made lowercase.
    memberid = models.CharField(db_column='MemberID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    wlid = models.IntegerField(db_column='WLID')  # Field name made lowercase.
    addeddate = models.TextField(db_column='AddedDate', blank=True, null=True)  # Field name made lowercase.
    addedby = models.IntegerField(db_column='AddedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WhiteListRecData'
