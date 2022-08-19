# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tblhypervguestnetwork(models.Model):
    hypervguestnetworkid = models.AutoField(db_column='HyperVGuestNetworkID', primary_key=True)  # Field name made lowercase.
    hypervguestid = models.ForeignKey('Tblhypervguest', models.DO_NOTHING, db_column='HyperVGuestID')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TblHyperVGuestNetwork'


class Tsyschassistypes(models.Model):
    chassistype = models.IntegerField(db_column='Chassistype', primary_key=True)  # Field name made lowercase.
    chassisname = models.CharField(db_column='ChassisName', max_length=255)  # Field name made lowercase.
    img = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'TsysChassisTypes'


class Tsyscloudconfiguration(models.Model):
    cloudconfigurationid = models.AutoField(db_column='CloudConfigurationId', primary_key=True)  # Field name made lowercase.
    enablepushtocloud = models.BooleanField(db_column='EnablePushToCloud', blank=True, null=True)  # Field name made lowercase.
    clientkey = models.CharField(db_column='ClientKey', max_length=500)  # Field name made lowercase.
    installkey = models.CharField(db_column='InstallKey', max_length=500)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accesstoken = models.CharField(db_column='AccessToken', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    refreshtoken = models.CharField(db_column='RefreshToken', max_length=500, blank=True, null=True)  # Field name made lowercase.
    scanningservername = models.ForeignKey('Tsysasservers', models.DO_NOTHING, db_column='ScanningServerName', blank=True, null=True)  # Field name made lowercase.
    userdomain = models.CharField(db_column='UserDomain', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ispushtocloudenabled = models.BooleanField(db_column='IsPushToCloudEnabled')  # Field name made lowercase.
    feedbackmessage = models.CharField(db_column='FeedbackMessage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    lastsynceddatetime = models.DateTimeField(db_column='LastSyncedDateTime', blank=True, null=True)  # Field name made lowercase.
    numberoflastsyncedrecords = models.IntegerField(db_column='NumberOfLastSyncedRecords', blank=True, null=True)  # Field name made lowercase.
    numberoffailedattempts = models.IntegerField(db_column='NumberOfFailedAttempts')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    clientid = models.CharField(db_column='ClientId', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    clientsecret = models.CharField(db_column='ClientSecret', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    initialpushretries = models.SmallIntegerField(db_column='InitialPushRetries')  # Field name made lowercase.
    accesstokenvaliduntil = models.DateTimeField(db_column='AccessTokenValidUntil', blank=True, null=True)  # Field name made lowercase.
    initialpushretrytime = models.DateTimeField(db_column='InitialPushRetryTime', blank=True, null=True)  # Field name made lowercase.
    cloudconfigurationdeleteaction = models.IntegerField(db_column='CloudConfigurationDeleteAction')  # Field name made lowercase.
    licensetoken = models.CharField(db_column='LicenseToken', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    refreshlicensetokenstatus = models.IntegerField(db_column='RefreshLicenseTokenStatus')  # Field name made lowercase.
    journalsyncinterval = models.IntegerField(db_column='JournalSyncInterval', blank=True, null=True)  # Field name made lowercase.
    journalsyncbatch = models.IntegerField(db_column='JournalSyncBatch', blank=True, null=True)  # Field name made lowercase.
    installationname = models.CharField(db_column='InstallationName', max_length=40)  # Field name made lowercase.
    installationdescription = models.CharField(db_column='InstallationDescription', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    pushidentifier = models.CharField(db_column='PushIdentifier', max_length=500, blank=True, null=True)  # Field name made lowercase.
    firstgetinitialpushprogress = models.DateTimeField(db_column='FirstGetInitialPushProgress', blank=True, null=True)  # Field name made lowercase.
    isinitialpushsuccessful = models.BooleanField(db_column='IsInitialPushSuccessful')  # Field name made lowercase.
    initialpushpreviousstatus = models.TextField(db_column='InitialPushPreviousStatus', blank=True, null=True)  # Field name made lowercase.
    sendchangeddatatimeoutinseconds = models.IntegerField(db_column='SendChangedDataTimeoutInSeconds', blank=True, null=True)  # Field name made lowercase.
    sendfastchangingdatatimeoutinseconds = models.IntegerField(db_column='SendFastChangingDataTimeoutInSeconds', blank=True, null=True)  # Field name made lowercase.
    sendnonchangeddatatimeoutinseconds = models.IntegerField(db_column='SendNonChangedDataTimeoutInSeconds', blank=True, null=True)  # Field name made lowercase.
    sendchangeddatatimeoutinsecondsoverride = models.IntegerField(db_column='SendChangedDataTimeoutInSecondsOverride', blank=True, null=True)  # Field name made lowercase.
    sendfastchangingdatatimeoutinsecondsoverride = models.IntegerField(db_column='SendFastChangingDataTimeoutInSecondsOverride', blank=True, null=True)  # Field name made lowercase.
    sendnonchangeddatatimeoutinsecondsoverride = models.IntegerField(db_column='SendNonChangedDataTimeoutInSecondsOverride', blank=True, null=True)  # Field name made lowercase.
    numberofchangesfornextsync = models.IntegerField(db_column='NumberOfChangesForNextSync')  # Field name made lowercase.
    isdualmodeenabled = models.BooleanField(db_column='IsDualModeEnabled')  # Field name made lowercase.
    retryinitialpushnow = models.BooleanField(db_column='RetryInitialPushNow')  # Field name made lowercase.
    statuslastchanged = models.DateTimeField(db_column='StatusLastChanged', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TsysCloudConfiguration'


class Tsysconfig(models.Model):
    config = models.CharField(db_column='Config', primary_key=True, max_length=50)  # Field name made lowercase.
    licensekey = models.CharField(max_length=2000, blank=True, null=True)
    datefrom = models.CharField(max_length=8, blank=True, null=True)
    dateto = models.CharField(max_length=8, blank=True, null=True)
    wolcommand = models.CharField(db_column='Wolcommand', max_length=500, blank=True, null=True)  # Field name made lowercase.
    wolremovepoint = models.BooleanField(db_column='Wolremovepoint', blank=True, null=True)  # Field name made lowercase.
    actionpath = models.CharField(db_column='Actionpath', max_length=400, blank=True, null=True)  # Field name made lowercase.
    trialdateto = models.CharField(db_column='Trialdateto', max_length=8, blank=True, null=True)  # Field name made lowercase.
    schemaversion = models.IntegerField(db_column='Schemaversion', blank=True, null=True)  # Field name made lowercase.
    trialmode = models.BooleanField(db_column='Trialmode', blank=True, null=True)  # Field name made lowercase.
    firstrun = models.BooleanField(db_column='Firstrun')  # Field name made lowercase.
    reportrefresh = models.IntegerField(db_column='Reportrefresh')  # Field name made lowercase.
    assetdashboard = models.BooleanField(db_column='AssetDashboard')  # Field name made lowercase.
    updatecheck = models.BooleanField(db_column='UpdateCheck')  # Field name made lowercase.
    lastupdatecheck = models.DateTimeField(db_column='LastUpdateCheck')  # Field name made lowercase.
    qrcodehostname = models.CharField(db_column='Qrcodehostname', max_length=300, blank=True, null=True)  # Field name made lowercase.
    masseditinfo = models.BooleanField(db_column='MassEditInfo')  # Field name made lowercase.
    renameworkgroupcredential = models.BooleanField(db_column='RenameWorkgroupCredential')  # Field name made lowercase.
    wolport = models.IntegerField(db_column='Wolport')  # Field name made lowercase.
    defaultpackageshare = models.CharField(db_column='DefaultPackageShare', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    latestlspushversion = models.CharField(db_column='LatestLspushVersion', max_length=20, blank=True, null=True)  # Field name made lowercase.
    defaultshareusername = models.CharField(db_column='DefaultShareUsername', max_length=100, blank=True, null=True)  # Field name made lowercase.
    defaultsharepassword = models.CharField(db_column='DefaultSharePassword', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    assetstate = models.CharField(db_column='AssetState', max_length=200, blank=True, null=True)  # Field name made lowercase.
    deploymentrunmode = models.IntegerField(db_column='DeploymentRunMode', blank=True, null=True)  # Field name made lowercase.
    donotshrinklogfiles = models.BooleanField(db_column='DoNotShrinkLogFiles')  # Field name made lowercase.
    forcehttps = models.BooleanField(db_column='ForceHttps', blank=True, null=True)  # Field name made lowercase.
    showbanner = models.BooleanField(blank=True, null=True)
    banner = models.CharField(max_length=100, blank=True, null=True)
    adminlogin = models.BooleanField(blank=True, null=True)
    agentstrialmode = models.IntegerField(db_column='Agentstrialmode', blank=True, null=True)  # Field name made lowercase.
    agentstrialdateto = models.CharField(db_column='Agentstrialdateto', max_length=8, blank=True, null=True)  # Field name made lowercase.
    websiteaccess = models.CharField(db_column='WebsiteAccess', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    showrolechanges = models.BooleanField()
    defaultsharekeyhash = models.IntegerField(db_column='DefaultShareKeyHash', blank=True, null=True)  # Field name made lowercase.
    defaultlanguage = models.IntegerField(db_column='DefaultLanguage')  # Field name made lowercase.
    languageupdate = models.IntegerField(db_column='LanguageUpdate', blank=True, null=True)  # Field name made lowercase.
    servercurrentlyupdating = models.CharField(db_column='ServerCurrentlyUpdating', max_length=60, blank=True, null=True)  # Field name made lowercase.
    rebuildticketindex = models.BooleanField(db_column='rebuildTicketIndex', blank=True, null=True)  # Field name made lowercase.
    rebuildkbindex = models.BooleanField(db_column='rebuildKBIndex', blank=True, null=True)  # Field name made lowercase.
    usefileencryption = models.BooleanField(db_column='UseFileEncryption')  # Field name made lowercase.
    latestlsagentclientversion = models.CharField(db_column='LatestLsAgentClientVersion', max_length=20, blank=True, null=True)  # Field name made lowercase.
    hidecloudtab = models.BooleanField(db_column='HideCloudTab', blank=True, null=True)  # Field name made lowercase.
    alertreportrefresh = models.IntegerField(db_column='AlertReportRefresh')  # Field name made lowercase.
    installationmode = models.IntegerField(db_column='InstallationMode')  # Field name made lowercase.
    negotiatedterms = models.IntegerField(db_column='NegotiatedTerms', blank=True, null=True)  # Field name made lowercase.
    adminusername = models.CharField(db_column='AdminUserName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    adminpassword = models.CharField(db_column='AdminPassword', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    adminpasswordhash = models.IntegerField(db_column='AdminPasswordHash', blank=True, null=True)  # Field name made lowercase.
    isextendeddisplayscanningenabled = models.BooleanField(db_column='IsExtendedDisplayScanningEnabled')  # Field name made lowercase.
    forceextendeddisplayscan = models.BooleanField(db_column='ForceExtendedDisplayScan')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TsysConfig'


class Tsyscustomlayout(models.Model):
    loginlogo = models.CharField(max_length=50, blank=True, null=True)
    loginheaderheight = models.IntegerField()
    loginheaderimg = models.CharField(max_length=50, blank=True, null=True)
    loginheadercolor = models.CharField(max_length=10, blank=True, null=True)
    loginfootertext = models.CharField(max_length=200, blank=True, null=True)
    loginfootertextcolor = models.CharField(max_length=10, blank=True, null=True)
    loginfooterheight = models.IntegerField()
    loginfooterimg = models.CharField(max_length=50, blank=True, null=True)
    loginfootercolor = models.CharField(max_length=10, blank=True, null=True)
    logintitle = models.CharField(max_length=200, blank=True, null=True)
    loginmessage = models.TextField(blank=True, null=True)
    loginmessagecolor = models.CharField(max_length=10, blank=True, null=True)
    loginmessageposition = models.IntegerField(blank=True, null=True)
    showloginmessage = models.BooleanField(blank=True, null=True)
    showloginheader = models.BooleanField(blank=True, null=True)
    showloginfooter = models.BooleanField(blank=True, null=True)
    customlayoutid = models.AutoField(db_column='CustomLayoutID', primary_key=True)  # Field name made lowercase.
    uimodernization = models.BooleanField(db_column='UiModernization', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TsysCustomLayout'


class Tsysdonotscan(models.Model):
    assetname = models.CharField(db_column='Assetname', max_length=150)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=150, blank=True, null=True)  # Field name made lowercase.
    servername = models.ForeignKey('Tsysasservers', models.DO_NOTHING, db_column='ServerName', blank=True, null=True)  # Field name made lowercase.
    assetexclusionid = models.AutoField(db_column='AssetExclusionID', primary_key=True)  # Field name made lowercase.
    assetexclusionreasonid = models.ForeignKey('Tsysassetexclusionreason', models.DO_NOTHING, db_column='AssetExclusionReasonId', blank=True, null=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TsysDonotscan'


class Tsysfiles(models.Model):
    versionid = models.AutoField(db_column='VersionID', primary_key=True)  # Field name made lowercase.
    searchfile = models.CharField(db_column='Searchfile', max_length=1000)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TsysFiles'


class Tsyslastscan(models.Model):
    assetid = models.ForeignKey('Tblassets', models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    cfgcode = models.ForeignKey('Tsyswaittime', models.DO_NOTHING, db_column='CFGcode')  # Field name made lowercase.
    lasttime = models.DateTimeField(db_column='Lasttime')  # Field name made lowercase.
    scantime = models.DecimalField(db_column='Scantime', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lastscanid = models.BigAutoField(db_column='LastScanID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TsysLastscan'
        unique_together = (('assetid', 'cfgcode'),)


class Tsysmemorytypes(models.Model):
    memorytype = models.IntegerField(db_column='Memorytype', primary_key=True)  # Field name made lowercase.
    memoryname = models.CharField(db_column='MemoryName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TsysMemorytypes'


class Tsysregistry(models.Model):
    regid = models.AutoField(db_column='RegID', primary_key=True)  # Field name made lowercase.
    rootkey = models.CharField(db_column='Rootkey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    regpath = models.CharField(db_column='RegPath', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    regvalue = models.CharField(db_column='Regvalue', max_length=200, blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TsysRegistry'


class Tsysserials(models.Model):
    product = models.CharField(db_column='Product', primary_key=True, max_length=255)  # Field name made lowercase.
    regkey = models.CharField(db_column='Regkey', max_length=400)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    serialid = models.DecimalField(db_column='SerialID', max_digits=18, decimal_places=0)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=300)  # Field name made lowercase.
    variations = models.BooleanField(db_column='Variations')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TsysSerials'


class Tsyswaittime(models.Model):
    cfgcode = models.IntegerField(db_column='CFGCode', primary_key=True)  # Field name made lowercase.
    cfgname = models.CharField(db_column='CFGname', unique=True, max_length=20)  # Field name made lowercase.
    waitdays = models.DecimalField(db_column='Waitdays', max_digits=18, decimal_places=0)  # Field name made lowercase.
    trackchanges = models.BooleanField(db_column='Trackchanges', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TsysWaittime'


class Tsyswarrantyqueue(models.Model):
    assetid = models.OneToOneField('Tblassets', models.DO_NOTHING, db_column='AssetId', primary_key=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TimeStamp')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TsysWarrantyQueue'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Htblagentconfig(models.Model):
    agentconfigid = models.AutoField(primary_key=True)
    agentid = models.ForeignKey('Htblagents', models.DO_NOTHING, db_column='agentid')
    shortcuts = models.BooleanField(blank=True, null=True)
    emailoncreation = models.BooleanField(blank=True, null=True)
    emailonassigned = models.BooleanField(blank=True, null=True)
    emailonagentupdate = models.BooleanField(blank=True, null=True)
    emailonclientupdate = models.BooleanField(blank=True, null=True)
    emailonstatechange = models.BooleanField(blank=True, null=True)
    emailonmyupdate = models.BooleanField(blank=True, null=True)
    emailonteamchange = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'htblagentconfig'


class Htblagentlicenses(models.Model):
    licenseid = models.AutoField(primary_key=True)
    key = models.CharField(max_length=2000)
    orderreference = models.CharField(max_length=250, blank=True, null=True)
    licensee = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblagentlicenses'


class Htblagents(models.Model):
    agentid = models.AutoField(primary_key=True)
    userid = models.OneToOneField('Htblusers', models.DO_NOTHING, db_column='userid')
    active = models.BooleanField(blank=True, null=True)
    notificationschecked = models.DateTimeField()
    footer = models.TextField(blank=True, null=True)
    disabledbysystem = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'htblagents'


class Htblagentteam(models.Model):
    agentid = models.OneToOneField(Htblagents, models.DO_NOTHING, db_column='agentid', primary_key=True)
    teamid = models.ForeignKey('Htblteams', models.DO_NOTHING, db_column='teamid')
    webroleid = models.ForeignKey('Htblwebroles', models.DO_NOTHING, db_column='webroleid')

    class Meta:
        managed = False
        db_table = 'htblagentteam'
        unique_together = (('agentid', 'teamid', 'webroleid'),)


class Htblassignexclusions(models.Model):
    assignexclusionid = models.AutoField(primary_key=True)
    type = models.IntegerField()
    typeid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'htblassignexclusions'


class Htblattachements(models.Model):
    attachmentid = models.AutoField(primary_key=True)
    noteid = models.ForeignKey('Htblnotes', models.DO_NOTHING, db_column='noteid')
    fileid = models.ForeignKey('Htblfiles', models.DO_NOTHING, db_column='fileid')
    mediatype = models.CharField(max_length=100)
    contentid = models.CharField(max_length=100, blank=True, null=True)
    filename = models.CharField(max_length=256, blank=True, null=True)
    deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'htblattachements'


class Htblautomaticclose(models.Model):
    autocloseid = models.AutoField(primary_key=True)
    time1 = models.IntegerField()
    time2 = models.IntegerField()
    time3 = models.IntegerField()
    day1 = models.BooleanField()
    day2 = models.BooleanField()
    day3 = models.BooleanField()
    mail1 = models.BooleanField()
    mail2 = models.BooleanField()
    message1 = models.TextField()
    message2 = models.TextField()
    lastedited = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblautomaticclose'


class Htblautomaticcloselang(models.Model):
    autocloseid = models.OneToOneField(Htblautomaticclose, models.DO_NOTHING, db_column='autocloseid', primary_key=True)
    language = models.IntegerField()
    message1 = models.TextField(blank=True, null=True)
    message2 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblautomaticcloseLang'
        unique_together = (('autocloseid', 'language'),)


class Htblautomaticcloseticketstates(models.Model):
    autocloseid = models.OneToOneField(Htblautomaticclose, models.DO_NOTHING, db_column='autocloseid', primary_key=True)
    ticketstateid = models.ForeignKey('Htblticketstates', models.DO_NOTHING, db_column='ticketstateid')

    class Meta:
        managed = False
        db_table = 'htblautomaticcloseticketstates'
        unique_together = (('autocloseid', 'ticketstateid'),)


class Htblautomaticclosetickettypes(models.Model):
    autocloseid = models.OneToOneField(Htblautomaticclose, models.DO_NOTHING, db_column='autocloseid', primary_key=True)
    tickettypeid = models.ForeignKey('Htbltickettypes', models.DO_NOTHING, db_column='tickettypeid')

    class Meta:
        managed = False
        db_table = 'htblautomaticclosetickettypes'
        unique_together = (('autocloseid', 'tickettypeid'),)


class Htblbusinesshours(models.Model):
    mon = models.DateTimeField()
    mon2 = models.DateTimeField()
    tue = models.DateTimeField()
    tue2 = models.DateTimeField()
    wed = models.DateTimeField()
    wed2 = models.DateTimeField()
    thu = models.DateTimeField()
    thu2 = models.DateTimeField()
    fri = models.DateTimeField()
    fri2 = models.DateTimeField()
    sat = models.DateTimeField()
    sat2 = models.DateTimeField()
    sun = models.DateTimeField()
    sun2 = models.DateTimeField()
    monnot = models.BooleanField(blank=True, null=True)
    tuenot = models.BooleanField(blank=True, null=True)
    wednot = models.BooleanField(blank=True, null=True)
    thunot = models.BooleanField(blank=True, null=True)
    frinot = models.BooleanField(blank=True, null=True)
    satnot = models.BooleanField(blank=True, null=True)
    sunnot = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblbusinesshours'


class Htblcalendarsettings(models.Model):
    settingid = models.AutoField(db_column='SettingID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    eventtypefilter = models.CharField(db_column='EventTypeFilter', max_length=100, blank=True, null=True)  # Field name made lowercase.
    agentfilter = models.CharField(db_column='AgentFilter', max_length=100, blank=True, null=True)  # Field name made lowercase.
    teamfilter = models.CharField(db_column='TeamFilter', max_length=100, blank=True, null=True)  # Field name made lowercase.
    myeventfilter = models.BooleanField(db_column='MyEventFilter', blank=True, null=True)  # Field name made lowercase.
    disabledeventtypes = models.CharField(db_column='DisabledEventTypes', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'htblcalendarsettings'


class Htblcustomfields(models.Model):
    fieldid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    type = models.IntegerField()
    labeltext = models.CharField(max_length=500, blank=True, null=True)
    editable = models.BooleanField()
    showinoverview = models.BooleanField(blank=True, null=True)
    showinsummary = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblcustomfields'


class Htblcustomfieldslang(models.Model):
    fieldid = models.OneToOneField(Htblcustomfields, models.DO_NOTHING, db_column='fieldid', primary_key=True)
    language = models.IntegerField()
    name = models.CharField(max_length=500, blank=True, null=True)
    labeltext = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblcustomfieldsLang'
        unique_together = (('fieldid', 'language'),)


class Htblcustomfieldvaluelinks(models.Model):
    linkid = models.AutoField(primary_key=True)
    fieldvalueid = models.ForeignKey('Htblcustomfieldvalues', models.DO_NOTHING, db_column='fieldvalueid')
    fieldid = models.ForeignKey('Htbltickettypecustomfield', models.DO_NOTHING, db_column='fieldid')
    sortorder = models.IntegerField(blank=True, null=True)
    parentfieldid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblcustomfieldvaluelinks'


class Htblcustomfieldvalues(models.Model):
    fieldvalueid = models.AutoField(primary_key=True)
    fieldid = models.ForeignKey(Htblcustomfields, models.DO_NOTHING, db_column='fieldid')
    value = models.CharField(max_length=500, blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    color2 = models.CharField(max_length=10, blank=True, null=True)
    visible = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'htblcustomfieldvalues'


class Htblcustomticketfilteritems(models.Model):
    filteritemid = models.AutoField(primary_key=True)
    filterid = models.ForeignKey('Htblcustomticketfilters', models.DO_NOTHING, db_column='filterid')
    type = models.IntegerField()
    itemid = models.IntegerField()
    value = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblcustomticketfilteritems'


class Htblcustomticketfilters(models.Model):
    filterid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    agents = models.CharField(max_length=500)
    clients = models.CharField(max_length=500)
    flagged = models.IntegerField()
    datefrom = models.DateTimeField(blank=True, null=True)
    dateto = models.DateTimeField(blank=True, null=True)
    spam = models.BooleanField(blank=True, null=True)
    userid = models.ForeignKey('Htblusers', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    assigned = models.BooleanField(blank=True, null=True)
    unassigned = models.BooleanField(blank=True, null=True)
    related = models.BooleanField(blank=True, null=True)
    slaovertime = models.BooleanField(blank=True, null=True)
    subscribed = models.BooleanField(blank=True, null=True)
    agentinit = models.BooleanField(blank=True, null=True)
    search = models.CharField(max_length=150, blank=True, null=True)
    unanswered = models.BooleanField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    order = models.CharField(max_length=5, blank=True, null=True)
    top = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblcustomticketfilters'


class Htbldeadlines(models.Model):
    deadlineid = models.AutoField(primary_key=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    time = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htbldeadlines'


class Htblemailaccountaliases(models.Model):
    aliasid = models.AutoField(primary_key=True)
    accountid = models.ForeignKey('Htblemailaccounts', models.DO_NOTHING, db_column='accountid')
    displayname = models.CharField(max_length=150)
    email = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'htblemailaccountaliases'


class Htblemailaccounts(models.Model):
    accountid = models.AutoField(primary_key=True)
    smtpserver = models.CharField(db_column='SMTPserver', max_length=250)  # Field name made lowercase.
    incomingmailserver = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    displayname = models.CharField(max_length=250)
    sslincoming = models.IntegerField(blank=True, null=True)
    ssloutgoing = models.IntegerField(blank=True, null=True)
    authenticationincoming = models.BooleanField(blank=True, null=True)
    authenticationoutgoing = models.BooleanField(blank=True, null=True)
    usernameincoming = models.CharField(max_length=50, blank=True, null=True)
    usernameoutgoing = models.CharField(max_length=50, blank=True, null=True)
    passwordincoming = models.CharField(max_length=1000, blank=True, null=True)
    passwordoutgoing = models.CharField(max_length=1000, blank=True, null=True)
    smtpport = models.IntegerField(db_column='SMTPport')  # Field name made lowercase.
    serverport = models.IntegerField()
    default = models.BooleanField(blank=True, null=True)
    protocol = models.SmallIntegerField()
    inboxfolders = models.CharField(max_length=500)
    archivefolder = models.CharField(max_length=500)
    trashfolder = models.CharField(max_length=500)
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    errorincoming = models.SmallIntegerField(blank=True, null=True)
    erroroutgoing = models.SmallIntegerField(blank=True, null=True)
    lasttried = models.DateTimeField(blank=True, null=True)
    aliases = models.TextField(blank=True, null=True)
    passwordkeyhash = models.IntegerField(db_column='PasswordKeyHash', blank=True, null=True)  # Field name made lowercase.
    noincoming = models.BooleanField()
    nooutgoing = models.BooleanField()
    protocoloutgoing = models.SmallIntegerField()
    clientidincoming = models.CharField(db_column='ClientIdIncoming', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tenantidincoming = models.CharField(db_column='TenantIdIncoming', max_length=36, blank=True, null=True)  # Field name made lowercase.
    clientsecretincoming = models.CharField(db_column='ClientSecretIncoming', max_length=200, blank=True, null=True)  # Field name made lowercase.
    clientidoutgoing = models.CharField(db_column='ClientIdOutgoing', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tenantidoutgoing = models.CharField(db_column='TenantIdOutgoing', max_length=36, blank=True, null=True)  # Field name made lowercase.
    clientsecretoutgoing = models.CharField(db_column='ClientSecretOutgoing', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'htblemailaccounts'


class Htblemailaccountslang(models.Model):
    accountid = models.OneToOneField(Htblemailaccounts, models.DO_NOTHING, db_column='accountid', primary_key=True)
    language = models.IntegerField()
    displayname = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblemailaccountsLang'
        unique_together = (('accountid', 'language'),)


class Htblemailaccountsteams(models.Model):
    teamid = models.OneToOneField('Htblteams', models.DO_NOTHING, db_column='teamid', primary_key=True)
    accountid = models.ForeignKey(Htblemailaccounts, models.DO_NOTHING, db_column='accountid')

    class Meta:
        managed = False
        db_table = 'htblemailaccountsteams'
        unique_together = (('teamid', 'accountid'),)


class Htblemailfilters(models.Model):
    filterid = models.AutoField(primary_key=True)
    type = models.IntegerField()
    filter = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblemailfilters'


class Htblemailsetup(models.Model):
    timeout = models.IntegerField()
    historytime = models.IntegerField()
    historytype = models.IntegerField()
    rejectunknownid = models.BooleanField(blank=True, null=True)
    addnewclient = models.IntegerField(blank=True, null=True)
    accepteddomains = models.CharField(max_length=2500, blank=True, null=True)
    includegraphics = models.BooleanField(blank=True, null=True)
    clayoutclient = models.IntegerField(blank=True, null=True)
    clayoutticket = models.IntegerField(blank=True, null=True)
    clayoutnotes = models.IntegerField(blank=True, null=True)
    cnotes = models.IntegerField(blank=True, null=True)
    alayoutclient = models.IntegerField(blank=True, null=True)
    alayoutticket = models.IntegerField(blank=True, null=True)
    alayoutnotes = models.IntegerField(blank=True, null=True)
    anotes = models.IntegerField(blank=True, null=True)
    interfacelinks = models.BooleanField(blank=True, null=True)
    actionlinks = models.BooleanField(blank=True, null=True)
    threshold = models.IntegerField(blank=True, null=True)
    footer = models.TextField(blank=True, null=True)  # This field type is a guess.
    emailprefix = models.CharField(max_length=50, blank=True, null=True)
    cannotaddclient = models.BooleanField(blank=True, null=True)
    cannotaddclienttext = models.CharField(max_length=1000, blank=True, null=True)
    interfacelinkhostname = models.CharField(max_length=250, blank=True, null=True)
    divider = models.CharField(max_length=250, blank=True, null=True)
    dividerregex = models.CharField(max_length=250, blank=True, null=True)
    historycleanup = models.DateTimeField()
    allowkblinks = models.BooleanField(blank=True, null=True)
    emailstyle = models.IntegerField()
    footertype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'htblemailsetup'


class Htblemailtemplates(models.Model):
    templateid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    outgoing = models.BooleanField()
    replytype = models.IntegerField(blank=True, null=True)
    addnotehistory = models.BooleanField(blank=True, null=True)
    subject = models.CharField(max_length=250, blank=True, null=True)
    enabled = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblemailtemplates'


class Htblemailtemplateslang(models.Model):
    templateid = models.OneToOneField(Htblemailtemplates, models.DO_NOTHING, db_column='templateid', primary_key=True)
    language = models.IntegerField()
    name = models.CharField(max_length=250, blank=True, null=True)
    subject = models.CharField(max_length=250, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblemailtemplatesLang'
        unique_together = (('templateid', 'language'),)


class Htblemailtemplatesattachements(models.Model):
    attachmentid = models.AutoField(primary_key=True)
    templateid = models.ForeignKey(Htblemailtemplates, models.DO_NOTHING, db_column='templateid', blank=True, null=True)
    fileid = models.ForeignKey('Htblfiles', models.DO_NOTHING, db_column='fileid')
    mediatype = models.CharField(max_length=100)
    contentid = models.CharField(max_length=100, blank=True, null=True)
    filename = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'htblemailtemplatesattachements'


class Htblemailtemplatespriorities(models.Model):
    templateid = models.OneToOneField(Htblemailtemplates, models.DO_NOTHING, db_column='templateid', primary_key=True)
    priority = models.ForeignKey('Htblpriorities', models.DO_NOTHING, db_column='priority')

    class Meta:
        managed = False
        db_table = 'htblemailtemplatespriorities'
        unique_together = (('templateid', 'priority'),)


class Htblemailtemplatesticketstates(models.Model):
    templateid = models.OneToOneField(Htblemailtemplates, models.DO_NOTHING, db_column='templateid', primary_key=True)
    ticketstateid = models.ForeignKey('Htblticketstates', models.DO_NOTHING, db_column='ticketstateid')

    class Meta:
        managed = False
        db_table = 'htblemailtemplatesticketstates'
        unique_together = (('templateid', 'ticketstateid'),)


class Htblemailtemplatestickettypes(models.Model):
    templateid = models.OneToOneField(Htblemailtemplates, models.DO_NOTHING, db_column='templateid', primary_key=True)
    tickettypeid = models.ForeignKey('Htbltickettypes', models.DO_NOTHING, db_column='tickettypeid')

    class Meta:
        managed = False
        db_table = 'htblemailtemplatestickettypes'
        unique_together = (('templateid', 'tickettypeid'),)


class Htblemailverification(models.Model):
    verificationid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('Htblusers', models.DO_NOTHING, db_column='userid')
    email = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'htblemailverification'


class Htbleventinfochecks(models.Model):
    eventcheckid = models.AutoField(db_column='EventCheckID', primary_key=True)  # Field name made lowercase.
    agentid = models.IntegerField(db_column='AgentID')  # Field name made lowercase.
    infoid = models.ForeignKey('Htblscheduleinfo', models.DO_NOTHING, db_column='InfoID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'htbleventinfochecks'


class Htbleventreminders(models.Model):
    eventreminderid = models.AutoField(db_column='EventReminderID', primary_key=True)  # Field name made lowercase.
    agentid = models.IntegerField(db_column='AgentID')  # Field name made lowercase.
    eventid = models.ForeignKey('Htblschedule', models.DO_NOTHING, db_column='EventID')  # Field name made lowercase.
    checked = models.BooleanField(db_column='Checked')  # Field name made lowercase.
    nextreminder = models.DateTimeField(db_column='NextReminder', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'htbleventreminders'


class Htblfiles(models.Model):
    fileid = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=50, blank=True, null=True)
    bithash = models.CharField(unique=True, max_length=250, blank=True, null=True)
    uploaded = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblfiles'


class Htblfooterattachements(models.Model):
    attachmentid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('Htblusers', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    fileid = models.ForeignKey(Htblfiles, models.DO_NOTHING, db_column='fileid')
    mediatype = models.CharField(max_length=100)
    contentid = models.CharField(max_length=100, blank=True, null=True)
    filename = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblfooterattachements'


class Htblhistory(models.Model):
    histid = models.AutoField(primary_key=True)
    action = models.CharField(max_length=4000, blank=True, null=True)
    userid = models.ForeignKey('Htblusers', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    ticketid = models.ForeignKey('Htblticket', models.DO_NOTHING, db_column='ticketid', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    typeid = models.ForeignKey('Htblhistorytypes', models.DO_NOTHING, db_column='typeid')
    status = models.IntegerField(blank=True, null=True)
    reason = models.CharField(max_length=100, blank=True, null=True)
    ticketstateid = models.IntegerField(blank=True, null=True)
    tickettypeid = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    teamid = models.IntegerField(blank=True, null=True)
    agentid = models.IntegerField(blank=True, null=True)
    assetid = models.IntegerField(blank=True, null=True)
    scheduleid = models.IntegerField(blank=True, null=True)
    noteid = models.IntegerField(blank=True, null=True)
    fieldid = models.IntegerField(blank=True, null=True)
    ruleid = models.IntegerField(blank=True, null=True)
    userid2 = models.ForeignKey('Htblusers', models.DO_NOTHING, db_column='userid2', blank=True, null=True)
    userid3 = models.ForeignKey('Htblusers', models.DO_NOTHING, db_column='userid3', blank=True, null=True)
    agentid2 = models.ForeignKey(Htblagents, models.DO_NOTHING, db_column='agentid2', blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    unauthorised = models.BooleanField(blank=True, null=True)
    luceneadded = models.BooleanField(blank=True, null=True)
    newvalue = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblhistory'


class Htblhistorytypes(models.Model):
    typeid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'htblhistorytypes'


class Htblknowledgebase(models.Model):
    kbid = models.AutoField(primary_key=True)
    attachementid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    categoryid = models.ForeignKey('Htblknowledgebasecategories', models.DO_NOTHING, db_column='categoryid')
    sortorder = models.IntegerField()
    added = models.DateTimeField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    alteredby = models.IntegerField(blank=True, null=True)
    altered = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblknowledgebase'


class Htblknowledgebaselang(models.Model):
    kbid = models.OneToOneField(Htblknowledgebase, models.DO_NOTHING, db_column='kbid', primary_key=True)
    language = models.IntegerField()
    name = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblknowledgebaseLang'
        unique_together = (('kbid', 'language'),)


class Htblknowledgebaseattachments(models.Model):
    attachmentid = models.AutoField(primary_key=True)
    kbid = models.ForeignKey(Htblknowledgebase, models.DO_NOTHING, db_column='kbid')
    fileid = models.ForeignKey(Htblfiles, models.DO_NOTHING, db_column='fileid')
    mediatype = models.CharField(max_length=100)
    contentid = models.CharField(max_length=100, blank=True, null=True)
    filename = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblknowledgebaseattachments'


class Htblknowledgebasecategories(models.Model):
    categoryid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    sortorder = models.IntegerField()
    color = models.CharField(max_length=10, blank=True, null=True)
    useraccess = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblknowledgebasecategories'


class Htblknowledgebasecategorieslang(models.Model):
    categoryid = models.OneToOneField(Htblknowledgebasecategories, models.DO_NOTHING, db_column='categoryid', primary_key=True)
    language = models.IntegerField()
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblknowledgebasecategoriesLang'
        unique_together = (('categoryid', 'language'),)


class Htblknowledgebasecategoriesteams(models.Model):
    linkid = models.AutoField(primary_key=True)
    categoryid = models.ForeignKey(Htblknowledgebasecategories, models.DO_NOTHING, db_column='categoryid')
    teamid = models.ForeignKey('Htblteams', models.DO_NOTHING, db_column='teamid')
    editaccess = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblknowledgebasecategoriesteams'


class Htbllook(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    singlebg = models.BooleanField(blank=True, null=True)
    colorbg = models.CharField(max_length=10, blank=True, null=True)
    colorgradient1 = models.CharField(max_length=10, blank=True, null=True)
    colorgradient2 = models.CharField(max_length=10, blank=True, null=True)
    colortext = models.CharField(max_length=10, blank=True, null=True)
    font = models.CharField(max_length=50, blank=True, null=True)
    tabcolor = models.CharField(max_length=10, blank=True, null=True)
    tabtext = models.CharField(max_length=10, blank=True, null=True)
    selectedtabcolor = models.CharField(max_length=10, blank=True, null=True)
    selectedtabtext = models.CharField(max_length=10, blank=True, null=True)
    showname = models.BooleanField(blank=True, null=True)
    nameshadow = models.BooleanField(blank=True, null=True)
    customheader = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htbllook'


class Htblnews(models.Model):
    newsid = models.AutoField(primary_key=True)
    type = models.IntegerField()
    text = models.TextField()
    description = models.CharField(max_length=100)
    enabled = models.BooleanField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblnews'


class Htblnewslang(models.Model):
    newsid = models.OneToOneField(Htblnews, models.DO_NOTHING, db_column='newsid', primary_key=True)
    language = models.IntegerField()
    description = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblnewsLang'
        unique_together = (('newsid', 'language'),)


class Htblnotehistory(models.Model):
    notehistoryid = models.AutoField(primary_key=True)
    noteid = models.ForeignKey('Htblnotes', models.DO_NOTHING, db_column='noteid')
    note = models.TextField(blank=True, null=True)
    userid = models.ForeignKey('Htblusers', models.DO_NOTHING, db_column='userid')
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblnotehistory'


class Htblnotes(models.Model):
    noteid = models.AutoField(primary_key=True)
    ticketid = models.ForeignKey('Htblticket', models.DO_NOTHING, db_column='ticketid', blank=True, null=True)
    userid = models.ForeignKey('Htblusers', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    date = models.DateTimeField()
    note = models.TextField(blank=True, null=True)
    notetype = models.IntegerField(blank=True, null=True)
    emailmessageid = models.CharField(max_length=1024, blank=True, null=True)
    servicechange = models.BooleanField(blank=True, null=True)
    timeworkeduserid = models.IntegerField(blank=True, null=True)
    timeworkeddate = models.DateTimeField(blank=True, null=True)
    timeworked = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblnotes'


class Htblnotificationschecked(models.Model):
    checkid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('Htblusers', models.DO_NOTHING, db_column='userid')
    histid = models.ForeignKey(Htblhistory, models.DO_NOTHING, db_column='histid')

    class Meta:
        managed = False
        db_table = 'htblnotificationschecked'


class Htbloldticketdata(models.Model):
    oldid = models.AutoField(primary_key=True)
    ticketid = models.ForeignKey('Htblticket', models.DO_NOTHING, db_column='ticketid')
    subject = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    changed = models.DateTimeField(blank=True, null=True)
    userid = models.ForeignKey('Htblusers', models.DO_NOTHING, db_column='userid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htbloldticketdata'


class Htblpriorities(models.Model):
    priority = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    sortorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblpriorities'


class Htblprioritieslang(models.Model):
    priority = models.OneToOneField(Htblpriorities, models.DO_NOTHING, db_column='priority', primary_key=True)
    language = models.IntegerField()
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblprioritiesLang'
        unique_together = (('priority', 'language'),)


class Htblreports(models.Model):
    reportid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    query = models.TextField()
    builtin = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblreports'


class Htblreportslang(models.Model):
    reportid = models.OneToOneField(Htblreports, models.DO_NOTHING, db_column='reportid', primary_key=True)
    language = models.IntegerField()
    title = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblreportsLang'
        unique_together = (('reportid', 'language'),)


class Htblsavedcustomfilters(models.Model):
    saveid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('Htblusers', models.DO_NOTHING, db_column='userid')
    filterdata = models.CharField(max_length=2500)
    sortorder = models.IntegerField()
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblsavedcustomfilters'


class Htblschedule(models.Model):
    scheduleid = models.AutoField(primary_key=True)
    ticketid = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=4000, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    typeid = models.ForeignKey('Htblscheduletypes', models.DO_NOTHING, db_column='typeid', blank=True, null=True)
    allday = models.BooleanField(blank=True, null=True)
    public = models.BooleanField(blank=True, null=True)
    showtoteam = models.BooleanField(blank=True, null=True)
    createdby = models.ForeignKey(Htblagents, models.DO_NOTHING, db_column='createdby', blank=True, null=True)
    alteredby = models.IntegerField(blank=True, null=True)
    reminder = models.IntegerField(blank=True, null=True)
    deleted = models.BooleanField()
    processed = models.BooleanField(db_column='Processed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'htblschedule'


class Htblscheduleagents(models.Model):
    scheduleagentid = models.AutoField(primary_key=True)
    scheduleid = models.ForeignKey(Htblschedule, models.DO_NOTHING, db_column='scheduleid')
    agentid = models.IntegerField()
    nextreminder = models.DateTimeField()
    status = models.BooleanField()
    checked = models.BooleanField()
    editallowed = models.BooleanField(db_column='editAllowed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'htblscheduleagents'


class Htblscheduleinfo(models.Model):
    infoid = models.AutoField(primary_key=True)
    agentid = models.ForeignKey(Htblagents, models.DO_NOTHING, db_column='agentid', blank=True, null=True)
    scheduleid = models.IntegerField(blank=True, null=True)
    infotype = models.IntegerField()
    title = models.CharField(max_length=150, blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    datechanged = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblscheduleinfo'


class Htblschedulerepeat(models.Model):
    repeatid = models.AutoField(primary_key=True)
    scheduleid = models.OneToOneField(Htblschedule, models.DO_NOTHING, db_column='scheduleid')
    repeattype = models.IntegerField()
    amount = models.IntegerField()
    dayofmonth = models.BooleanField()
    day = models.IntegerField(blank=True, null=True)
    ends = models.IntegerField()
    occurrences = models.IntegerField(blank=True, null=True)
    weekdays = models.CharField(max_length=7)
    enddate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblschedulerepeat'


class Htblscheduleteams(models.Model):
    scheduleteamid = models.AutoField(db_column='ScheduleTeamID', primary_key=True)  # Field name made lowercase.
    scheduleid = models.ForeignKey(Htblschedule, models.DO_NOTHING, db_column='ScheduleID')  # Field name made lowercase.
    teamid = models.ForeignKey('Htblteams', models.DO_NOTHING, db_column='TeamID')  # Field name made lowercase.
    editallowed = models.BooleanField(db_column='EditAllowed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'htblscheduleteams'


class Htblscheduletypes(models.Model):
    typeid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=10, blank=True, null=True)
    agentavailable = models.BooleanField(blank=True, null=True)
    default = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'htblscheduletypes'


class Htblscheduletypeslang(models.Model):
    typeid = models.OneToOneField(Htblscheduletypes, models.DO_NOTHING, db_column='typeid', primary_key=True)
    language = models.IntegerField()
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblscheduletypesLang'
        unique_together = (('typeid', 'language'),)


class Htblserviceactions(models.Model):
    actionid = models.IntegerField(primary_key=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    compare = models.CharField(max_length=50, blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    comparevalue = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblserviceactions'


class Htblsetup(models.Model):
    defaultpriority = models.IntegerField(blank=True, null=True)
    editwarning = models.IntegerField(blank=True, null=True)
    emailtickets = models.BooleanField(blank=True, null=True)
    consoletickets = models.BooleanField(blank=True, null=True)
    allowmerging = models.BooleanField(blank=True, null=True)
    allowattachments = models.BooleanField(blank=True, null=True)
    sortascending = models.BooleanField(blank=True, null=True)
    selectunrelated = models.BooleanField(blank=True, null=True)
    selectsamelocation = models.BooleanField(blank=True, null=True)
    showschedule = models.BooleanField(blank=True, null=True)
    showduedate = models.BooleanField(blank=True, null=True)
    clientcc = models.BooleanField(blank=True, null=True)
    showagentnotes = models.BooleanField(blank=True, null=True)
    autoassign = models.BooleanField(blank=True, null=True)
    assigntocreator = models.BooleanField(blank=True, null=True)
    assigntype = models.IntegerField(blank=True, null=True)
    assignwhen = models.IntegerField(blank=True, null=True)
    assigntoeditor = models.BooleanField(blank=True, null=True)
    standarddeadline = models.BigIntegerField()
    maxkbarticles = models.IntegerField()
    defaulttickettype = models.IntegerField(blank=True, null=True)
    pasteventsdeletion = models.IntegerField()
    attachmentsfolder = models.CharField(max_length=200, blank=True, null=True)
    usecustomfolder = models.BooleanField(blank=True, null=True)
    attfolderlogin = models.CharField(max_length=100, blank=True, null=True)
    attfolderpass = models.CharField(max_length=500, blank=True, null=True)
    clientsaddemail = models.BooleanField(blank=True, null=True)
    keepspamdays = models.IntegerField(blank=True, null=True)
    firstrun = models.BooleanField(blank=True, null=True)
    usedeadlines = models.BooleanField(blank=True, null=True)
    kbenabled = models.BooleanField(blank=True, null=True)
    kbagentonly = models.BooleanField(blank=True, null=True)
    defaultteamid = models.IntegerField(blank=True, null=True)
    shortcuts = models.BooleanField(blank=True, null=True)
    servernamechanged = models.BooleanField(blank=True, null=True)
    showpriority = models.BooleanField(blank=True, null=True)
    ticketshover = models.IntegerField(blank=True, null=True)
    allowselectotheruser = models.BooleanField(blank=True, null=True)
    clientclose = models.BooleanField(blank=True, null=True)
    attfolderkeyhash = models.IntegerField(blank=True, null=True)
    disablehelpdesk = models.BooleanField(blank=True, null=True)
    showkbembeddedimages = models.BooleanField(blank=True, null=True)
    kbattachmentstop = models.BooleanField(blank=True, null=True)
    defaultsourceid = models.IntegerField(blank=True, null=True)
    kbsort = models.IntegerField(blank=True, null=True)
    autoticketlink = models.BooleanField(blank=True, null=True)
    disablenoteemails = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'htblsetup'


class Htblshortcuts(models.Model):
    keyid = models.IntegerField(primary_key=True)
    effect = models.CharField(max_length=50)
    code = models.IntegerField()
    key = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'htblshortcuts'


class Htblshortcutslang(models.Model):
    keyid = models.OneToOneField(Htblshortcuts, models.DO_NOTHING, db_column='keyid', primary_key=True)
    language = models.IntegerField()
    effect = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblshortcutsLang'
        unique_together = (('keyid', 'language'),)


class Htblshownclientrelations(models.Model):
    relationtypeid = models.OneToOneField('Tsysassetrelationtypes', models.DO_NOTHING, db_column='RelationTypeID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'htblshownclientrelations'


class Htblsla(models.Model):
    slaid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)
    hours = models.IntegerField()
    initial = models.DateTimeField()
    resolved = models.DateTimeField()
    color1 = models.CharField(max_length=10)
    color2 = models.CharField(max_length=10)
    sortorder = models.IntegerField()
    enabled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'htblsla'


class Htblslacompanies(models.Model):
    slaid = models.ForeignKey(Htblsla, models.DO_NOTHING, db_column='slaid')
    company = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'htblslacompanies'


class Htblsladepartments(models.Model):
    slaid = models.ForeignKey(Htblsla, models.DO_NOTHING, db_column='slaid')
    department = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'htblsladepartments'


class Htblslapriorities(models.Model):
    slaid = models.ForeignKey(Htblsla, models.DO_NOTHING, db_column='slaid')
    priority = models.ForeignKey(Htblpriorities, models.DO_NOTHING, db_column='priority')

    class Meta:
        managed = False
        db_table = 'htblslapriorities'


class Htblslasource(models.Model):
    slaid = models.OneToOneField(Htblsla, models.DO_NOTHING, db_column='slaid', primary_key=True)
    sourceid = models.ForeignKey('Htblsource', models.DO_NOTHING, db_column='sourceid')

    class Meta:
        managed = False
        db_table = 'htblslasource'
        unique_together = (('slaid', 'sourceid'),)


class Htblslatickettypes(models.Model):
    slaid = models.OneToOneField(Htblsla, models.DO_NOTHING, db_column='slaid', primary_key=True)
    tickettypeid = models.ForeignKey('Htbltickettypes', models.DO_NOTHING, db_column='tickettypeid')

    class Meta:
        managed = False
        db_table = 'htblslatickettypes'
        unique_together = (('slaid', 'tickettypeid'),)


class Htblslausers(models.Model):
    slaid = models.OneToOneField(Htblsla, models.DO_NOTHING, db_column='slaid', primary_key=True)
    userid = models.ForeignKey('Htblusers', models.DO_NOTHING, db_column='userid')

    class Meta:
        managed = False
        db_table = 'htblslausers'
        unique_together = (('slaid', 'userid'),)


class Htblsource(models.Model):
    sourceid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    description = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblsource'


class Htblsourcelang(models.Model):
    sourceid = models.OneToOneField('self', models.DO_NOTHING, db_column='sourceid', primary_key=True)
    language = models.ForeignKey('self', models.DO_NOTHING, db_column='language')
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblsourcelang'
        unique_together = (('sourceid', 'language'),)


class Htblspecialrules(models.Model):
    ruleid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=4000)
    sortorder = models.IntegerField(blank=True, null=True)
    enabled = models.BooleanField(blank=True, null=True)
    stopdispatching = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblspecialrules'


class Htblspecialrulesactions(models.Model):
    actionid = models.AutoField(primary_key=True)
    ruleid = models.ForeignKey(Htblspecialrules, models.DO_NOTHING, db_column='ruleid')
    type = models.IntegerField()
    typeid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'htblspecialrulesactions'


class Htblspecialrulesconditions(models.Model):
    conditionid = models.AutoField(primary_key=True)
    ruleid = models.ForeignKey(Htblspecialrules, models.DO_NOTHING, db_column='ruleid')
    type = models.IntegerField()
    condition = models.IntegerField()
    text = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'htblspecialrulesconditions'


class Htblspecialrulestaskagents(models.Model):
    ruletaskagentid = models.AutoField(primary_key=True)
    ruletaskid = models.ForeignKey('Htblspecialrulestasks', models.DO_NOTHING, db_column='ruletaskid')
    agentid = models.ForeignKey(Htblagents, models.DO_NOTHING, db_column='agentid')
    editallowed = models.BooleanField(db_column='editAllowed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'htblspecialrulestaskagents'


class Htblspecialrulestasks(models.Model):
    taskid = models.AutoField(primary_key=True)
    ruleid = models.IntegerField()
    typeid = models.IntegerField()
    minutesdelay = models.IntegerField()
    minutesrequired = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=4000)
    allday = models.BooleanField(blank=True, null=True)
    showtoteam = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblspecialrulestasks'


class Htblspecialrulestaskteams(models.Model):
    ruletaskteamid = models.AutoField(primary_key=True)
    ruletaskid = models.ForeignKey(Htblspecialrulestasks, models.DO_NOTHING, db_column='ruletaskid')
    teamid = models.ForeignKey('Htblteams', models.DO_NOTHING, db_column='teamid')
    editallowed = models.BooleanField(db_column='editAllowed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'htblspecialrulestaskteams'


class Htblteams(models.Model):
    teamid = models.AutoField(primary_key=True)
    teamname = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    img = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblteams'


class Htblteamslang(models.Model):
    teamid = models.OneToOneField(Htblteams, models.DO_NOTHING, db_column='teamid', primary_key=True)
    language = models.IntegerField()
    teamname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblteamsLang'
        unique_together = (('teamid', 'language'),)


class Htbltemplatecategories(models.Model):
    categoryid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'htbltemplatecategories'


class Htbltemplates(models.Model):
    templateid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    categoryid = models.ForeignKey(Htbltemplatecategories, models.DO_NOTHING, db_column='categoryid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htbltemplates'


class Htbltemplateslang(models.Model):
    templateid = models.OneToOneField(Htbltemplates, models.DO_NOTHING, db_column='templateid', primary_key=True)
    language = models.IntegerField()
    name = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htbltemplatesLang'
        unique_together = (('templateid', 'language'),)


class Htblticket(models.Model):
    ticketid = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=500)
    replysubject = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateTimeField()
    priority = models.ForeignKey(Htblpriorities, models.DO_NOTHING, db_column='priority', blank=True, null=True)
    ticketstateid = models.ForeignKey('Htblticketstates', models.DO_NOTHING, db_column='ticketstateid', blank=True, null=True)
    fromuserid = models.ForeignKey('Htblusers', models.DO_NOTHING, db_column='fromuserid', blank=True, null=True)
    agentid = models.ForeignKey(Htblagents, models.DO_NOTHING, db_column='agentid', blank=True, null=True)
    tickettypeid = models.IntegerField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    sourceid = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField()
    flagged = models.BooleanField(blank=True, null=True)
    accountid = models.IntegerField(blank=True, null=True)
    replyaddress = models.CharField(max_length=256, blank=True, null=True)
    servicechange = models.BooleanField(blank=True, null=True)
    websitechange = models.BooleanField(blank=True, null=True)
    extradata = models.CharField(max_length=250, blank=True, null=True)
    clientconcerning = models.IntegerField(blank=True, null=True)
    spam = models.BooleanField(blank=True, null=True)
    assetid = models.IntegerField(blank=True, null=True)
    agentinitiated = models.BooleanField(blank=True, null=True)
    alias = models.CharField(max_length=256, blank=True, null=True)
    slaname = models.CharField(max_length=75, blank=True, null=True)
    slainitial = models.DateTimeField(blank=True, null=True)
    slaresolved = models.DateTimeField(blank=True, null=True)
    resolvecalc = models.BooleanField(blank=True, null=True)
    slabusiness = models.BooleanField(blank=True, null=True)
    flaggeddate = models.DateTimeField(blank=True, null=True)
    autoclose = models.IntegerField(blank=True, null=True)
    duplicateid = models.IntegerField(blank=True, null=True)
    ispersonal = models.BooleanField()
    histid = models.IntegerField(blank=True, null=True)
    userid_lastnote = models.IntegerField(blank=True, null=True)
    ipaddress = models.CharField(max_length=100, blank=True, null=True)
    lastuserreply = models.DateTimeField(blank=True, null=True)
    aliasemail = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblticket'


class Htblticketasset(models.Model):
    ticketid = models.OneToOneField(Htblticket, models.DO_NOTHING, db_column='ticketid', primary_key=True)
    assetid = models.ForeignKey('Tblassets', models.DO_NOTHING, db_column='assetid')

    class Meta:
        managed = False
        db_table = 'htblticketasset'
        unique_together = (('ticketid', 'assetid'),)


class Htblticketcustomfield(models.Model):
    ticketid = models.ForeignKey(Htblticket, models.DO_NOTHING, db_column='ticketid')
    fieldid = models.ForeignKey(Htblcustomfields, models.DO_NOTHING, db_column='fieldid')
    data = models.CharField(max_length=4000, blank=True, null=True)
    ticketcustomfieldid = models.AutoField(primary_key=True)
    tickettypefieldid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblticketcustomfield'


class Htblticketmerges(models.Model):
    mergeid = models.AutoField(primary_key=True)
    oldtid = models.IntegerField()
    newtid = models.ForeignKey(Htblticket, models.DO_NOTHING, db_column='newtid')
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblticketmerges'


class Htblticketsfilter(models.Model):
    filterid = models.AutoField(primary_key=True)
    tablefilter = models.CharField(max_length=50)
    field = models.CharField(max_length=100, blank=True, null=True)
    filtervalue = models.CharField(max_length=4000)
    operator = models.CharField(max_length=3, blank=True, null=True)
    comparator = models.IntegerField()
    grouped = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'htblticketsfilter'


class Htblticketssummary(models.Model):
    summaryid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('Htblusers', models.DO_NOTHING, db_column='userid')
    customtime = models.BooleanField()
    standardtime = models.IntegerField()
    time1 = models.DateTimeField()
    time2 = models.DateTimeField()
    endtoday = models.BooleanField()
    tickettypes = models.CharField(max_length=150, blank=True, null=True)
    teams = models.CharField(max_length=150, blank=True, null=True)
    agents = models.CharField(max_length=150, blank=True, null=True)
    s1 = models.CharField(max_length=50, blank=True, null=True)
    s2 = models.CharField(max_length=50, blank=True, null=True)
    s3 = models.CharField(max_length=50, blank=True, null=True)
    sort = models.IntegerField()
    order = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'htblticketssummary'


class Htblticketssummaryfilter(models.Model):
    summaryid = models.IntegerField(primary_key=True)
    filterid = models.IntegerField()
    filterorder = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'htblticketssummaryfilter'


class Htblticketstates(models.Model):
    ticketstateid = models.IntegerField(primary_key=True)
    statename = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    default = models.BooleanField(blank=True, null=True)
    trackaswork = models.BooleanField(blank=True, null=True)
    sortorder = models.IntegerField(blank=True, null=True)
    clientreplies = models.BooleanField(blank=True, null=True)
    taskstate = models.BooleanField(blank=True, null=True)
    replacementid = models.ForeignKey('self', models.DO_NOTHING, db_column='replacementid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblticketstates'


class Htblticketstateslang(models.Model):
    ticketstateid = models.OneToOneField(Htblticketstates, models.DO_NOTHING, db_column='ticketstateid', primary_key=True)
    language = models.IntegerField()
    statename = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblticketstatesLang'
        unique_together = (('ticketstateid', 'language'),)


class Htblticketsubscribers(models.Model):
    subscriberid = models.AutoField(primary_key=True)
    ticketid = models.ForeignKey(Htblticket, models.DO_NOTHING, db_column='ticketid', blank=True, null=True)
    agentid = models.ForeignKey(Htblagents, models.DO_NOTHING, db_column='agentid')
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblticketsubscribers'


class Htblticketteam(models.Model):
    ticketid = models.OneToOneField(Htblticket, models.DO_NOTHING, db_column='ticketid', primary_key=True)
    teamid = models.ForeignKey(Htblteams, models.DO_NOTHING, db_column='teamid')

    class Meta:
        managed = False
        db_table = 'htblticketteam'
        unique_together = (('ticketid', 'teamid'),)


class Htbltickettypecustomfield(models.Model):
    tickettypeid = models.ForeignKey('Htbltickettypes', models.DO_NOTHING, db_column='tickettypeid')
    fieldid = models.ForeignKey(Htblcustomfields, models.DO_NOTHING, db_column='fieldid')
    orderindex = models.SmallIntegerField(blank=True, null=True)
    agentonly = models.BooleanField(blank=True, null=True)
    requiredonclosing = models.BooleanField()
    requiredoncreation = models.BooleanField()
    tickettypecustomfieldid = models.AutoField(primary_key=True)
    collapsed = models.BooleanField()
    linked = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'htbltickettypecustomfield'


class Htbltickettypes(models.Model):
    tickettypeid = models.IntegerField(primary_key=True)
    typename = models.CharField(max_length=50, blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True)
    agentid = models.ForeignKey(Htblagents, models.DO_NOTHING, db_column='agentid', blank=True, null=True)
    enabled = models.BooleanField(blank=True, null=True)
    notetype = models.IntegerField(blank=True, null=True)
    replacementid = models.ForeignKey('self', models.DO_NOTHING, db_column='replacementid', blank=True, null=True)
    ignoredefaultstate = models.BooleanField()
    initialdescription = models.IntegerField(blank=True, null=True)
    extraticketoptions = models.IntegerField(blank=True, null=True)
    timeworked = models.BooleanField(blank=True, null=True)
    initialpriority = models.BooleanField()
    addccusers = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htbltickettypes'


class Htbltickettypeslang(models.Model):
    tickettypeid = models.OneToOneField(Htbltickettypes, models.DO_NOTHING, db_column='tickettypeid', primary_key=True)
    language = models.IntegerField()
    typename = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htbltickettypesLang'
        unique_together = (('tickettypeid', 'language'),)


class Htbltickettypeteams(models.Model):
    teamid = models.OneToOneField(Htblteams, models.DO_NOTHING, db_column='teamid', primary_key=True)
    tickettypeid = models.ForeignKey(Htbltickettypes, models.DO_NOTHING, db_column='tickettypeid')

    class Meta:
        managed = False
        db_table = 'htbltickettypeteams'
        unique_together = (('teamid', 'tickettypeid'),)


class Htblticketuserrelation(models.Model):
    ticketuserrelationid = models.AutoField(primary_key=True)
    ticketid = models.ForeignKey(Htblticket, models.DO_NOTHING, db_column='ticketid')
    userid = models.ForeignKey('Htblusers', models.DO_NOTHING, db_column='userid')
    type = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'htblticketuserrelation'


class Htblusers(models.Model):
    userid = models.AutoField(primary_key=True)
    email = models.CharField(max_length=256, blank=True, null=True)
    img = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    upn = models.CharField(max_length=300, blank=True, null=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    userdomain = models.CharField(max_length=150, blank=True, null=True)
    metrocolor = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    telephone = models.CharField(max_length=500, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=500, blank=True, null=True)
    ticketssort = models.IntegerField(blank=True, null=True)
    info = models.CharField(max_length=500, blank=True, null=True)
    roleid = models.IntegerField(db_column='Roleid', blank=True, null=True)  # Field name made lowercase.
    firstdayofweek = models.SmallIntegerField(blank=True, null=True)
    namelock = models.BooleanField(db_column='nameLock')  # Field name made lowercase.
    descriptionlock = models.BooleanField(db_column='descriptionLock')  # Field name made lowercase.
    addresslock = models.BooleanField(db_column='addressLock')  # Field name made lowercase.
    telephonelock = models.BooleanField(db_column='telephoneLock')  # Field name made lowercase.
    mobilelock = models.BooleanField(db_column='mobileLock')  # Field name made lowercase.
    faxlock = models.BooleanField(db_column='faxLock')  # Field name made lowercase.
    companylock = models.BooleanField(db_column='companyLock')  # Field name made lowercase.
    departmentlock = models.BooleanField(db_column='departmentLock')  # Field name made lowercase.
    emaillock = models.BooleanField(db_column='emailLock')  # Field name made lowercase.
    language = models.IntegerField()
    calendarview = models.IntegerField(blank=True, null=True)
    nomailasuser = models.BooleanField(db_column='NoMailAsUser')  # Field name made lowercase.
    added = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblusers'


class Htblwebroles(models.Model):
    webroleid = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=4000, blank=True, null=True)
    authmembers = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htblwebroles'


class Htblzones(models.Model):
    zoneid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    timezone = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    day1 = models.BooleanField()
    day2 = models.BooleanField()
    day3 = models.BooleanField()
    day4 = models.BooleanField()
    day5 = models.BooleanField()
    day6 = models.BooleanField()
    day7 = models.BooleanField()
    day1time1 = models.DateTimeField()
    day1time2 = models.DateTimeField()
    day2time1 = models.DateTimeField()
    day2time2 = models.DateTimeField()
    day3time1 = models.DateTimeField()
    day3time2 = models.DateTimeField()
    day4time1 = models.DateTimeField()
    day4time2 = models.DateTimeField()
    day5time1 = models.DateTimeField()
    day5time2 = models.DateTimeField()
    day6time1 = models.DateTimeField()
    day6time2 = models.DateTimeField()
    day7time1 = models.DateTimeField()
    day7time2 = models.DateTimeField()
    dateformat = models.CharField(max_length=20)
    default = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'htblzones'


class Tbladcomputers(models.Model):
    adcomputerid = models.AutoField(db_column='AdcomputerID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey('Tblassets', models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=800, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=500, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ou = models.CharField(db_column='OU', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    adobjectid = models.ForeignKey('Tbladobjects', models.DO_NOTHING, db_column='ADObjectID', blank=True, null=True)  # Field name made lowercase.
    manageradobjectid = models.ForeignKey('Tbladobjects', models.DO_NOTHING, db_column='ManagerADObjectId', blank=True, null=True)  # Field name made lowercase.
    isenabled = models.BooleanField(db_column='IsEnabled')  # Field name made lowercase.
    objectguid = models.CharField(db_column='ObjectGUID', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblADComputers'


class Tbladgroups(models.Model):
    adgroupid = models.AutoField(db_column='ADGroupID', primary_key=True)  # Field name made lowercase.
    adobjectid = models.ForeignKey('Tbladobjects', models.DO_NOTHING, db_column='ADObjectID')  # Field name made lowercase.
    manageradobjectid = models.ForeignKey('Tbladobjects', models.DO_NOTHING, db_column='ManagerADObjectId', blank=True, null=True)  # Field name made lowercase.
    grouptype = models.IntegerField(db_column='GroupType', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblADGroups'


class Tbladmembership(models.Model):
    childadobjectid = models.ForeignKey('Tbladobjects', models.DO_NOTHING, db_column='ChildAdObjectID')  # Field name made lowercase.
    parentadobjectid = models.ForeignKey('Tbladobjects', models.DO_NOTHING, db_column='ParentAdObjectID')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='lastChanged')  # Field name made lowercase.
    admembershipid = models.AutoField(db_column='ADMembershipId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblADMembership'
        unique_together = (('childadobjectid', 'parentadobjectid'),)


class Tbladobjects(models.Model):
    adobjectid = models.AutoField(db_column='ADObjectID', primary_key=True)  # Field name made lowercase.
    samaccountname = models.CharField(db_column='sAMAccountName', max_length=150)  # Field name made lowercase.
    domain = models.CharField(max_length=150)
    lastscanned = models.DateTimeField(db_column='LastScanned')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblADObjects'
        unique_together = (('domain', 'samaccountname'),)


class Tbladusers(models.Model):
    username = models.CharField(db_column='Username', max_length=150)  # Field name made lowercase.
    userdomain = models.CharField(db_column='Userdomain', max_length=150)  # Field name made lowercase.
    firstname = models.CharField(db_column='Firstname', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=500, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=500, blank=True, null=True)  # Field name made lowercase.
    displayname = models.CharField(db_column='Displayname', max_length=500, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    office = models.CharField(db_column='Office', max_length=500, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=500, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=500, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=500, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=300, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=300, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=300, blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='Countrycode', max_length=300, blank=True, null=True)  # Field name made lowercase.
    upn = models.CharField(db_column='UPN', max_length=300, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=500, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=500, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=500, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=300, blank=True, null=True)
    ou = models.CharField(db_column='OU', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    picture = models.BinaryField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    adobjectid = models.ForeignKey(Tbladobjects, models.DO_NOTHING, db_column='ADObjectID', blank=True, null=True)  # Field name made lowercase.
    manageradobjectid = models.ForeignKey(Tbladobjects, models.DO_NOTHING, db_column='ManagerADObjectId', blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pager = models.CharField(db_column='Pager', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ipphone = models.CharField(db_column='IpPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=300, blank=True, null=True)  # Field name made lowercase.
    homepage = models.CharField(db_column='HomePage', max_length=300, blank=True, null=True)  # Field name made lowercase.
    homedirectory = models.CharField(db_column='HomeDirectory', max_length=500, blank=True, null=True)  # Field name made lowercase.
    profilepath = models.CharField(db_column='ProfilePath', max_length=500, blank=True, null=True)  # Field name made lowercase.
    logonscript = models.CharField(db_column='LogonScript', max_length=500, blank=True, null=True)  # Field name made lowercase.
    whencreated = models.DateTimeField(db_column='whenCreated', blank=True, null=True)  # Field name made lowercase.
    whenchanged = models.DateTimeField(db_column='whenChanged', blank=True, null=True)  # Field name made lowercase.
    employeeid = models.CharField(db_column='EmployeeID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    employeenumber = models.CharField(db_column='EmployeeNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    employeetype = models.CharField(db_column='EmployeeType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    info = models.CharField(db_column='Info', max_length=500, blank=True, null=True)  # Field name made lowercase.
    division = models.CharField(db_column='Division', max_length=500, blank=True, null=True)  # Field name made lowercase.
    aduserid = models.AutoField(db_column='ADUserID', primary_key=True)  # Field name made lowercase.
    isenabled = models.BooleanField(db_column='IsEnabled')  # Field name made lowercase.
    expirationdate = models.DateTimeField(db_column='ExpirationDate', blank=True, null=True)  # Field name made lowercase.
    lockoutdate = models.DateTimeField(db_column='LockoutDate', blank=True, null=True)  # Field name made lowercase.
    passwordneverexpires = models.BooleanField(db_column='PasswordNeverExpires', blank=True, null=True)  # Field name made lowercase.
    passwordlastset = models.DateTimeField(db_column='PasswordLastSet', blank=True, null=True)  # Field name made lowercase.
    usercannotchangepassword = models.BooleanField(db_column='UserCannotChangePassword', blank=True, null=True)  # Field name made lowercase.
    passwordrequired = models.BooleanField(db_column='PasswordRequired', blank=True, null=True)  # Field name made lowercase.
    passwordexpirationdate = models.DateTimeField(db_column='PasswordExpirationDate', blank=True, null=True)  # Field name made lowercase.
    passwordchangeabledate = models.DateTimeField(db_column='PasswordChangeableDate', blank=True, null=True)  # Field name made lowercase.
    initials = models.CharField(db_column='Initials', max_length=50, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    postofficebox = models.CharField(db_column='PostOfficeBox', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastlogon = models.DateTimeField(db_column='LastLogon', blank=True, null=True)  # Field name made lowercase.
    objectsid = models.CharField(db_column='ObjectSid', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblADusers'
        unique_together = (('username', 'userdomain'),)


class Tblawsami(models.Model):
    awsamiid = models.AutoField(db_column='AWSAmiId', primary_key=True)  # Field name made lowercase.
    imageid = models.CharField(db_column='ImageId', max_length=50)  # Field name made lowercase.
    architecture = models.CharField(db_column='Architecture', max_length=50, blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enasupport = models.BooleanField(db_column='EnaSupport', blank=True, null=True)  # Field name made lowercase.
    imagelocation = models.CharField(db_column='ImageLocation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imageowneralias = models.CharField(db_column='ImageOwnerAlias', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imagetype = models.CharField(db_column='ImageType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ownerid = models.CharField(db_column='OwnerId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    public = models.BooleanField(db_column='Public', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    statereason = models.CharField(db_column='StateReason', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rootdevicename = models.CharField(db_column='Rootdevicename', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rootdevicetype = models.CharField(db_column='Rootdevicetype', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sriovnetsupport = models.CharField(db_column='SriovNetSupport', max_length=50, blank=True, null=True)  # Field name made lowercase.
    virtualizationtype = models.CharField(db_column='VirtualizationType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    platform = models.CharField(db_column='Platform', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hypervisor = models.CharField(db_column='Hypervisor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAWSAmi'


class Tblawscontainer(models.Model):
    awscontainerid = models.AutoField(db_column='AWSContainerId', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey('Tblassets', models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50)  # Field name made lowercase.
    instancetenancy = models.CharField(db_column='InstanceTenancy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='IsDefault', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vpcid = models.CharField(db_column='VpcId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=50)  # Field name made lowercase.
    regioncode = models.CharField(db_column='RegionCode', max_length=50)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAWSContainer'


class Tblawselasticgpu(models.Model):
    awselasticgpuid = models.AutoField(db_column='AWSElasticGpuId', primary_key=True)  # Field name made lowercase.
    awsinstanceid = models.ForeignKey('Tblawsinstance', models.DO_NOTHING, db_column='AWSInstanceId')  # Field name made lowercase.
    elasticgpuid = models.CharField(db_column='ElasticGpuId', max_length=50)  # Field name made lowercase.
    health = models.CharField(db_column='Health', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    availabilityzone = models.CharField(db_column='AvailabilityZone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAWSElasticGpu'


class Tblawshost(models.Model):
    awshostid = models.AutoField(db_column='AWSHostId', primary_key=True)  # Field name made lowercase.
    hostid = models.CharField(db_column='HostId', max_length=50)  # Field name made lowercase.
    autoplacement = models.BooleanField(db_column='AutoPlacement', blank=True, null=True)  # Field name made lowercase.
    availabilityzone = models.CharField(db_column='AvailabilityZone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    availablevcpus = models.IntegerField(db_column='AvailableVCpus', blank=True, null=True)  # Field name made lowercase.
    cores = models.IntegerField(db_column='Cores', blank=True, null=True)  # Field name made lowercase.
    instancetype = models.CharField(db_column='InstanceType', max_length=25, blank=True, null=True)  # Field name made lowercase.
    sockets = models.IntegerField(db_column='Sockets', blank=True, null=True)  # Field name made lowercase.
    totalvcpus = models.IntegerField(db_column='TotalVCpus', blank=True, null=True)  # Field name made lowercase.
    releasetime = models.DateTimeField(db_column='ReleaseTime', blank=True, null=True)  # Field name made lowercase.
    availablecapacity = models.IntegerField(db_column='AvailableCapacity', blank=True, null=True)  # Field name made lowercase.
    totalcapacity = models.IntegerField(db_column='TotalCapacity', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAWSHost'


class Tblawsinstance(models.Model):
    awsinstanceid = models.AutoField(db_column='AWSInstanceId', primary_key=True)  # Field name made lowercase.
    awscontainerid = models.ForeignKey(Tblawscontainer, models.DO_NOTHING, db_column='AWSContainerId')  # Field name made lowercase.
    awssubnetid = models.ForeignKey('Tblawssubnet', models.DO_NOTHING, db_column='AWSSubnetId', blank=True, null=True)  # Field name made lowercase.
    awshostid = models.ForeignKey(Tblawshost, models.DO_NOTHING, db_column='AWSHostId', blank=True, null=True)  # Field name made lowercase.
    awsamiid = models.ForeignKey(Tblawsami, models.DO_NOTHING, db_column='AWSAmiId', blank=True, null=True)  # Field name made lowercase.
    assetid = models.ForeignKey('Tblassets', models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    architecture = models.CharField(db_column='Architecture', max_length=50, blank=True, null=True)  # Field name made lowercase.
    environment = models.CharField(db_column='Environment', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hypervisor = models.CharField(db_column='Hypervisor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    instanceid = models.CharField(db_column='InstanceId', max_length=50)  # Field name made lowercase.
    instancetype = models.CharField(db_column='InstanceType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    instanceprofilearn = models.CharField(db_column='InstanceProfileARN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    instanceprofileid = models.CharField(db_column='InstanceProfileId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imageid = models.CharField(db_column='ImageId', max_length=50)  # Field name made lowercase.
    kernel = models.CharField(db_column='Kernel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keypairname = models.CharField(db_column='KeyPairName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publicdnsname = models.CharField(db_column='PublicDNSName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publicipaddress = models.CharField(db_column='PublicIPAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rootdevicename = models.CharField(db_column='RootDeviceName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rootdevicetype = models.CharField(db_column='RootDeviceType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    platform = models.CharField(db_column='Platform', max_length=50)  # Field name made lowercase.
    virtualizationtype = models.CharField(db_column='VirtualizationType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cpucredits = models.CharField(db_column='CpuCredits', max_length=50, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=50)  # Field name made lowercase.
    regioncode = models.CharField(db_column='RegionCode', max_length=50)  # Field name made lowercase.
    availabilityzone = models.CharField(db_column='AvailabilityZone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lifecycle = models.CharField(db_column='LifeCycle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    corecount = models.IntegerField(db_column='CoreCount', blank=True, null=True)  # Field name made lowercase.
    threadspercore = models.IntegerField(db_column='ThreadsPerCore', blank=True, null=True)  # Field name made lowercase.
    statereason = models.CharField(db_column='StateReason', max_length=500, blank=True, null=True)  # Field name made lowercase.
    enasupport = models.BooleanField(db_column='EnaSupport', blank=True, null=True)  # Field name made lowercase.
    launchtime = models.DateTimeField(db_column='LaunchTime', blank=True, null=True)  # Field name made lowercase.
    privatednsname = models.CharField(db_column='PrivateDNSName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    privateipaddress = models.CharField(db_column='PrivateIPAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ramdiskid = models.CharField(db_column='RamdiskId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sourcedestcheck = models.BooleanField(db_column='SourceDestCheck', blank=True, null=True)  # Field name made lowercase.
    sriovnetsupport = models.CharField(db_column='SriovNetSupport', max_length=50, blank=True, null=True)  # Field name made lowercase.
    statetransitionreason = models.CharField(db_column='StateTransitionReason', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAWSInstance'


class Tblawsinstancesecuritygroup(models.Model):
    awsinstancesecuritygroupid = models.AutoField(db_column='AWSInstanceSecurityGroupId', primary_key=True)  # Field name made lowercase.
    awsinstanceid = models.ForeignKey(Tblawsinstance, models.DO_NOTHING, db_column='AWSInstanceId')  # Field name made lowercase.
    awssecuritygroupid = models.ForeignKey('Tblawssecuritygroup', models.DO_NOTHING, db_column='AWSSecurityGroupId')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAWSInstanceSecurityGroup'


class Tblawsipaddress(models.Model):
    awsipaddressid = models.AutoField(db_column='AWSIpAddressId', primary_key=True)  # Field name made lowercase.
    awsnetworkinterfaceid = models.ForeignKey('Tblawsnetworkinterface', models.DO_NOTHING, db_column='AWSNetworkInterfaceId')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IpAddress', max_length=50)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAWSIpAddress'


class Tblawsnetworkinterface(models.Model):
    awsnetworkinterfaceid = models.AutoField(db_column='AWSNetworkInterfaceId', primary_key=True)  # Field name made lowercase.
    awsinstanceid = models.ForeignKey(Tblawsinstance, models.DO_NOTHING, db_column='AWSInstanceId')  # Field name made lowercase.
    networkinterfaceid = models.CharField(db_column='NetworkInterfaceId', max_length=50)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    privatednsname = models.CharField(db_column='PrivateDNSName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    privateipaddress = models.CharField(db_column='PrivateIPAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ownerid = models.CharField(db_column='OwnerId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subnetid = models.CharField(db_column='SubnetId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sourcedestcheck = models.BooleanField(db_column='SourceDestCheck', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    attachtime = models.DateTimeField(db_column='AttachTime', blank=True, null=True)  # Field name made lowercase.
    deleteontermination = models.BooleanField(db_column='DeleteOnTermination', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    interfacetype = models.CharField(db_column='InterfaceType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    requesterid = models.CharField(db_column='RequesterId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    requestermanaged = models.BooleanField(db_column='RequesterManaged', blank=True, null=True)  # Field name made lowercase.
    availabilityzone = models.CharField(db_column='AvailabilityZone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAWSNetworkInterface'


class Tblawsproductcode(models.Model):
    awsproductcodeid = models.AutoField(db_column='AWSProductCodeId', primary_key=True)  # Field name made lowercase.
    awsinstanceid = models.ForeignKey(Tblawsinstance, models.DO_NOTHING, db_column='AWSInstanceId')  # Field name made lowercase.
    productcodeid = models.CharField(db_column='ProductCodeId', max_length=50)  # Field name made lowercase.
    productcodetype = models.CharField(db_column='ProductCodeType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAWSProductCode'


class Tblawssecuritygroup(models.Model):
    awssecuritygroupid = models.AutoField(db_column='AWSSecurityGroupId', primary_key=True)  # Field name made lowercase.
    awscontainerid = models.ForeignKey(Tblawscontainer, models.DO_NOTHING, db_column='AWSContainerId', blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='GroupId', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ownerid = models.CharField(db_column='OwnerId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAWSSecurityGroup'


class Tblawssecuritygrouppermission(models.Model):
    awssecuritygrouppermissionid = models.AutoField(db_column='AWSSecurityGroupPermissionId', primary_key=True)  # Field name made lowercase.
    awssecuritygroupid = models.ForeignKey(Tblawssecuritygroup, models.DO_NOTHING, db_column='AWSSecurityGroupId')  # Field name made lowercase.
    fromport = models.IntegerField(db_column='FromPort', blank=True, null=True)  # Field name made lowercase.
    toport = models.IntegerField(db_column='ToPort', blank=True, null=True)  # Field name made lowercase.
    ipprotocol = models.CharField(db_column='IpProtocol', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isinbound = models.BooleanField(db_column='IsInbound', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAWSSecurityGroupPermission'


class Tblawssecuritygrouppermissioniprange(models.Model):
    awssecuritygrouppermissioniprangeid = models.AutoField(db_column='AWSSecurityGroupPermissionIpRangeId', primary_key=True)  # Field name made lowercase.
    awssecuritygrouppermissionid = models.ForeignKey(Tblawssecuritygrouppermission, models.DO_NOTHING, db_column='AWSSecurityGroupPermissionId')  # Field name made lowercase.
    cidrip = models.CharField(db_column='CidrIp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAWSSecurityGroupPermissionIpRange'


class Tblawssubnet(models.Model):
    awssubnetid = models.AutoField(db_column='AWSSubnetId', primary_key=True)  # Field name made lowercase.
    awscontainerid = models.ForeignKey(Tblawscontainer, models.DO_NOTHING, db_column='AWSContainerId')  # Field name made lowercase.
    subnetid = models.CharField(db_column='SubnetId', max_length=50)  # Field name made lowercase.
    vpcid = models.CharField(db_column='VPCId', max_length=50)  # Field name made lowercase.
    availabilityzone = models.CharField(db_column='AvailabilityZone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    availableipaddresscount = models.IntegerField(db_column='AvailableIpAddressCount', blank=True, null=True)  # Field name made lowercase.
    cidrblock = models.CharField(db_column='CidrBlock', max_length=50, blank=True, null=True)  # Field name made lowercase.
    defaultforaz = models.BooleanField(db_column='DefaultForAz', blank=True, null=True)  # Field name made lowercase.
    mappubliciponlaunch = models.BooleanField(db_column='MapPublicIpOnLaunch', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAWSSubnet'


class Tblawssubnetipv6Cidrblock(models.Model):
    awssubnetipv6cidrblockid = models.AutoField(db_column='AWSSubnetIpv6CidrBlockId', primary_key=True)  # Field name made lowercase.
    awssubnetid = models.ForeignKey(Tblawssubnet, models.DO_NOTHING, db_column='AWSSubnetId')  # Field name made lowercase.
    ipv6cidrblock = models.CharField(db_column='Ipv6CidrBlock', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAWSSubnetIpv6CidrBlock'


class Tblawstag(models.Model):
    awstagid = models.AutoField(db_column='AWSTagId', primary_key=True)  # Field name made lowercase.
    awsinstanceid = models.ForeignKey(Tblawsinstance, models.DO_NOTHING, db_column='AWSInstanceId')  # Field name made lowercase.
    key = models.CharField(db_column='Key', max_length=127)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAWSTag'


class Tblawsvolume(models.Model):
    awsvolumeid = models.AutoField(db_column='AWSVolumeId', primary_key=True)  # Field name made lowercase.
    awsinstanceid = models.ForeignKey(Tblawsinstance, models.DO_NOTHING, db_column='AWSInstanceId')  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    encrypted = models.BooleanField(db_column='Encrypted', blank=True, null=True)  # Field name made lowercase.
    size = models.IntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    volumeid = models.CharField(db_column='VolumeId', max_length=50)  # Field name made lowercase.
    volumetype = models.CharField(db_column='VolumeType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    snapshotid = models.CharField(db_column='SnapShotId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deleteontermination = models.BooleanField(db_column='DeleteOnTermination', blank=True, null=True)  # Field name made lowercase.
    iops = models.IntegerField(db_column='Iops', blank=True, null=True)  # Field name made lowercase.
    availabilityzone = models.CharField(db_column='AvailabilityZone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kmskeyid = models.CharField(db_column='KmsKeyId', max_length=150, blank=True, null=True)  # Field name made lowercase.
    attachtime = models.DateTimeField(db_column='AttachTime', blank=True, null=True)  # Field name made lowercase.
    device = models.CharField(db_column='Device', max_length=50, blank=True, null=True)  # Field name made lowercase.
    attachmentstate = models.CharField(db_column='AttachmentState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAWSVolume'


class Tbladproperty(models.Model):
    adpropertyid = models.AutoField(db_column='AdPropertyId', primary_key=True)  # Field name made lowercase.
    typeid = models.ForeignKey('Tsysadpropertytype', models.DO_NOTHING, db_column='TypeId')  # Field name made lowercase.
    adobjectid = models.ForeignKey(Tbladobjects, models.DO_NOTHING, db_column='AdObjectId')  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=1024)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAdProperty'


class Tblairwatchapplication(models.Model):
    airwatchapplicationid = models.AutoField(db_column='AirWatchApplicationId', primary_key=True)  # Field name made lowercase.
    airwatchdeviceid = models.ForeignKey('Tblairwatchdevice', models.DO_NOTHING, db_column='AirWatchDeviceId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=200, blank=True, null=True)  # Field name made lowercase.
    buildversion = models.CharField(db_column='BuildVersion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=200, blank=True, null=True)  # Field name made lowercase.
    size = models.IntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    applicationidentifier = models.CharField(db_column='ApplicationIdentifier', max_length=200)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ismanaged = models.BooleanField(db_column='IsManaged', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAirWatchApplication'


class Tblairwatchdevice(models.Model):
    airwatchdeviceid = models.AutoField(db_column='AirWatchDeviceId', primary_key=True)  # Field name made lowercase.
    airwatchorganizationgroupid = models.ForeignKey('Tblairwatchorganizationgroup', models.DO_NOTHING, db_column='AirWatchOrganizationGroupId')  # Field name made lowercase.
    airwatchuserid = models.ForeignKey('Tblairwatchuser', models.DO_NOTHING, db_column='AirWatchUserId', blank=True, null=True)  # Field name made lowercase.
    assetid = models.ForeignKey('Tblassets', models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    deviceid = models.IntegerField(db_column='DeviceId')  # Field name made lowercase.
    udid = models.CharField(db_column='Udid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imei = models.CharField(db_column='Imei', max_length=200, blank=True, null=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    assetnumber = models.CharField(db_column='AssetNumber', max_length=200)  # Field name made lowercase.
    easid = models.CharField(db_column='EasId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    devicefriendlyname = models.CharField(db_column='DeviceFriendlyName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='Uuid', max_length=200)  # Field name made lowercase.
    locationgroupname = models.CharField(db_column='LocationGroupName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    useremailaddress = models.CharField(db_column='UserEmailAddress', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ownership = models.CharField(db_column='Ownership', max_length=200, blank=True, null=True)  # Field name made lowercase.
    platform = models.CharField(db_column='Platform', max_length=200, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=200, blank=True, null=True)  # Field name made lowercase.
    osversion = models.CharField(db_column='OsVersion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lastseen = models.DateTimeField(db_column='LastSeen', blank=True, null=True)  # Field name made lowercase.
    enrollmentstatus = models.CharField(db_column='EnrollmentStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    compliancestatus = models.CharField(db_column='ComplianceStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    compromisedstatus = models.BooleanField(db_column='CompromisedStatus', blank=True, null=True)  # Field name made lowercase.
    lastenrolledon = models.DateTimeField(db_column='LastEnrolledOn', blank=True, null=True)  # Field name made lowercase.
    lastcompliancecheckon = models.DateTimeField(db_column='LastComplianceCheckOn', blank=True, null=True)  # Field name made lowercase.
    lastcompromisedcheckon = models.DateTimeField(db_column='LastCompromisedCheckOn', blank=True, null=True)  # Field name made lowercase.
    issupervised = models.BooleanField(db_column='IsSupervised', blank=True, null=True)  # Field name made lowercase.
    simmcc = models.IntegerField(db_column='SimMcc', blank=True, null=True)  # Field name made lowercase.
    currentmcc = models.IntegerField(db_column='CurrentMcc', blank=True, null=True)  # Field name made lowercase.
    virtualmemory = models.IntegerField(db_column='VirtualMemory', blank=True, null=True)  # Field name made lowercase.
    isdevicedndenabled = models.BooleanField(db_column='IsDeviceDNDEnabled', blank=True, null=True)  # Field name made lowercase.
    isdevicelocatorenabled = models.BooleanField(db_column='IsDeviceLocatorEnabled', blank=True, null=True)  # Field name made lowercase.
    iscloudbackupenabled = models.BooleanField(db_column='IsCloudBackupEnabled', blank=True, null=True)  # Field name made lowercase.
    isactivationlockenabled = models.BooleanField(db_column='IsActivationLockEnabled', blank=True, null=True)  # Field name made lowercase.
    isnetworktethered = models.BooleanField(db_column='IsNetworkTethered', blank=True, null=True)  # Field name made lowercase.
    batterylevel = models.CharField(db_column='BatteryLevel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    isroaming = models.BooleanField(db_column='IsRoaming', blank=True, null=True)  # Field name made lowercase.
    systemintegrityprotectionenabled = models.BooleanField(db_column='SystemIntegrityProtectionEnabled', blank=True, null=True)  # Field name made lowercase.
    processorarchitecture = models.IntegerField(db_column='ProcessorArchitecture', blank=True, null=True)  # Field name made lowercase.
    totalphysicalmemory = models.IntegerField(db_column='TotalPhysicalMemory', blank=True, null=True)  # Field name made lowercase.
    availablephysicalmemory = models.IntegerField(db_column='AvailablePhysicalMemory', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAirWatchDevice'


class Tblairwatchorganizationgroup(models.Model):
    airwatchorganizationgroupid = models.AutoField(db_column='AirWatchOrganizationGroupId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=500)  # Field name made lowercase.
    organizationgroupid = models.IntegerField(db_column='OrganizationGroupId')  # Field name made lowercase.
    locationgrouptype = models.CharField(db_column='LocationGroupType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=200, blank=True, null=True)  # Field name made lowercase.
    locale = models.CharField(db_column='Locale', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdon = models.CharField(db_column='CreatedOn', max_length=50, blank=True, null=True)  # Field name made lowercase.
    users = models.IntegerField(db_column='Users', blank=True, null=True)  # Field name made lowercase.
    admins = models.IntegerField(db_column='Admins', blank=True, null=True)  # Field name made lowercase.
    devices = models.IntegerField(db_column='Devices', blank=True, null=True)  # Field name made lowercase.
    lglevel = models.IntegerField(db_column='LgLevel')  # Field name made lowercase.
    uuid = models.CharField(db_column='Uuid', max_length=200)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAirWatchOrganizationGroup'


class Tblairwatchuser(models.Model):
    airwatchuserid = models.AutoField(db_column='AirWatchUserId', primary_key=True)  # Field name made lowercase.
    airwatchorganizationgroupid = models.ForeignKey(Tblairwatchorganizationgroup, models.DO_NOTHING, db_column='AirWatchOrganizationGroupId')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    status = models.BooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=200, blank=True, null=True)  # Field name made lowercase.
    securitytype = models.CharField(db_column='SecurityType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mobilenumber = models.CharField(db_column='MobileNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    emailusername = models.CharField(db_column='EmailUserName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=200, blank=True, null=True)  # Field name made lowercase.
    customattribute1 = models.CharField(db_column='CustomAttribute1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    customattribute2 = models.CharField(db_column='CustomAttribute2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    customattribute3 = models.CharField(db_column='CustomAttribute3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    customattribute4 = models.CharField(db_column='CustomAttribute4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    customattribute5 = models.CharField(db_column='CustomAttribute5', max_length=200, blank=True, null=True)  # Field name made lowercase.
    externalid = models.CharField(db_column='ExternalId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    stagingmode = models.IntegerField(db_column='StagingMode', blank=True, null=True)  # Field name made lowercase.
    devicestagingenabled = models.BooleanField(db_column='DeviceStagingEnabled', blank=True, null=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='Uuid', max_length=200, blank=True, null=True)  # Field name made lowercase.
    messagetype = models.IntegerField(db_column='MessageType', blank=True, null=True)  # Field name made lowercase.
    enrolleddevicescount = models.IntegerField(db_column='EnrolledDevicesCount', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAirWatchUser'


class Tblantivirus(models.Model):
    antivirusid = models.AutoField(db_column='AntivirusId', primary_key=True)  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    assetid = models.ForeignKey('Tblassets', models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    productstate = models.IntegerField(db_column='ProductState', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    onaccessscanningenabled = models.BooleanField(db_column='onAccessScanningEnabled', blank=True, null=True)  # Field name made lowercase.
    productuptodate = models.BooleanField(db_column='productUpToDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAntivirus'


class Tblassetchangelog(models.Model):
    assetchangelogid = models.AutoField(db_column='AssetChangeLogId', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey('Tblassets', models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    fieldid = models.ForeignKey('Tsysassetfield', models.DO_NOTHING, db_column='FieldId')  # Field name made lowercase.
    changedby = models.ForeignKey('Tsysassetchangesource', models.DO_NOTHING, db_column='ChangedBy')  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAssetChangeLog'


class Tblassetcomments(models.Model):
    commentid = models.AutoField(db_column='CommentID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey('Tblassets', models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=4000)  # Field name made lowercase.
    addedby = models.CharField(db_column='AddedBy', max_length=150)  # Field name made lowercase.
    added = models.DateTimeField(db_column='Added')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAssetComments'


class Tblassetcustom(models.Model):
    custid = models.AutoField(db_column='CustID', primary_key=True)  # Field name made lowercase.
    assetid = models.OneToOneField('Tblassets', models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    state = models.ForeignKey('Tblstate', models.DO_NOTHING, db_column='State')  # Field name made lowercase.
    purchasedate = models.DateTimeField(db_column='PurchaseDate', blank=True, null=True)  # Field name made lowercase.
    warrantydate = models.DateTimeField(db_column='Warrantydate', blank=True, null=True)  # Field name made lowercase.
    lastpatched = models.DateTimeField(db_column='LastPatched', blank=True, null=True)  # Field name made lowercase.
    lastfullbackup = models.DateTimeField(db_column='LastFullbackup', blank=True, null=True)  # Field name made lowercase.
    lastfullimage = models.DateTimeField(db_column='LastFullimage', blank=True, null=True)  # Field name made lowercase.
    ordernumber = models.CharField(db_column='OrderNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=300, blank=True, null=True)  # Field name made lowercase.
    locationlock = models.BooleanField(db_column='LocationLock', blank=True, null=True)  # Field name made lowercase.
    building = models.CharField(db_column='Building', max_length=300, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=300, blank=True, null=True)  # Field name made lowercase.
    branchoffice = models.CharField(db_column='Branchoffice', max_length=50, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='BarCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=200, blank=True, null=True)  # Field name made lowercase.
    manufacturerlock = models.BooleanField(db_column='ManufacturerLock', blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=300, blank=True, null=True)  # Field name made lowercase.
    contactlock = models.BooleanField(db_column='ContactLock', blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=200, blank=True, null=True)  # Field name made lowercase.
    modellock = models.BooleanField(db_column='ModelLock', blank=True, null=True)  # Field name made lowercase.
    httptitle = models.CharField(db_column='HTTPTitle', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    httpserver = models.CharField(db_column='HttpServer', max_length=500, blank=True, null=True)  # Field name made lowercase.
    httpsserver = models.CharField(db_column='HttpsServer', max_length=500, blank=True, null=True)  # Field name made lowercase.
    snmpoid = models.CharField(db_column='SnmpOID', max_length=150, blank=True, null=True)  # Field name made lowercase.
    smtpheader = models.CharField(db_column='SMTPheader', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ftpheader = models.CharField(db_column='FTPheader', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    serialnumber = models.CharField(db_column='Serialnumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    serialnumberlock = models.BooleanField(db_column='SerialnumberLock', blank=True, null=True)  # Field name made lowercase.
    printedpages = models.DecimalField(db_column='Printedpages', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    printerstatus = models.CharField(db_column='Printerstatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    custom1 = models.CharField(db_column='Custom1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custom2 = models.CharField(db_column='Custom2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custom3 = models.CharField(db_column='Custom3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custom4 = models.CharField(db_column='Custom4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custom5 = models.CharField(db_column='Custom5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custom6 = models.CharField(db_column='Custom6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custom7 = models.CharField(db_column='Custom7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custom8 = models.CharField(db_column='Custom8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custom9 = models.CharField(db_column='Custom9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custom10 = models.CharField(db_column='Custom10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custom11 = models.CharField(db_column='Custom11', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custom12 = models.CharField(db_column='Custom12', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custom13 = models.CharField(db_column='Custom13', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custom14 = models.CharField(db_column='Custom14', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custom15 = models.CharField(db_column='Custom15', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custom16 = models.CharField(db_column='Custom16', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custom17 = models.CharField(db_column='Custom17', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custom18 = models.CharField(db_column='Custom18', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custom19 = models.CharField(db_column='Custom19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custom20 = models.CharField(db_column='Custom20', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dnsname = models.CharField(db_column='DNSName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sshserver = models.CharField(db_column='SSHServer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    purchasedatelock = models.BooleanField(db_column='PurchaseDateLock', blank=True, null=True)  # Field name made lowercase.
    warrantydatelock = models.BooleanField(db_column='WarrantyDateLock', blank=True, null=True)  # Field name made lowercase.
    systemsku = models.CharField(db_column='SystemSKU', max_length=200, blank=True, null=True)  # Field name made lowercase.
    preventcleanup = models.BooleanField(db_column='PreventCleanup', blank=True, null=True)  # Field name made lowercase.
    locksystemsku = models.BooleanField(db_column='LockSystemSKU', blank=True, null=True)  # Field name made lowercase.
    dmidecodeerror = models.BooleanField(db_column='DmidecodeError')  # Field name made lowercase.
    printedcolorpages = models.IntegerField(db_column='PrintedColorPages', blank=True, null=True)  # Field name made lowercase.
    printedmonopages = models.IntegerField(db_column='PrintedMonoPages', blank=True, null=True)  # Field name made lowercase.
    hardwareversion = models.CharField(db_column='HardwareVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    softwareversion = models.CharField(db_column='SoftwareVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    firmwareversion = models.CharField(db_column='FirmwareVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deviceversion = models.CharField(db_column='DeviceVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    couldscanntlogevent = models.BooleanField(db_column='CouldScanNtLogEvent', blank=True, null=True)  # Field name made lowercase.
    serialnumberscanned = models.CharField(db_column='SerialNumberScanned', max_length=100, blank=True, null=True)  # Field name made lowercase.
    extendeddisplayuniid = models.ForeignKey('Tblextendeddisplayuni', models.DO_NOTHING, db_column='ExtendedDisplayUniId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAssetCustom'


class Tblassetdocs(models.Model):
    docsid = models.AutoField(db_column='DocsID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey('Tblassets', models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    docname = models.CharField(db_column='Docname', max_length=255)  # Field name made lowercase.
    docguid = models.CharField(db_column='Docguid', max_length=100)  # Field name made lowercase.
    addedby = models.CharField(db_column='AddedBy', max_length=150)  # Field name made lowercase.
    added = models.DateTimeField(db_column='Added')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAssetDocs'


class Tblassetgrouplink(models.Model):
    assetgrouplinkid = models.BigAutoField(db_column='AssetGroupLinkID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey('Tblassets', models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    assetgroupid = models.ForeignKey('Tblassetgroups', models.DO_NOTHING, db_column='AssetGroupID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAssetGroupLink'
        unique_together = (('assetid', 'assetgroupid'),)


class Tblassetgroups(models.Model):
    assetgroupid = models.IntegerField(db_column='AssetGroupID', primary_key=True)  # Field name made lowercase.
    assetgroup = models.CharField(db_column='AssetGroup', unique=True, max_length=150)  # Field name made lowercase.
    builtin = models.BooleanField(db_column='Builtin')  # Field name made lowercase.
    dynamic = models.BooleanField(db_column='Dynamic', blank=True, null=True)  # Field name made lowercase.
    cloudstatusid = models.ForeignKey('Tsyscloudstatus', models.DO_NOTHING, db_column='CloudStatusId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAssetGroups'


class Tblassetjournal(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn')  # Field name made lowercase.
    action = models.IntegerField(db_column='Action')  # Field name made lowercase.
    entityid = models.CharField(db_column='EntityId', max_length=128, blank=True, null=True)  # Field name made lowercase.
    entitytable = models.CharField(db_column='EntityTable', max_length=128, blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=128)  # Field name made lowercase.
    object = models.TextField(db_column='Object', blank=True, null=True)  # Field name made lowercase.
    partitionkey = models.CharField(db_column='PartitionKey', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAssetJournal'


class Tblassetmacaddress(models.Model):
    macid = models.BigAutoField(db_column='MacID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey('Tblassets', models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    mac = models.CharField(db_column='Mac', max_length=20)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAssetMacAddress'


class Tblassetmergelinks(models.Model):
    assetmergelinkid = models.AutoField(db_column='AssetMergeLinkID', primary_key=True)  # Field name made lowercase.
    oldassetid = models.IntegerField(db_column='OldAssetID')  # Field name made lowercase.
    newassetid = models.IntegerField(db_column='NewAssetID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAssetMergeLinks'


class Tblassetradardevice(models.Model):
    deviceid = models.AutoField(db_column='DeviceId', primary_key=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    devicename = models.CharField(db_column='DeviceName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    domainname = models.CharField(db_column='DomainName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ipv4address = models.CharField(db_column='Ipv4Address', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ipv6address = models.CharField(db_column='Ipv6Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ipsubnet = models.CharField(db_column='IpSubnet', max_length=30, blank=True, null=True)  # Field name made lowercase.
    defaultgateway = models.CharField(db_column='DefaultGateway', max_length=50, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=200, blank=True, null=True)  # Field name made lowercase.
    discoveredby = models.CharField(db_column='DiscoveredBy', max_length=150, blank=True, null=True)  # Field name made lowercase.
    firstseen = models.DateTimeField(db_column='FirstSeen')  # Field name made lowercase.
    lastseen = models.DateTimeField(db_column='LastSeen')  # Field name made lowercase.
    packetsretrieved = models.BigIntegerField(db_column='PacketsRetrieved', blank=True, null=True)  # Field name made lowercase.
    protocols = models.IntegerField(db_column='Protocols')  # Field name made lowercase.
    pingttl = models.CharField(db_column='PingTtl', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rtt = models.CharField(db_column='Rtt', max_length=10, blank=True, null=True)  # Field name made lowercase.
    detectedduringfreshinstall = models.BooleanField(db_column='DetectedDuringFreshInstall')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAssetRadarDevice'


class Tblassetrelations(models.Model):
    relationid = models.AutoField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    parentassetid = models.ForeignKey('Tblassets', models.DO_NOTHING, db_column='ParentAssetID', blank=True, null=True)  # Field name made lowercase.
    childassetid = models.IntegerField(db_column='ChildAssetID', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    posx = models.IntegerField(db_column='posX', blank=True, null=True)  # Field name made lowercase.
    posy = models.IntegerField(db_column='posY', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAssetRelations'


class Tblassetuserrelations(models.Model):
    relationid = models.AutoField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=150, blank=True, null=True)  # Field name made lowercase.
    userdomain = models.CharField(db_column='Userdomain', max_length=150, blank=True, null=True)  # Field name made lowercase.
    assetid = models.ForeignKey('Tblassets', models.DO_NOTHING, db_column='AssetID', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    ou = models.CharField(db_column='Ou', max_length=500, blank=True, null=True)  # Field name made lowercase.
    adobjectid = models.IntegerField(db_column='AdObjectId', blank=True, null=True)  # Field name made lowercase.
    islocaluser = models.BooleanField(db_column='IsLocalUser')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.
    upn = models.CharField(db_column='Upn', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAssetUserRelations'


class Tblassets(models.Model):
    assetid = models.AutoField(db_column='AssetID', primary_key=True)  # Field name made lowercase.
    assetunique = models.CharField(db_column='AssetUnique', unique=True, max_length=150, blank=True, null=True)  # Field name made lowercase.
    domain = models.CharField(db_column='Domain', max_length=150, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=150, blank=True, null=True)  # Field name made lowercase.
    userdomain = models.CharField(db_column='Userdomain', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fqdn = models.CharField(db_column='FQDN', max_length=512, blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ipnumeric = models.DecimalField(db_column='IPNumeric', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    siteid = models.DecimalField(db_column='SiteID', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    scanserver = models.CharField(db_column='Scanserver', max_length=150, blank=True, null=True)  # Field name made lowercase.
    oscode = models.CharField(db_column='OScode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sp = models.DecimalField(db_column='SP', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    descriptionlock = models.BooleanField(db_column='Descriptionlock', blank=True, null=True)  # Field name made lowercase.
    assettype = models.ForeignKey('Tsysassettypes', models.DO_NOTHING, db_column='Assettype')  # Field name made lowercase.
    assettypelock = models.BooleanField(db_column='AssetTypeLock', blank=True, null=True)  # Field name made lowercase.
    assetname = models.CharField(db_column='AssetName', max_length=200)  # Field name made lowercase.
    assetnamelock = models.BooleanField(db_column='AssetNameLock', blank=True, null=True)  # Field name made lowercase.
    mac = models.CharField(db_column='Mac', max_length=20, blank=True, null=True)  # Field name made lowercase.
    firstseen = models.DateTimeField(db_column='Firstseen', blank=True, null=True)  # Field name made lowercase.
    lastseen = models.DateTimeField(db_column='Lastseen', blank=True, null=True)  # Field name made lowercase.
    lasttried = models.DateTimeField(db_column='Lasttried', blank=True, null=True)  # Field name made lowercase.
    lasttriggered = models.DateTimeField(db_column='Lasttriggered', blank=True, null=True)  # Field name made lowercase.
    lastscheduled = models.DateTimeField(db_column='LastScheduled', blank=True, null=True)  # Field name made lowercase.
    lastactivescan = models.DateTimeField(db_column='LastActiveScan', blank=True, null=True)  # Field name made lowercase.
    lastipscan = models.DateTimeField(db_column='LastIPScan', blank=True, null=True)  # Field name made lowercase.
    lastlspush = models.DateTimeField(db_column='LastLsPush', blank=True, null=True)  # Field name made lowercase.
    lastsaved = models.DateTimeField(db_column='LastSaved', blank=True, null=True)  # Field name made lowercase.
    uptime = models.DecimalField(db_column='Uptime', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    memory = models.DecimalField(db_column='Memory', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    nrprocessors = models.DecimalField(db_column='NrProcessors', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    processor = models.CharField(db_column='Processor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    serviceversion = models.CharField(db_column='ServiceVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lspushversion = models.CharField(db_column='LsPushVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastworkgroupscan = models.DateTimeField(db_column='lastWorkgroupScan', blank=True, null=True)  # Field name made lowercase.
    locationid = models.ForeignKey('Tsysiplocations', models.DO_NOTHING, db_column='LocationID')  # Field name made lowercase.
    manualmac = models.BooleanField(db_column='ManualMAC')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    lastlsfallback = models.DateTimeField(db_column='LastLsFallBack', blank=True, null=True)  # Field name made lowercase.
    buildnumber = models.CharField(db_column='BuildNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lsagentversion = models.CharField(db_column='LsAgentVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastlsagent = models.DateTimeField(db_column='LastLsAgent', blank=True, null=True)  # Field name made lowercase.
    hosttypeid = models.ForeignKey('Tsyshosttype', models.DO_NOTHING, db_column='HostTypeId', blank=True, null=True)  # Field name made lowercase.
    lastperformancescan = models.DateTimeField(db_column='LastPerformanceScan', blank=True, null=True)  # Field name made lowercase.
    scannedby = models.IntegerField(db_column='ScannedBy')  # Field name made lowercase.
    lastsccmscan = models.DateTimeField(db_column='LastSccmScan', blank=True, null=True)  # Field name made lowercase.
    lastassetradarscan = models.DateTimeField(db_column='LastAssetRadarScan', blank=True, null=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.
    cloudstatusid = models.IntegerField(db_column='CloudStatusId')  # Field name made lowercase.
    lsagentversionthroughrelay = models.CharField(db_column='LsAgentVersionThroughRelay', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastlsagentthroughrelay = models.DateTimeField(db_column='LastLsAgentThroughRelay', blank=True, null=True)  # Field name made lowercase.
    lastseencredentials = models.TextField(db_column='LastseenCredentials', blank=True, null=True)  # Field name made lowercase.
    lasttriedcredentials = models.TextField(db_column='LasttriedCredentials', blank=True, null=True)  # Field name made lowercase.
    lasttriggeredcredentials = models.TextField(db_column='LasttriggeredCredentials', blank=True, null=True)  # Field name made lowercase.
    lsagentversiondirect = models.CharField(db_column='LsAgentVersionDirect', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastlsagentdirect = models.DateTimeField(db_column='LastLsAgentDirect', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAssets'


class Tblassetscloudstatus(models.Model):
    assetid = models.OneToOneField(Tblassets, models.DO_NOTHING, db_column='AssetID', primary_key=True)  # Field name made lowercase.
    cloudstatusid = models.ForeignKey('Tsyscloudstatus', models.DO_NOTHING, db_column='CloudStatusId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAssetsCloudStatus'


class Tblautorun(models.Model):
    autorunid = models.AutoField(db_column='AutorunID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    autorununi = models.ForeignKey('Tblautorununi', models.DO_NOTHING, db_column='AutorunUNI')  # Field name made lowercase.
    locationid = models.ForeignKey('Tblautorunloc', models.DO_NOTHING, db_column='LocationID')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAutorun'


class Tblautorunhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    autorununi = models.IntegerField(db_column='AutorunUNI', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAutorunHist'


class Tblautorunloc(models.Model):
    locationid = models.AutoField(db_column='LocationID', primary_key=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', unique=True, max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAutorunLoc'


class Tblautorununi(models.Model):
    autorununi = models.AutoField(db_column='AutorunUNI', primary_key=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=100, blank=True, null=True)  # Field name made lowercase.
    command = models.CharField(db_column='Command', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAutorunUni'
        unique_together = (('caption', 'command'),)


class Tblazureadcontainer(models.Model):
    azureadcontainerid = models.AutoField(db_column='AzureAdContainerId', primary_key=True)  # Field name made lowercase.
    tenantid = models.CharField(db_column='TenantId', unique=True, max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAzureAdContainer'


class Tblazureaddevice(models.Model):
    azureaddeviceid = models.OneToOneField('Tblazureadobject', models.DO_NOTHING, db_column='AzureAdDeviceId', primary_key=True)  # Field name made lowercase.
    azureid = models.CharField(db_column='AzureId', max_length=36)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    accountenabled = models.BooleanField(db_column='AccountEnabled')  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceId', max_length=36)  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=500)  # Field name made lowercase.
    iscompliant = models.BooleanField(db_column='IsCompliant', blank=True, null=True)  # Field name made lowercase.
    ismanaged = models.BooleanField(db_column='IsManaged', blank=True, null=True)  # Field name made lowercase.
    mdmappid = models.CharField(db_column='MdmAppId', max_length=500, blank=True, null=True)  # Field name made lowercase.
    onpremiseslastsyncdatetime = models.DateTimeField(db_column='OnPremisesLastSyncDateTime', blank=True, null=True)  # Field name made lowercase.
    onpremisessyncenabled = models.BooleanField(db_column='OnPremisesSyncEnabled', blank=True, null=True)  # Field name made lowercase.
    operatingsystem = models.CharField(db_column='OperatingSystem', max_length=500)  # Field name made lowercase.
    operatingsystemversion = models.CharField(db_column='OperatingSystemVersion', max_length=500)  # Field name made lowercase.
    profiletype = models.CharField(db_column='ProfileType', max_length=500, blank=True, null=True)  # Field name made lowercase.
    registeredownerid = models.CharField(db_column='RegisteredOwnerId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    trusttype = models.CharField(db_column='TrustType', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAzureAdDevice'


class Tblazureadgroup(models.Model):
    azureadgroupid = models.OneToOneField('Tblazureadobject', models.DO_NOTHING, db_column='AzureAdGroupId', primary_key=True)  # Field name made lowercase.
    azureid = models.CharField(db_column='AzureId', max_length=36)  # Field name made lowercase.
    createddatetime = models.DateTimeField(db_column='CreatedDateTime', blank=True, null=True)  # Field name made lowercase.
    deleteddatetime = models.DateTimeField(db_column='DeletedDateTime', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    expirationdatetime = models.DateTimeField(db_column='ExpirationDateTime', blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(db_column='Mail', max_length=500, blank=True, null=True)  # Field name made lowercase.
    mailenabled = models.BooleanField(db_column='MailEnabled', blank=True, null=True)  # Field name made lowercase.
    mailnickname = models.CharField(db_column='MailNickname', max_length=500, blank=True, null=True)  # Field name made lowercase.
    onpremisesdomainname = models.CharField(db_column='OnPremisesDomainName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    onpremiseslastsyncdatetime = models.DateTimeField(db_column='OnPremisesLastSyncDateTime', blank=True, null=True)  # Field name made lowercase.
    onpremisesnetbiosname = models.CharField(db_column='OnPremisesNetBiosName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    onpremisessamaccountname = models.CharField(db_column='OnPremisesSamAccountName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    onpremisessecurityidentifier = models.CharField(db_column='OnPremisesSecurityIdentifier', max_length=500, blank=True, null=True)  # Field name made lowercase.
    onpremisessyncenabled = models.BooleanField(db_column='OnPremisesSyncEnabled', blank=True, null=True)  # Field name made lowercase.
    proxyaddresses = models.CharField(db_column='ProxyAddresses', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    reneweddatetime = models.DateTimeField(db_column='RenewedDateTime', blank=True, null=True)  # Field name made lowercase.
    securityenabled = models.BooleanField(db_column='SecurityEnabled', blank=True, null=True)  # Field name made lowercase.
    securityidentifier = models.CharField(db_column='SecurityIdentifier', max_length=500, blank=True, null=True)  # Field name made lowercase.
    visibility = models.CharField(db_column='Visibility', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAzureAdGroup'


class Tblazureadgroupmembership(models.Model):
    azureadgroupmembershipid = models.AutoField(db_column='AzureAdGroupMembershipId', primary_key=True)  # Field name made lowercase.
    azureadparentobjectid = models.ForeignKey('Tblazureadobject', models.DO_NOTHING, db_column='AzureAdParentObjectId')  # Field name made lowercase.
    azureadchildobjectid = models.ForeignKey('Tblazureadobject', models.DO_NOTHING, db_column='AzureAdChildObjectId')  # Field name made lowercase.
    azureadcontainerid = models.ForeignKey(Tblazureadcontainer, models.DO_NOTHING, db_column='AzureAdContainerId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAzureAdGroupMembership'
        unique_together = (('azureadchildobjectid', 'azureadparentobjectid'),)


class Tblazureadobject(models.Model):
    azureadobjectid = models.AutoField(db_column='AzureAdObjectId', primary_key=True)  # Field name made lowercase.
    azureadcontainerid = models.ForeignKey(Tblazureadcontainer, models.DO_NOTHING, db_column='AzureAdContainerId')  # Field name made lowercase.
    azureadobjecttype = models.IntegerField(db_column='AzureAdObjectType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAzureAdObject'


class Tblazureadorganization(models.Model):
    azureadorganizationid = models.OneToOneField(Tblazureadcontainer, models.DO_NOTHING, db_column='AzureAdOrganizationId', primary_key=True)  # Field name made lowercase.
    businessphone = models.CharField(db_column='BusinessPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=500, blank=True, null=True)  # Field name made lowercase.
    companylastdirsynctime = models.DateTimeField(db_column='CompanyLastDirSyncTime', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=500, blank=True, null=True)  # Field name made lowercase.
    countrylettercode = models.CharField(db_column='CountryLetterCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dirsyncenabled = models.BooleanField(db_column='DirSyncEnabled', blank=True, null=True)  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=60, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=300, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lastscan = models.DateTimeField(db_column='LastScan')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAzureAdOrganization'


class Tblazureaduser(models.Model):
    azureaduserid = models.OneToOneField(Tblazureadobject, models.DO_NOTHING, db_column='AzureAdUserId', primary_key=True)  # Field name made lowercase.
    azureid = models.CharField(db_column='AzureId', max_length=36)  # Field name made lowercase.
    accountenabled = models.BooleanField(db_column='AccountEnabled')  # Field name made lowercase.
    businessphones = models.CharField(db_column='BusinessPhones', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createddatetime = models.DateTimeField(db_column='CreatedDateTime', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=500, blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=100, blank=True, null=True)  # Field name made lowercase.
    deleteddatetime = models.DateTimeField(db_column='DeletedDateTime', blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=500, blank=True, null=True)  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    employeeid = models.CharField(db_column='EmployeeId', max_length=500, blank=True, null=True)  # Field name made lowercase.
    employeetype = models.CharField(db_column='EmployeeType', max_length=500, blank=True, null=True)  # Field name made lowercase.
    faxnumber = models.CharField(db_column='FaxNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    givenname = models.CharField(db_column='GivenName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    imaddresses = models.CharField(db_column='ImAddresses', max_length=500, blank=True, null=True)  # Field name made lowercase.
    jobtitle = models.CharField(db_column='JobTitle', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    lastpasswordchangedatetime = models.DateTimeField(db_column='LastPasswordChangeDateTime', blank=True, null=True)  # Field name made lowercase.
    lastlogon = models.DateTimeField(db_column='LastLogon', blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(db_column='Mail', max_length=500, blank=True, null=True)  # Field name made lowercase.
    managerupn = models.CharField(db_column='ManagerUpn', max_length=500, blank=True, null=True)  # Field name made lowercase.
    mobilephone = models.CharField(db_column='MobilePhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    officelocation = models.CharField(db_column='OfficeLocation', max_length=500, blank=True, null=True)  # Field name made lowercase.
    onpremisesdomainname = models.CharField(db_column='OnPremisesDomainName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    onpremisesou = models.CharField(db_column='OnPremisesOU', max_length=500, blank=True, null=True)  # Field name made lowercase.
    onpremiseslastsyncdatetime = models.DateTimeField(db_column='OnPremisesLastSyncDateTime', blank=True, null=True)  # Field name made lowercase.
    onpremisesdistinguishedname = models.CharField(db_column='OnPremisesDistinguishedName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    onpremisesimmutableid = models.CharField(db_column='OnPremisesImmutableId', max_length=500, blank=True, null=True)  # Field name made lowercase.
    onpremisessamaccountname = models.CharField(db_column='OnPremisesSamAccountName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    onpremisessecurityidentifier = models.CharField(db_column='OnPremisesSecurityIdentifier', max_length=500, blank=True, null=True)  # Field name made lowercase.
    onpremisessyncenabled = models.BooleanField(db_column='OnPremisesSyncEnabled', blank=True, null=True)  # Field name made lowercase.
    onpremisesuserprincipalname = models.CharField(db_column='OnPremisesUserPrincipalName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    othermails = models.CharField(db_column='OtherMails', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    passwordpolicies = models.CharField(db_column='PasswordPolicies', max_length=500, blank=True, null=True)  # Field name made lowercase.
    passwordprofile = models.CharField(db_column='PasswordProfile', max_length=500, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    proxyaddresses = models.CharField(db_column='ProxyAddresses', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    streetaddress = models.CharField(db_column='StreetAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=500, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=500, blank=True, null=True)  # Field name made lowercase.
    userprincipalname = models.CharField(db_column='UserPrincipalName', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAzureAdUser'


class Tblazuredisk(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    azureresourcegroupid = models.ForeignKey('Tblazureresourcegroup', models.DO_NOTHING, db_column='AzureResourceGroupId')  # Field name made lowercase.
    azureid = models.CharField(db_column='AzureId', max_length=500)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='Tags', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    provisioningstate = models.CharField(db_column='ProvisioningState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    creationmethod = models.CharField(db_column='CreationMethod', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ostype = models.CharField(db_column='OsType', max_length=25, blank=True, null=True)  # Field name made lowercase.
    disksizegb = models.IntegerField(db_column='DiskSizeGb', blank=True, null=True)  # Field name made lowercase.
    storageaccounttype = models.CharField(db_column='StorageAccountType', max_length=25, blank=True, null=True)  # Field name made lowercase.
    creationsourcetype = models.CharField(db_column='CreationSourceType', max_length=25, blank=True, null=True)  # Field name made lowercase.
    timecreated = models.DateTimeField(db_column='TimeCreated', blank=True, null=True)  # Field name made lowercase.
    zones = models.CharField(db_column='Zones', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAzureDisk'


class Tblazureipconfiguration(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    azurenetworkinterfaceid = models.ForeignKey('Tblazurenetworkinterface', models.DO_NOTHING, db_column='AzureNetworkInterfaceId')  # Field name made lowercase.
    azureid = models.CharField(db_column='AzureId', max_length=500)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    provisioningstate = models.CharField(db_column='ProvisioningState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    privateipaddress = models.CharField(db_column='PrivateIpAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    privateipaddressversion = models.CharField(db_column='PrivateIpAddressVersion', max_length=5, blank=True, null=True)  # Field name made lowercase.
    privateipallocationmethod = models.CharField(db_column='PrivateIpAllocationMethod', max_length=10, blank=True, null=True)  # Field name made lowercase.
    isprimary = models.BooleanField(db_column='IsPrimary')  # Field name made lowercase.
    publicipaddress = models.CharField(db_column='PublicIpAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    publicipaddressversion = models.CharField(db_column='PublicIpAddressVersion', max_length=5, blank=True, null=True)  # Field name made lowercase.
    publicipallocationmethod = models.CharField(db_column='PublicIpAllocationMethod', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fqdn = models.CharField(db_column='Fqdn', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reversefqdn = models.CharField(db_column='ReverseFqdn', max_length=100, blank=True, null=True)  # Field name made lowercase.
    leafdomainlabel = models.CharField(db_column='LeafDomainLabel', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idletimeoutinminutes = models.IntegerField(db_column='IdleTimeoutInMinutes')  # Field name made lowercase.
    hasassignedloadbalancer = models.BooleanField(db_column='HasAssignedLoadBalancer')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAzureIpConfiguration'


class Tblazurenetwork(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    azureresourcegroupid = models.ForeignKey('Tblazureresourcegroup', models.DO_NOTHING, db_column='AzureResourceGroupId')  # Field name made lowercase.
    azureid = models.CharField(db_column='AzureId', max_length=500)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='Tags', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    provisioningstate = models.CharField(db_column='ProvisioningState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isddosprotectionenabled = models.BooleanField(db_column='IsDdosProtectionEnabled')  # Field name made lowercase.
    isvmprotectionenabled = models.BooleanField(db_column='IsVmProtectionEnabled')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAzureNetwork'


class Tblazurenetworkinterface(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    azurevirtualmachineid = models.ForeignKey('Tblazurevirtualmachine', models.DO_NOTHING, db_column='AzureVirtualMachineId', blank=True, null=True)  # Field name made lowercase.
    azureresourcegroupid = models.ForeignKey('Tblazureresourcegroup', models.DO_NOTHING, db_column='AzureResourceGroupId')  # Field name made lowercase.
    azureid = models.CharField(db_column='AzureId', max_length=500)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='Tags', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    provisioningstate = models.CharField(db_column='ProvisioningState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    isacceleratednetworkingenabled = models.BooleanField(db_column='IsAcceleratedNetworkingEnabled')  # Field name made lowercase.
    isipforwardingenabled = models.BooleanField(db_column='IsIpForwardingEnabled')  # Field name made lowercase.
    isprimarynetworkinterface = models.BooleanField(db_column='IsPrimaryNetworkInterface')  # Field name made lowercase.
    internaldnsnamelabel = models.CharField(db_column='InternalDnsNameLabel', max_length=100, blank=True, null=True)  # Field name made lowercase.
    internaldomainnamesuffix = models.CharField(db_column='InternalDomainNameSuffix', max_length=100, blank=True, null=True)  # Field name made lowercase.
    internalfqdn = models.CharField(db_column='InternalFqdn', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dnsservers = models.CharField(db_column='DnsServers', max_length=500, blank=True, null=True)  # Field name made lowercase.
    applieddnsservers = models.CharField(db_column='AppliedDnsServers', max_length=500, blank=True, null=True)  # Field name made lowercase.
    azurenetworksecuritygroupid = models.ForeignKey('Tblazurenetworksecuritygroup', models.DO_NOTHING, db_column='AzureNetworkSecurityGroupId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAzureNetworkInterface'


class Tblazurenetworksecuritygroup(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    azureresourcegroupid = models.ForeignKey('Tblazureresourcegroup', models.DO_NOTHING, db_column='AzureResourceGroupId')  # Field name made lowercase.
    azureid = models.CharField(db_column='AzureId', max_length=500)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='Tags', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    provisioningstate = models.CharField(db_column='ProvisioningState', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAzureNetworkSecurityGroup'


class Tblazureresourcegroup(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    azureid = models.CharField(db_column='AzureId', max_length=500)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='Tags', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    provisioningstate = models.CharField(db_column='ProvisioningState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subscriptionid = models.CharField(db_column='SubscriptionId', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAzureResourceGroup'


class Tblazuresecurityrule(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    azurenetworksecuritygroupid = models.ForeignKey(Tblazurenetworksecuritygroup, models.DO_NOTHING, db_column='AzureNetworkSecurityGroupId')  # Field name made lowercase.
    azureid = models.CharField(db_column='AzureId', max_length=500)  # Field name made lowercase.
    ruletype = models.CharField(db_column='RuleType', max_length=20)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    provisioningstate = models.CharField(db_column='ProvisioningState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    access = models.CharField(db_column='Access', max_length=50, blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    direction = models.CharField(db_column='Direction', max_length=50, blank=True, null=True)  # Field name made lowercase.
    protocol = models.CharField(db_column='Protocol', max_length=20, blank=True, null=True)  # Field name made lowercase.
    destinationportrange = models.CharField(db_column='DestinationPortRange', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourceportrange = models.CharField(db_column='SourcePortRange', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destinationaddressprefix = models.CharField(db_column='DestinationAddressPrefix', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sourceaddressprefix = models.CharField(db_column='SourceAddressPrefix', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAzureSecurityRule'


class Tblazuresubnet(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    azurenetworkid = models.ForeignKey(Tblazurenetwork, models.DO_NOTHING, db_column='AzureNetworkId')  # Field name made lowercase.
    azureid = models.CharField(db_column='AzureId', max_length=500)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=50, blank=True, null=True)  # Field name made lowercase.
    provisioningstate = models.CharField(db_column='ProvisioningState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    addressprefix = models.CharField(db_column='AddressPrefix', max_length=25, blank=True, null=True)  # Field name made lowercase.
    azurenetworksecuritygroupid = models.ForeignKey(Tblazurenetworksecuritygroup, models.DO_NOTHING, db_column='AzureNetworkSecurityGroupId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAzureSubnet'


class Tblazuresubnetipconfiguration(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    azuresubnetid = models.ForeignKey(Tblazuresubnet, models.DO_NOTHING, db_column='AzureSubnetId')  # Field name made lowercase.
    azureid = models.CharField(db_column='AzureId', max_length=500)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    provisioningstate = models.CharField(db_column='ProvisioningState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    privateipaddress = models.CharField(db_column='PrivateIpAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    privateipaddressversion = models.CharField(db_column='PrivateIpAddressVersion', max_length=5, blank=True, null=True)  # Field name made lowercase.
    privateipallocationmethod = models.CharField(db_column='PrivateIpAllocationMethod', max_length=10, blank=True, null=True)  # Field name made lowercase.
    isprimary = models.BooleanField(db_column='IsPrimary')  # Field name made lowercase.
    publicipaddress = models.CharField(db_column='PublicIpAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    publicipaddressversion = models.CharField(db_column='PublicIpAddressVersion', max_length=5, blank=True, null=True)  # Field name made lowercase.
    publicipallocationmethod = models.CharField(db_column='PublicIpAllocationMethod', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fqdn = models.CharField(db_column='Fqdn', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reversefqdn = models.CharField(db_column='ReverseFqdn', max_length=100, blank=True, null=True)  # Field name made lowercase.
    leafdomainlabel = models.CharField(db_column='LeafDomainLabel', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idletimeoutinminutes = models.IntegerField(db_column='IdleTimeoutInMinutes')  # Field name made lowercase.
    hasassignedloadbalancer = models.BooleanField(db_column='HasAssignedLoadBalancer')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAzureSubnetIpConfiguration'


class Tblazurevirtualmachine(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    azureresourcegroupid = models.ForeignKey(Tblazureresourcegroup, models.DO_NOTHING, db_column='AzureResourceGroupId')  # Field name made lowercase.
    azureid = models.CharField(db_column='AzureId', max_length=500)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='Tags', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    provisioningstate = models.CharField(db_column='ProvisioningState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bootdiagnosticsstorageuri = models.CharField(db_column='BootDiagnosticsStorageUri', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isbootdiagnosticsenabled = models.BooleanField(db_column='IsBootDiagnosticsEnabled')  # Field name made lowercase.
    ismanageddiskenabled = models.BooleanField(db_column='IsManagedDiskEnabled')  # Field name made lowercase.
    ismanagedserviceidentityenabled = models.BooleanField(db_column='IsManagedServiceIdentityEnabled')  # Field name made lowercase.
    licensetype = models.CharField(db_column='LicenseType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    powerstate = models.CharField(db_column='PowerState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=50, blank=True, null=True)  # Field name made lowercase.
    managedserviceidentitytype = models.CharField(db_column='ManagedServiceIdentityType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ostype = models.CharField(db_column='OsType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    osname = models.CharField(db_column='OsName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osversion = models.CharField(db_column='OsVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    diskimageoffer = models.CharField(db_column='DiskImageOffer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    diskimagepublisher = models.CharField(db_column='DiskImagePublisher', max_length=256, blank=True, null=True)  # Field name made lowercase.
    diskimagesku = models.CharField(db_column='DiskImageSku', max_length=100, blank=True, null=True)  # Field name made lowercase.
    diskimageversion = models.CharField(db_column='DiskImageVersion', max_length=25, blank=True, null=True)  # Field name made lowercase.
    maxdatadiskcount = models.IntegerField(db_column='MaxDataDiskCount')  # Field name made lowercase.
    memoryinmb = models.IntegerField(db_column='MemoryInMb')  # Field name made lowercase.
    numberofcores = models.IntegerField(db_column='NumberOfCores')  # Field name made lowercase.
    osdisksizeinmb = models.IntegerField(db_column='OsDiskSizeInMb')  # Field name made lowercase.
    resourcedisksizeinmb = models.IntegerField(db_column='ResourceDiskSizeInMb')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAzureVirtualMachine'


class Tblazurevirtualmachinedatadisk(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    azurevirtualmachineid = models.ForeignKey(Tblazurevirtualmachine, models.DO_NOTHING, db_column='AzureVirtualMachineId')  # Field name made lowercase.
    disktype = models.CharField(db_column='DiskType', max_length=20)  # Field name made lowercase.
    lun = models.IntegerField(db_column='Lun', blank=True, null=True)  # Field name made lowercase.
    vhduri = models.CharField(db_column='VhdUri', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    imageuri = models.CharField(db_column='ImageUri', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    iswriteacceleratorenabled = models.BooleanField(db_column='IsWriteAcceleratorEnabled')  # Field name made lowercase.
    isdiskencryptionenabled = models.BooleanField(db_column='IsDiskEncryptionEnabled')  # Field name made lowercase.
    cachingtype = models.CharField(db_column='CachingType', max_length=20)  # Field name made lowercase.
    azurediskid = models.ForeignKey(Tblazuredisk, models.DO_NOTHING, db_column='AzureDiskId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAzureVirtualMachineDataDisk'


class Tblazurevirtualmachineextension(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    azurevirtualmachineid = models.ForeignKey(Tblazurevirtualmachine, models.DO_NOTHING, db_column='AzureVirtualMachineId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    typehandlerversion = models.CharField(db_column='TypeHandlerVersion', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAzureVirtualMachineExtension'


class Tblbios(models.Model):
    win32_biosid = models.AutoField(db_column='Win32_BIOSid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    bioscharacteristics = models.CharField(db_column='BiosCharacteristics', max_length=400, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    currentlanguage = models.CharField(db_column='CurrentLanguage', max_length=500, blank=True, null=True)  # Field name made lowercase.
    installablelanguages = models.DecimalField(db_column='InstallableLanguages', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    primarybios = models.BooleanField(db_column='PrimaryBIOS', blank=True, null=True)  # Field name made lowercase.
    releasedate = models.DateTimeField(db_column='ReleaseDate', blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    smbiosbiosversion = models.CharField(db_column='SMBIOSBIOSVersion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    smbiosmajorversion = models.DecimalField(db_column='SMBIOSMajorVersion', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    smbiosminorversion = models.DecimalField(db_column='SMBIOSMinorVersion', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    smbiospresent = models.BooleanField(db_column='SMBIOSPresent', blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblBIOS'


class Tblbioshist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    bioscharacteristics = models.CharField(db_column='BiosCharacteristics', max_length=400, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    currentlanguage = models.CharField(db_column='CurrentLanguage', max_length=500, blank=True, null=True)  # Field name made lowercase.
    installablelanguages = models.DecimalField(db_column='InstallableLanguages', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    primarybios = models.BooleanField(db_column='PrimaryBIOS', blank=True, null=True)  # Field name made lowercase.
    releasedate = models.DateTimeField(db_column='ReleaseDate', blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    smbiosbiosversion = models.CharField(db_column='SMBIOSBIOSVersion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    smbiosmajorversion = models.DecimalField(db_column='SMBIOSMajorVersion', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    smbiosminorversion = models.DecimalField(db_column='SMBIOSMinorVersion', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    smbiospresent = models.BooleanField(db_column='SMBIOSPresent', blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblBIOSHist'


class Tblbaseboard(models.Model):
    win32_baseboardid = models.AutoField(db_column='Win32_BaseBoardid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    hostingboard = models.BooleanField(db_column='HostingBoard', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    product = models.CharField(db_column='Product', max_length=450, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=450, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblBaseBoard'


class Tblbaseboardhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    hostingboard = models.BooleanField(db_column='HostingBoard', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    product = models.CharField(db_column='Product', max_length=450, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=450, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblBaseBoardHist'


class Tblbattery(models.Model):
    win32_batteryid = models.AutoField(db_column='Win32_Batteryid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    availability = models.DecimalField(db_column='Availability', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    batterystatus = models.DecimalField(db_column='BatteryStatus', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    chemistry = models.DecimalField(db_column='Chemistry', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    designcapacity = models.DecimalField(db_column='DesignCapacity', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=450, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=450, blank=True, null=True)  # Field name made lowercase.
    powermanagementcapabilities = models.CharField(db_column='PowerManagementCapabilities', max_length=400, blank=True, null=True)  # Field name made lowercase.
    powermanagementsupported = models.BooleanField(db_column='PowerManagementSupported', blank=True, null=True)  # Field name made lowercase.
    smartbatteryversion = models.CharField(db_column='SmartBatteryVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblBattery'


class Tblbatteryhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    availability = models.DecimalField(db_column='Availability', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    batterystatus = models.DecimalField(db_column='BatteryStatus', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    chemistry = models.DecimalField(db_column='Chemistry', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    designcapacity = models.DecimalField(db_column='DesignCapacity', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=450, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=450, blank=True, null=True)  # Field name made lowercase.
    powermanagementcapabilities = models.CharField(db_column='PowerManagementCapabilities', max_length=400, blank=True, null=True)  # Field name made lowercase.
    powermanagementsupported = models.BooleanField(db_column='PowerManagementSupported', blank=True, null=True)  # Field name made lowercase.
    smartbatteryversion = models.CharField(db_column='SmartBatteryVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblBatteryHist'


class Tblbitlockerrecoverykey(models.Model):
    recoverykeyid = models.AutoField(db_column='RecoveryKeyId', primary_key=True)  # Field name made lowercase.
    adobjectid = models.ForeignKey(Tbladobjects, models.DO_NOTHING, db_column='AdObjectId')  # Field name made lowercase.
    recoverykey = models.CharField(db_column='RecoveryKey', max_length=256)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblBitLockerRecoveryKey'


class Tblbootconfiguration(models.Model):
    win32_bootconfigurationid = models.AutoField(db_column='Win32_BootConfigurationid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    bootconfigurationuniid = models.ForeignKey('Tblbootconfigurationuni', models.DO_NOTHING, db_column='BootConfigurationuniid')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblBootConfiguration'


class Tblbootconfigurationhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    bootconfigurationuniid = models.IntegerField(db_column='BootConfigurationuniid')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblBootConfigurationHist'


class Tblbootconfigurationuni(models.Model):
    bootconfigurationuniid = models.AutoField(db_column='BootConfigurationuniid', primary_key=True)  # Field name made lowercase.
    bootdirectory = models.CharField(db_column='BootDirectory', max_length=500, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=500, blank=True, null=True)  # Field name made lowercase.
    configurationpath = models.CharField(db_column='ConfigurationPath', max_length=500, blank=True, null=True)  # Field name made lowercase.
    scratchdirectory = models.CharField(db_column='ScratchDirectory', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tempdirectory = models.CharField(db_column='TempDirectory', max_length=500, blank=True, null=True)  # Field name made lowercase.
    hash = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'tblBootConfigurationUni'


class Tblbus(models.Model):
    win32_busid = models.AutoField(db_column='Win32_Busid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    busnum = models.DecimalField(db_column='BusNum', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bustype = models.DecimalField(db_column='BusType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblBus'


class Tblbushist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    busnum = models.DecimalField(db_column='BusNum', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bustype = models.DecimalField(db_column='BusType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblBusHist'


class Tblcdromdrive(models.Model):
    win32_cdromdriveid = models.AutoField(db_column='Win32_CDROMDriveid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    capabilities = models.CharField(db_column='Capabilities', max_length=100, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    drive = models.CharField(db_column='Drive', max_length=20, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    scsibus = models.DecimalField(db_column='SCSIBus', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    scsilogicalunit = models.DecimalField(db_column='SCSILogicalUnit', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    scsiport = models.DecimalField(db_column='SCSIPort', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    scsitargetid = models.DecimalField(db_column='SCSITargetId', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCDROMDrive'


class Tblcdromdrivehist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    capabilities = models.CharField(db_column='Capabilities', max_length=100, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    drive = models.CharField(db_column='Drive', max_length=20, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    scsibus = models.DecimalField(db_column='SCSIBus', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    scsilogicalunit = models.DecimalField(db_column='SCSILogicalUnit', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    scsiport = models.DecimalField(db_column='SCSIPort', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    scsitargetid = models.DecimalField(db_column='SCSITargetId', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCDROMDriveHist'


class Tblcomapplication(models.Model):
    win32_comapplicationid = models.AutoField(db_column='Win32_COMApplicationid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblCOMApplication'


class Tblcomapplicationhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField()
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCOMApplicationHist'


class Tblcplogoninfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    logontime = models.DateTimeField(blank=True, null=True)
    domain = models.CharField(db_column='Domain', max_length=150, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='Ipaddress', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCPlogoninfo'


class Tblcatalogbrand(models.Model):
    id = models.BigIntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    classes = models.CharField(db_column='Classes', max_length=128, blank=True, null=True)  # Field name made lowercase.
    lastupdatetime = models.DateTimeField(db_column='LastUpdateTime', blank=True, null=True)  # Field name made lowercase.
    logoimageurl = models.CharField(db_column='LogoImageUrl', max_length=128, blank=True, null=True)  # Field name made lowercase.
    bannerimageurl = models.CharField(db_column='BannerImageUrl', max_length=128, blank=True, null=True)  # Field name made lowercase.
    wikipediaid = models.CharField(db_column='WikipediaId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    wikipedialangcode = models.CharField(db_column='WikipediaLangCode', max_length=8, blank=True, null=True)  # Field name made lowercase.
    websiteurl = models.CharField(db_column='WebsiteUrl', max_length=256, blank=True, null=True)  # Field name made lowercase.
    supporturl = models.CharField(db_column='SupportUrl', max_length=256, blank=True, null=True)  # Field name made lowercase.
    supportphone = models.CharField(db_column='SupportPhone', max_length=64, blank=True, null=True)  # Field name made lowercase.
    facebookaccount = models.CharField(db_column='FacebookAccount', max_length=64, blank=True, null=True)  # Field name made lowercase.
    twitteraccount = models.CharField(db_column='TwitterAccount', max_length=64, blank=True, null=True)  # Field name made lowercase.
    instagramaccount = models.CharField(db_column='InstagramAccount', max_length=64, blank=True, null=True)  # Field name made lowercase.
    pinterestaccount = models.CharField(db_column='PinterestAccount', max_length=64, blank=True, null=True)  # Field name made lowercase.
    youtubeaccount = models.CharField(db_column='YoutubeAccount', max_length=64, blank=True, null=True)  # Field name made lowercase.
    linkedinaccount = models.CharField(db_column='LinkedInAccount', max_length=64, blank=True, null=True)  # Field name made lowercase.
    warrantyurl = models.CharField(db_column='WarrantyUrl', max_length=256, blank=True, null=True)  # Field name made lowercase.
    warrantydirecturl = models.CharField(db_column='WarrantyDirectUrl', max_length=256, blank=True, null=True)  # Field name made lowercase.
    communityurl = models.CharField(db_column='CommunityUrl', max_length=256, blank=True, null=True)  # Field name made lowercase.
    matchscore = models.SmallIntegerField(db_column='MatchScore', blank=True, null=True)  # Field name made lowercase.
    lastonlineupdatetimeutc = models.DateTimeField(db_column='LastOnlineUpdateTimeUtc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCatalogBrand'


class Tblcatalogmodel(models.Model):
    id = models.BigIntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=512, blank=True, null=True)  # Field name made lowercase.
    lastupdatetime = models.DateTimeField(db_column='LastUpdateTime', blank=True, null=True)  # Field name made lowercase.
    typeid = models.BigIntegerField(db_column='TypeId')  # Field name made lowercase.
    brandid = models.BigIntegerField(db_column='BrandId')  # Field name made lowercase.
    modelcodes = models.CharField(db_column='ModelCodes', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    isfamily = models.BooleanField(db_column='IsFamily')  # Field name made lowercase.
    familyid = models.BigIntegerField(db_column='FamilyId', blank=True, null=True)  # Field name made lowercase.
    releasedate = models.DateTimeField(db_column='ReleaseDate', blank=True, null=True)  # Field name made lowercase.
    endofsupportdate = models.DateTimeField(db_column='EndOfSupportDate', blank=True, null=True)  # Field name made lowercase.
    endoflifedate = models.DateTimeField(db_column='EndOfLifeDate', blank=True, null=True)  # Field name made lowercase.
    manualurl = models.CharField(db_column='ManualUrl', max_length=256, blank=True, null=True)  # Field name made lowercase.
    faqurl = models.CharField(db_column='FaqUrl', max_length=256, blank=True, null=True)  # Field name made lowercase.
    popularity = models.SmallIntegerField(db_column='Popularity', blank=True, null=True)  # Field name made lowercase.
    priceclass = models.CharField(db_column='PriceClass', max_length=64, blank=True, null=True)  # Field name made lowercase.
    productclass = models.CharField(db_column='ProductClass', max_length=64, blank=True, null=True)  # Field name made lowercase.
    matchscore = models.SmallIntegerField(db_column='MatchScore', blank=True, null=True)  # Field name made lowercase.
    smarthomeapplehomekit = models.BooleanField(db_column='SmartHomeAppleHomeKit', blank=True, null=True)  # Field name made lowercase.
    smarthomeifttthandle = models.CharField(db_column='SmartHomeIftttHandle', max_length=256, blank=True, null=True)  # Field name made lowercase.
    smarthomehomeassistanthandle = models.CharField(db_column='SmartHomeHomeAssistantHandle', max_length=64, blank=True, null=True)  # Field name made lowercase.
    smarthomeopenhabhandle = models.CharField(db_column='SmartHomeOpenHabHandle', max_length=64, blank=True, null=True)  # Field name made lowercase.
    smarthomeamazonalexa = models.BooleanField(db_column='SmartHomeAmazonAlexa', blank=True, null=True)  # Field name made lowercase.
    smarthomeamazonalexalanguagecodes = models.CharField(db_column='SmartHomeAmazonAlexaLanguageCodes', max_length=64, blank=True, null=True)  # Field name made lowercase.
    smarthomegoogleassistant = models.BooleanField(db_column='SmartHomeGoogleAssistant', blank=True, null=True)  # Field name made lowercase.
    smarthomegoogleassistantlanguagecodes = models.CharField(db_column='SmartHomeGoogleAssistantLanguageCodes', max_length=64, blank=True, null=True)  # Field name made lowercase.
    lastonlineupdatetimeutc = models.DateTimeField(db_column='LastOnlineUpdateTimeUtc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCatalogModel'


class Tblcatalogos(models.Model):
    id = models.BigIntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=128, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=128, blank=True, null=True)  # Field name made lowercase.
    build = models.CharField(db_column='Build', max_length=128, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    lastupdatetime = models.DateTimeField(db_column='LastUpdateTime', blank=True, null=True)  # Field name made lowercase.
    makeid = models.BigIntegerField(db_column='MakeId', blank=True, null=True)  # Field name made lowercase.
    parentid = models.BigIntegerField(db_column='ParentId', blank=True, null=True)  # Field name made lowercase.
    releasedate = models.DateTimeField(db_column='ReleaseDate', blank=True, null=True)  # Field name made lowercase.
    endofsupportdate = models.DateTimeField(db_column='EndOfSupportDate', blank=True, null=True)  # Field name made lowercase.
    endoflifedate = models.DateTimeField(db_column='EndOfLifeDate', blank=True, null=True)  # Field name made lowercase.
    logoimageurl = models.CharField(db_column='LogoImageUrl', max_length=128, blank=True, null=True)  # Field name made lowercase.
    bannerimageurl = models.CharField(db_column='BannerImageUrl', max_length=128, blank=True, null=True)  # Field name made lowercase.
    wikipediaid = models.CharField(db_column='WikipediaId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    wikipedialangcode = models.CharField(db_column='WikipediaLangCode', max_length=8, blank=True, null=True)  # Field name made lowercase.
    websiteurl = models.CharField(db_column='WebsiteUrl', max_length=256, blank=True, null=True)  # Field name made lowercase.
    supporturl = models.CharField(db_column='SupportUrl', max_length=256, blank=True, null=True)  # Field name made lowercase.
    supportphone = models.CharField(db_column='SupportPhone', max_length=64, blank=True, null=True)  # Field name made lowercase.
    facebookaccount = models.CharField(db_column='FacebookAccount', max_length=64, blank=True, null=True)  # Field name made lowercase.
    twitteraccount = models.CharField(db_column='TwitterAccount', max_length=64, blank=True, null=True)  # Field name made lowercase.
    matchscore = models.SmallIntegerField(db_column='MatchScore', blank=True, null=True)  # Field name made lowercase.
    lastonlineupdatetimeutc = models.DateTimeField(db_column='LastOnlineUpdateTimeUtc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCatalogOs'


class Tblcatalogsoftware(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=128, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=64, blank=True, null=True)  # Field name made lowercase.
    marketversion = models.CharField(db_column='MarketVersion', max_length=64, blank=True, null=True)  # Field name made lowercase.
    build = models.CharField(db_column='Build', max_length=64, blank=True, null=True)  # Field name made lowercase.
    edition = models.CharField(db_column='Edition', max_length=64, blank=True, null=True)  # Field name made lowercase.
    architecture = models.CharField(db_column='Architecture', max_length=32, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=64, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=64, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=128, blank=True, null=True)  # Field name made lowercase.
    cpe = models.CharField(db_column='Cpe', max_length=128, blank=True, null=True)  # Field name made lowercase.
    rawhash = models.CharField(db_column='RawHash', unique=True, max_length=64)  # Field name made lowercase.
    nrehash = models.CharField(db_column='NreHash', max_length=64)  # Field name made lowercase.
    parentid = models.BigIntegerField(db_column='ParentId', blank=True, null=True)  # Field name made lowercase.
    brandid = models.BigIntegerField(db_column='BrandId', blank=True, null=True)  # Field name made lowercase.
    assettype = models.IntegerField(db_column='AssetType')  # Field name made lowercase.
    lastonlineupdatetimeutc = models.DateTimeField(db_column='LastOnlineUpdateTimeUtc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCatalogSoftware'


class Tblcertificateenhancedkeyusages(models.Model):
    enhancedkeyusageid = models.BigAutoField(db_column='EnhancedKeyUsageID', primary_key=True)  # Field name made lowercase.
    certificateid = models.ForeignKey('Tblcertificates', models.DO_NOTHING, db_column='CertificateID')  # Field name made lowercase.
    oidname = models.CharField(db_column='OidName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    oidvalue = models.CharField(db_column='OidValue', max_length=200)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCertificateEnhancedKeyUsages'


class Tblcertificatekeyusages(models.Model):
    keyusageid = models.BigAutoField(db_column='KeyUsageID', primary_key=True)  # Field name made lowercase.
    certificateid = models.ForeignKey('Tblcertificates', models.DO_NOTHING, db_column='CertificateID')  # Field name made lowercase.
    keyusagetypeid = models.ForeignKey('Tsyscertificatekeyusagetypes', models.DO_NOTHING, db_column='KeyUsageTypeID')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCertificateKeyUsages'
        unique_together = (('certificateid', 'keyusagetypeid'),)


class Tblcertificatelocations(models.Model):
    certificatelocationid = models.BigAutoField(db_column='CertificateLocationID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    store = models.CharField(db_column='Store', max_length=330)  # Field name made lowercase.
    folder = models.CharField(db_column='Folder', max_length=50)  # Field name made lowercase.
    certificateid = models.ForeignKey('Tblcertificates', models.DO_NOTHING, db_column='CertificateID')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCertificateLocations'
        unique_together = (('assetid', 'store', 'folder', 'certificateid'),)


class Tblcertificates(models.Model):
    certificateid = models.BigAutoField(db_column='CertificateID', primary_key=True)  # Field name made lowercase.
    thumbprint = models.CharField(db_column='Thumbprint', unique=True, max_length=40)  # Field name made lowercase.
    serial = models.CharField(db_column='Serial', max_length=100)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=500, blank=True, null=True)  # Field name made lowercase.
    subjectname = models.CharField(db_column='SubjectName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    subjectalternativename = models.TextField(db_column='SubjectAlternativeName', blank=True, null=True)  # Field name made lowercase.
    issuer = models.CharField(db_column='Issuer', max_length=250)  # Field name made lowercase.
    issuername = models.CharField(db_column='IssuerName', max_length=100)  # Field name made lowercase.
    friendlyname = models.CharField(db_column='FriendlyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    expirationdate = models.DateTimeField(db_column='ExpirationDate')  # Field name made lowercase.
    isarchived = models.BooleanField(db_column='IsArchived')  # Field name made lowercase.
    hasprivatekey = models.BooleanField(db_column='HasPrivateKey')  # Field name made lowercase.
    version = models.IntegerField(db_column='Version')  # Field name made lowercase.
    signaturealgorithm = models.CharField(db_column='SignatureAlgorithm', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dnsnamelist = models.CharField(db_column='DnsNameList', max_length=200, blank=True, null=True)  # Field name made lowercase.
    template = models.CharField(db_column='Template', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCertificates'


class Tblchangetracking(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    rootentityid = models.IntegerField(db_column='RootEntityId')  # Field name made lowercase.
    childcollectionid = models.IntegerField(db_column='ChildCollectionId')  # Field name made lowercase.
    rootid = models.CharField(db_column='RootId', max_length=128)  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.
    lastsent = models.DateTimeField(db_column='LastSent', blank=True, null=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.
    sendnow = models.BooleanField(db_column='SendNow')  # Field name made lowercase.
    firstupdated = models.DateTimeField(db_column='FirstUpdated', blank=True, null=True)  # Field name made lowercase.
    operationid = models.CharField(db_column='OperationId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblChangeTracking'
        unique_together = (('rootentityid', 'rootid', 'childcollectionid'),)


class Tblchromeos(models.Model):
    chromeosid = models.AutoField(db_column='ChromeOsId', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    annotatedassetid = models.CharField(db_column='AnnotatedAssetId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    annotatedlocation = models.CharField(db_column='AnnotatedLocation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    annotateduser = models.CharField(db_column='AnnotatedUser', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bootmode = models.CharField(db_column='BootMode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceId', max_length=100)  # Field name made lowercase.
    ethernetmacaddress = models.CharField(db_column='EthernetMacAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    firmwareversion = models.CharField(db_column='FirmwareVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastenrollmenttime = models.DateTimeField(db_column='LastEnrollmentTime', blank=True, null=True)  # Field name made lowercase.
    lastsync = models.DateTimeField(db_column='LastSync', blank=True, null=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    meid = models.CharField(db_column='Meid', max_length=15, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=100, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ordernumber = models.CharField(db_column='OrderNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    orgunitpath = models.CharField(db_column='OrgUnitPath', max_length=500, blank=True, null=True)  # Field name made lowercase.
    osversion = models.CharField(db_column='OsVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    platformversion = models.CharField(db_column='PlatformVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=50)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
    supportenddate = models.DateTimeField(db_column='SupportEndDate', blank=True, null=True)  # Field name made lowercase.
    systemramtotal = models.BigIntegerField(db_column='SystemRamTotal', blank=True, null=True)  # Field name made lowercase.
    willautorenew = models.BooleanField(db_column='WillAutoRenew', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblChromeOs'


class Tblchromeosactivetimerange(models.Model):
    chromeosactivetimerangeid = models.AutoField(db_column='ChromeOsActiveTimeRangeId', primary_key=True)  # Field name made lowercase.
    chromeosid = models.ForeignKey(Tblchromeos, models.DO_NOTHING, db_column='ChromeOsId')  # Field name made lowercase.
    activetime = models.IntegerField(db_column='ActiveTime', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblChromeOsActiveTimeRange'


class Tblchromeosrecentuser(models.Model):
    chromeosrecentuserid = models.AutoField(db_column='ChromeOsRecentUserId', primary_key=True)  # Field name made lowercase.
    chromeosid = models.ForeignKey(Tblchromeos, models.DO_NOTHING, db_column='ChromeOsId')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblChromeOsRecentUser'


class Tblchromeostpm(models.Model):
    chromeostpmid = models.AutoField(db_column='ChromeOsTpmId', primary_key=True)  # Field name made lowercase.
    chromeosid = models.ForeignKey(Tblchromeos, models.DO_NOTHING, db_column='ChromeOsId')  # Field name made lowercase.
    family = models.CharField(db_column='Family', max_length=100, blank=True, null=True)  # Field name made lowercase.
    firmwareversion = models.CharField(db_column='FirmwareVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    manufacturercode = models.CharField(db_column='ManufacturerCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    speclevel = models.CharField(db_column='SpecLevel', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modelnumber = models.CharField(db_column='ModelNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vendorspecific = models.CharField(db_column='VendorSpecific', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblChromeOsTpm'


class Tblchromeosvolume(models.Model):
    chromeosvolumeid = models.AutoField(db_column='ChromeOsVolumeId', primary_key=True)  # Field name made lowercase.
    chromeosid = models.ForeignKey(Tblchromeos, models.DO_NOTHING, db_column='ChromeOsId')  # Field name made lowercase.
    volumeid = models.CharField(db_column='VolumeId', max_length=100)  # Field name made lowercase.
    storagefree = models.BigIntegerField(db_column='StorageFree', blank=True, null=True)  # Field name made lowercase.
    storagetotal = models.BigIntegerField(db_column='StorageTotal', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblChromeOsVolume'


class Tblcitrixappliance(models.Model):
    applianceid = models.AutoField(db_column='ApplianceId', primary_key=True)  # Field name made lowercase.
    poolid = models.ForeignKey('Tblcitrixpool', models.DO_NOTHING, db_column='PoolId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixAppliance'


class Tblcitrixguest(models.Model):
    guestid = models.AutoField(db_column='GuestId', primary_key=True)  # Field name made lowercase.
    hostid = models.IntegerField(db_column='HostId', blank=True, null=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    applianceid = models.IntegerField(db_column='ApplianceId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150, blank=True, null=True)  # Field name made lowercase.
    memory = models.BigIntegerField(db_column='Memory', blank=True, null=True)  # Field name made lowercase.
    cpucount = models.BigIntegerField(db_column='CpuCount', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated', blank=True, null=True)  # Field name made lowercase.
    live = models.BooleanField(db_column='Live', blank=True, null=True)  # Field name made lowercase.
    hvmbootpolicy = models.CharField(db_column='HvmBootPolicy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hvmshadowmultiplier = models.FloatField(db_column='HvmShadowMultiplier', blank=True, null=True)  # Field name made lowercase.
    pcibus = models.CharField(db_column='PciBus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pvarguments = models.CharField(db_column='PvArguments', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pvbootloader = models.CharField(db_column='PvBootloader', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pvbootloaderarguments = models.CharField(db_column='PvBootloaderArguments', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pvkernel = models.CharField(db_column='PvKernel', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pvlegacyarguments = models.CharField(db_column='PvLegacyArguments', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pvramdisk = models.CharField(db_column='PvRamdisk', max_length=100, blank=True, null=True)  # Field name made lowercase.
    actionsaftercrash = models.CharField(db_column='ActionsAfterCrash', max_length=100, blank=True, null=True)  # Field name made lowercase.
    actionsafterreboot = models.CharField(db_column='ActionsAfterReboot', max_length=100, blank=True, null=True)  # Field name made lowercase.
    actionsaftershutdown = models.CharField(db_column='ActionsAfterShutdown', max_length=100, blank=True, null=True)  # Field name made lowercase.
    haalwaysrun = models.BooleanField(db_column='HaAlwaysRun', blank=True, null=True)  # Field name made lowercase.
    harestartpriority = models.CharField(db_column='HaRestartPriority', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hardwareplatformversion = models.BigIntegerField(db_column='HardwarePlatformVersion', blank=True, null=True)  # Field name made lowercase.
    lastbootedrecord = models.CharField(db_column='LastBootedRecord', max_length=100, blank=True, null=True)  # Field name made lowercase.
    memorydynamicmax = models.BigIntegerField(db_column='MemoryDynamicMax', blank=True, null=True)  # Field name made lowercase.
    memorydynamicmin = models.BigIntegerField(db_column='MemoryDynamicMin', blank=True, null=True)  # Field name made lowercase.
    memoryoverhead = models.BigIntegerField(db_column='MemoryOverhead', blank=True, null=True)  # Field name made lowercase.
    memorystaticmax = models.BigIntegerField(db_column='MemoryStaticMax', blank=True, null=True)  # Field name made lowercase.
    memorystaticmin = models.BigIntegerField(db_column='MemoryStaticMin', blank=True, null=True)  # Field name made lowercase.
    memorytarget = models.BigIntegerField(db_column='MemoryTarget', blank=True, null=True)  # Field name made lowercase.
    order = models.BigIntegerField(db_column='Order', blank=True, null=True)  # Field name made lowercase.
    powerstate = models.CharField(db_column='PowerState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shutdowndelay = models.BigIntegerField(db_column='ShutdownDelay', blank=True, null=True)  # Field name made lowercase.
    startdelay = models.BigIntegerField(db_column='StartDelay', blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='Tags', max_length=300, blank=True, null=True)  # Field name made lowercase.
    userversion = models.BigIntegerField(db_column='UserVersion', blank=True, null=True)  # Field name made lowercase.
    version = models.BigIntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    installtime = models.DateTimeField(db_column='InstallTime', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixGuest'


class Tblcitrixguestextrainfo(models.Model):
    infoid = models.AutoField(db_column='InfoId', primary_key=True)  # Field name made lowercase.
    guestid = models.ForeignKey(Tblcitrixguest, models.DO_NOTHING, db_column='GuestId')  # Field name made lowercase.
    infotypeid = models.ForeignKey('Tblcitrixguestextrainfotypes', models.DO_NOTHING, db_column='InfoTypeId')  # Field name made lowercase.
    key = models.CharField(db_column='Key', max_length=150, blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixGuestExtraInfo'


class Tblcitrixguestextrainfotypes(models.Model):
    infotypeid = models.IntegerField(db_column='InfoTypeId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    isdictionary = models.BooleanField(db_column='IsDictionary')  # Field name made lowercase.
    extrainfotypeicon16 = models.CharField(db_column='ExtraInfoTypeIcon16', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixGuestExtraInfoTypes'


class Tblcitrixguestvirtualinterface(models.Model):
    guestvirtualinterfaceid = models.AutoField(db_column='GuestVirtualInterfaceId', primary_key=True)  # Field name made lowercase.
    guestid = models.ForeignKey(Tblcitrixguest, models.DO_NOTHING, db_column='GuestId')  # Field name made lowercase.
    interfaceid = models.IntegerField(db_column='InterfaceId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixGuestVirtualInterface'


class Tblcitrixhost(models.Model):
    hostid = models.AutoField(db_column='HostId', primary_key=True)  # Field name made lowercase.
    poolid = models.IntegerField(db_column='PoolId', blank=True, null=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    hostname = models.CharField(db_column='Hostname', max_length=150)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ismaster = models.BooleanField(db_column='IsMaster')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crashdumpstorageid = models.IntegerField(db_column='CrashDumpStorageID', blank=True, null=True)  # Field name made lowercase.
    edition = models.CharField(db_column='Edition', max_length=150, blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled', blank=True, null=True)  # Field name made lowercase.
    externalauthenticationservicename = models.CharField(db_column='ExternalAuthenticationServiceName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    externalauthenticationtype = models.CharField(db_column='ExternalAuthenticationType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    localcachestorageid = models.IntegerField(db_column='LocalCacheStorageId', blank=True, null=True)  # Field name made lowercase.
    memoryoverhead = models.BigIntegerField(db_column='MemoryOverhead', blank=True, null=True)  # Field name made lowercase.
    poweronmode = models.CharField(db_column='PowerOnMode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    schedulerpolicy = models.CharField(db_column='SchedulerPolicy', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ssllegacy = models.BooleanField(db_column='SslLegacy', blank=True, null=True)  # Field name made lowercase.
    suspendimagestorageid = models.IntegerField(db_column='SuspendImageStorageId', blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='Tags', max_length=300, blank=True, null=True)  # Field name made lowercase.
    display = models.CharField(db_column='Display', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated', blank=True, null=True)  # Field name made lowercase.
    live = models.BooleanField(db_column='Live', blank=True, null=True)  # Field name made lowercase.
    memoryfree = models.BigIntegerField(db_column='MemoryFree', blank=True, null=True)  # Field name made lowercase.
    memorytotal = models.BigIntegerField(db_column='MemoryTotal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixHost'


class Tblcitrixhostcrashdump(models.Model):
    dumpid = models.AutoField(db_column='DumpId', primary_key=True)  # Field name made lowercase.
    hostid = models.ForeignKey(Tblcitrixhost, models.DO_NOTHING, db_column='HostId')  # Field name made lowercase.
    size = models.BigIntegerField(db_column='Size')  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixHostCrashDump'


class Tblcitrixhostextrainfo(models.Model):
    infoid = models.AutoField(db_column='InfoId', primary_key=True)  # Field name made lowercase.
    hostid = models.ForeignKey(Tblcitrixhost, models.DO_NOTHING, db_column='HostId')  # Field name made lowercase.
    infotypeid = models.ForeignKey('Tblcitrixhostextrainfotypes', models.DO_NOTHING, db_column='InfoTypeId')  # Field name made lowercase.
    key = models.CharField(db_column='Key', max_length=150, blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixHostExtraInfo'


class Tblcitrixhostextrainfotypes(models.Model):
    infotypeid = models.IntegerField(db_column='InfoTypeId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    isdictionary = models.BooleanField(db_column='IsDictionary')  # Field name made lowercase.
    extrainfotypeicon16 = models.CharField(db_column='ExtraInfoTypeIcon16', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixHostExtraInfoTypes'


class Tblcitrixhostpatch(models.Model):
    patchid = models.AutoField(db_column='PatchId', primary_key=True)  # Field name made lowercase.
    hostid = models.ForeignKey(Tblcitrixhost, models.DO_NOTHING, db_column='HostId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150, blank=True, null=True)  # Field name made lowercase.
    size = models.BigIntegerField(db_column='Size')  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=30, blank=True, null=True)  # Field name made lowercase.
    applied = models.DateTimeField(db_column='Applied', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixHostPatch'


class Tblcitrixhostphysicalcpu(models.Model):
    cpuid = models.AutoField(db_column='CpuId', primary_key=True)  # Field name made lowercase.
    hostid = models.ForeignKey(Tblcitrixhost, models.DO_NOTHING, db_column='HostId')  # Field name made lowercase.
    family = models.BigIntegerField(db_column='Family')  # Field name made lowercase.
    features = models.CharField(db_column='Features', max_length=300, blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=300, blank=True, null=True)  # Field name made lowercase.
    model = models.BigIntegerField(db_column='Model')  # Field name made lowercase.
    modelname = models.CharField(db_column='ModelName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    numberofcpus = models.BigIntegerField(db_column='NumberOfCpus')  # Field name made lowercase.
    speed = models.BigIntegerField(db_column='Speed')  # Field name made lowercase.
    stepping = models.CharField(db_column='Stepping', max_length=150, blank=True, null=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixHostPhysicalCpu'


class Tblcitrixhostphysicalinterface(models.Model):
    hostphysicalinterfaceid = models.AutoField(db_column='HostPhysicalInterfaceId', primary_key=True)  # Field name made lowercase.
    hostid = models.ForeignKey(Tblcitrixhost, models.DO_NOTHING, db_column='HostId')  # Field name made lowercase.
    interfaceid = models.IntegerField(db_column='InterfaceId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixHostPhysicalInterface'


class Tblcitrixnetwork(models.Model):
    networkid = models.AutoField(db_column='NetworkId', primary_key=True)  # Field name made lowercase.
    poolid = models.ForeignKey('Tblcitrixpool', models.DO_NOTHING, db_column='PoolId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150, blank=True, null=True)  # Field name made lowercase.
    bridge = models.CharField(db_column='Bridge', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mtu = models.BigIntegerField(db_column='Mtu', blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='Tags', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixNetwork'


class Tblcitrixnetworkphysicalinterface(models.Model):
    networkphysicalinterfaceid = models.AutoField(db_column='NetworkPhysicalInterfaceId', primary_key=True)  # Field name made lowercase.
    networkid = models.ForeignKey(Tblcitrixnetwork, models.DO_NOTHING, db_column='NetworkId')  # Field name made lowercase.
    interfaceid = models.IntegerField(db_column='InterfaceId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixNetworkPhysicalInterface'


class Tblcitrixnetworkvirtualinterface(models.Model):
    networkvirtualinterfaceid = models.AutoField(db_column='NetworkVirtualInterfaceId', primary_key=True)  # Field name made lowercase.
    networkid = models.ForeignKey(Tblcitrixnetwork, models.DO_NOTHING, db_column='NetworkId')  # Field name made lowercase.
    interfaceid = models.IntegerField(db_column='InterfaceId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixNetworkVirtualInterface'


class Tblcitrixpci(models.Model):
    pciid = models.AutoField(db_column='PciId', primary_key=True)  # Field name made lowercase.
    hostid = models.ForeignKey(Tblcitrixhost, models.DO_NOTHING, db_column='HostId')  # Field name made lowercase.
    classname = models.CharField(db_column='ClassName', max_length=150)  # Field name made lowercase.
    devicename = models.CharField(db_column='DeviceName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    subsystemdevicename = models.CharField(db_column='SubsystemDeviceName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    subsystemvendorname = models.CharField(db_column='SubsystemVendorName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    vendorname = models.CharField(db_column='VendorName', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixPci'


class Tblcitrixphysicalblockdevice(models.Model):
    deviceid = models.AutoField(db_column='DeviceId', primary_key=True)  # Field name made lowercase.
    storageid = models.ForeignKey('Tblcitrixstorage', models.DO_NOTHING, db_column='StorageId')  # Field name made lowercase.
    currentlyattached = models.BooleanField(db_column='CurrentlyAttached')  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=150, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=150, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixPhysicalBlockDevice'


class Tblcitrixphysicalinterface(models.Model):
    interfaceid = models.AutoField(db_column='InterfaceId', primary_key=True)  # Field name made lowercase.
    poolid = models.ForeignKey('Tblcitrixpool', models.DO_NOTHING, db_column='PoolId', blank=True, null=True)  # Field name made lowercase.
    devicename = models.CharField(db_column='DeviceName', max_length=150)  # Field name made lowercase.
    mac = models.CharField(db_column='Mac', max_length=50)  # Field name made lowercase.
    mtu = models.BigIntegerField(db_column='Mtu', blank=True, null=True)  # Field name made lowercase.
    speed = models.BigIntegerField(db_column='Speed', blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='Ip', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dns = models.CharField(db_column='Dns', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gateway = models.CharField(db_column='Gateway', max_length=50, blank=True, null=True)  # Field name made lowercase.
    netmask = models.CharField(db_column='Netmask', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated', blank=True, null=True)  # Field name made lowercase.
    currentlyattached = models.BooleanField(db_column='CurrentlyAttached', blank=True, null=True)  # Field name made lowercase.
    disallowunplug = models.BooleanField(db_column='DisallowUnplug', blank=True, null=True)  # Field name made lowercase.
    ipv6 = models.CharField(db_column='IpV6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    device = models.CharField(db_column='Device', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ipconfigurationmode = models.CharField(db_column='IpConfigurationMode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ipv6configurationmode = models.CharField(db_column='IpV6ConfigurationMode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ipv6gateway = models.CharField(db_column='IpV6Gateway', max_length=50, blank=True, null=True)  # Field name made lowercase.
    managed = models.BooleanField(db_column='Managed', blank=True, null=True)  # Field name made lowercase.
    management = models.BooleanField(db_column='Management', blank=True, null=True)  # Field name made lowercase.
    physical = models.BooleanField(db_column='Physical', blank=True, null=True)  # Field name made lowercase.
    primaryaddresstype = models.CharField(db_column='PrimaryAddressType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    carier = models.BooleanField(db_column='Carier', blank=True, null=True)  # Field name made lowercase.
    duplex = models.BooleanField(db_column='Duplex', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pcibuspath = models.CharField(db_column='PciBusPath', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendorid = models.CharField(db_column='VendorId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendorname = models.CharField(db_column='VendorName', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixPhysicalInterface'


class Tblcitrixpool(models.Model):
    poolid = models.AutoField(db_column='PoolId', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cpucount = models.IntegerField(db_column='CpuCount', blank=True, null=True)  # Field name made lowercase.
    socketcount = models.IntegerField(db_column='SocketCount', blank=True, null=True)  # Field name made lowercase.
    cpuvendor = models.CharField(db_column='CpuVendor', max_length=150, blank=True, null=True)  # Field name made lowercase.
    defaultstorageid = models.IntegerField(db_column='DefaultStorageId', blank=True, null=True)  # Field name made lowercase.
    crashdumpstorageid = models.IntegerField(db_column='CrashDumpStorageId', blank=True, null=True)  # Field name made lowercase.
    livepatching = models.BooleanField(db_column='LivePatching', blank=True, null=True)  # Field name made lowercase.
    policynovendordevice = models.BooleanField(db_column='PolicyNoVendorDevice', blank=True, null=True)  # Field name made lowercase.
    redolog = models.BooleanField(db_column='RedoLog', blank=True, null=True)  # Field name made lowercase.
    suspendimagestorageid = models.IntegerField(db_column='SuspendImageStorageId', blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='Tags', max_length=300, blank=True, null=True)  # Field name made lowercase.
    vswitchcontroller = models.CharField(db_column='VSwitchController', max_length=150, blank=True, null=True)  # Field name made lowercase.
    highavailability = models.BooleanField(db_column='HighAvailability', blank=True, null=True)  # Field name made lowercase.
    highavailabilityallowovercommit = models.BooleanField(db_column='HighAvailabilityAllowOvercommit', blank=True, null=True)  # Field name made lowercase.
    highavailabilityovercommitted = models.BooleanField(db_column='HighAvailabilityOvercommitted', blank=True, null=True)  # Field name made lowercase.
    highavailabilityhostfailurestotolerate = models.BigIntegerField(db_column='HighAvailabilityHostFailuresToTolerate', blank=True, null=True)  # Field name made lowercase.
    highavailabilityplanexistsfor = models.BigIntegerField(db_column='HighAvailabilityPlanExistsFor', blank=True, null=True)  # Field name made lowercase.
    highavailabilityclusterstack = models.CharField(db_column='HighAvailabilityClusterStack', max_length=150, blank=True, null=True)  # Field name made lowercase.
    workloadbalancing = models.BooleanField(db_column='WorkloadBalancing', blank=True, null=True)  # Field name made lowercase.
    workloadbalancingurl = models.CharField(db_column='WorkloadBalancingUrl', max_length=150, blank=True, null=True)  # Field name made lowercase.
    workloadbalancingusername = models.CharField(db_column='WorkloadBalancingUsername', max_length=150, blank=True, null=True)  # Field name made lowercase.
    workloadbalancingverifycert = models.BooleanField(db_column='WorkloadBalancingVerifyCert', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixPool'


class Tblcitrixpoolotherconfiguration(models.Model):
    configid = models.AutoField(db_column='ConfigId', primary_key=True)  # Field name made lowercase.
    poolid = models.ForeignKey(Tblcitrixpool, models.DO_NOTHING, db_column='PoolId')  # Field name made lowercase.
    key = models.CharField(db_column='Key', max_length=150)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=150, blank=True, null=True)  # Field name made lowercase.
    iscustomfield = models.BooleanField(db_column='IsCustomField')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixPoolOtherConfiguration'


class Tblcitrixpoolpatch(models.Model):
    patchid = models.AutoField(db_column='PatchId', primary_key=True)  # Field name made lowercase.
    poolid = models.ForeignKey(Tblcitrixpool, models.DO_NOTHING, db_column='PoolId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150, blank=True, null=True)  # Field name made lowercase.
    size = models.BigIntegerField(db_column='Size')  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=30, blank=True, null=True)  # Field name made lowercase.
    afterapplyguidance = models.CharField(db_column='AfterApplyGuidance', max_length=150, blank=True, null=True)  # Field name made lowercase.
    applied = models.BooleanField(db_column='Applied')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixPoolPatch'


class Tblcitrixpoolrestriction(models.Model):
    restrictionid = models.AutoField(db_column='RestrictionId', primary_key=True)  # Field name made lowercase.
    poolid = models.ForeignKey(Tblcitrixpool, models.DO_NOTHING, db_column='PoolId')  # Field name made lowercase.
    key = models.CharField(db_column='Key', max_length=150)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixPoolRestriction'


class Tblcitrixstorage(models.Model):
    storageid = models.AutoField(db_column='StorageId', primary_key=True)  # Field name made lowercase.
    hostid = models.ForeignKey(Tblcitrixhost, models.DO_NOTHING, db_column='HostId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150, blank=True, null=True)  # Field name made lowercase.
    physicalsize = models.BigIntegerField(db_column='PhysicalSize', blank=True, null=True)  # Field name made lowercase.
    physicalutilization = models.BigIntegerField(db_column='PhysicalUtilization', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=15, blank=True, null=True)  # Field name made lowercase.
    contenttype = models.CharField(db_column='ContentType', max_length=15, blank=True, null=True)  # Field name made lowercase.
    clustered = models.BooleanField(db_column='Clustered', blank=True, null=True)  # Field name made lowercase.
    istoolsstorage = models.BooleanField(db_column='IsToolsStorage', blank=True, null=True)  # Field name made lowercase.
    localcache = models.BooleanField(db_column='LocalCache', blank=True, null=True)  # Field name made lowercase.
    shared = models.BooleanField(db_column='Shared', blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='Tags', max_length=300, blank=True, null=True)  # Field name made lowercase.
    virtualallocation = models.BigIntegerField(db_column='VirtualAllocation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixStorage'


class Tblcitrixtemplate(models.Model):
    templateid = models.AutoField(db_column='TemplateId', primary_key=True)  # Field name made lowercase.
    poolid = models.ForeignKey(Tblcitrixpool, models.DO_NOTHING, db_column='PoolId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixTemplate'


class Tblcitrixuser(models.Model):
    userid = models.AutoField(db_column='UserId', primary_key=True)  # Field name made lowercase.
    poolid = models.ForeignKey(Tblcitrixpool, models.DO_NOTHING, db_column='PoolId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixUser'


class Tblcitrixvirtualblockdevice(models.Model):
    deviceid = models.AutoField(db_column='DeviceId', primary_key=True)  # Field name made lowercase.
    guestid = models.ForeignKey(Tblcitrixguest, models.DO_NOTHING, db_column='GuestId')  # Field name made lowercase.
    diskimageid = models.IntegerField(db_column='DiskImageId', blank=True, null=True)  # Field name made lowercase.
    bootable = models.BooleanField(db_column='Bootable', blank=True, null=True)  # Field name made lowercase.
    currentlyattached = models.BooleanField(db_column='CurrentlyAttached', blank=True, null=True)  # Field name made lowercase.
    device = models.CharField(db_column='Device', max_length=50, blank=True, null=True)  # Field name made lowercase.
    empty = models.BooleanField(db_column='Empty', blank=True, null=True)  # Field name made lowercase.
    mode = models.CharField(db_column='Mode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qosalgorithmparameters = models.CharField(db_column='QosAlgorithmParameters', max_length=300, blank=True, null=True)  # Field name made lowercase.
    qosalgorithmtype = models.CharField(db_column='QosAlgorithmType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    qossupportedalgorithms = models.CharField(db_column='QosSupportedAlgorithms', max_length=300, blank=True, null=True)  # Field name made lowercase.
    runtimeproperties = models.CharField(db_column='RuntimeProperties', max_length=300, blank=True, null=True)  # Field name made lowercase.
    statuscode = models.BigIntegerField(db_column='StatusCode', blank=True, null=True)  # Field name made lowercase.
    statusdetails = models.CharField(db_column='StatusDetails', max_length=300, blank=True, null=True)  # Field name made lowercase.
    storagelock = models.BooleanField(db_column='StorageLock', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    unpluggable = models.BooleanField(db_column='Unpluggable', blank=True, null=True)  # Field name made lowercase.
    userdevice = models.CharField(db_column='UserDevice', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixVirtualBlockDevice'


class Tblcitrixvirtualdiskimage(models.Model):
    diskimageid = models.AutoField(db_column='DiskImageId', primary_key=True)  # Field name made lowercase.
    storageid = models.ForeignKey(Tblcitrixstorage, models.DO_NOTHING, db_column='StorageId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150, blank=True, null=True)  # Field name made lowercase.
    allowcaching = models.BooleanField(db_column='AllowCaching', blank=True, null=True)  # Field name made lowercase.
    isasnapshot = models.BooleanField(db_column='IsASnapshot', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=150, blank=True, null=True)  # Field name made lowercase.
    managed = models.BooleanField(db_column='Managed', blank=True, null=True)  # Field name made lowercase.
    metadatalatest = models.BooleanField(db_column='MetadataLatest', blank=True, null=True)  # Field name made lowercase.
    missing = models.BooleanField(db_column='Missing', blank=True, null=True)  # Field name made lowercase.
    onboot = models.CharField(db_column='OnBoot', max_length=50, blank=True, null=True)  # Field name made lowercase.
    physicalutilisation = models.BigIntegerField(db_column='PhysicalUtilisation', blank=True, null=True)  # Field name made lowercase.
    readonly = models.BooleanField(db_column='ReadOnly', blank=True, null=True)  # Field name made lowercase.
    sharable = models.BooleanField(db_column='Sharable', blank=True, null=True)  # Field name made lowercase.
    storagelock = models.BooleanField(db_column='StorageLock', blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='Tags', max_length=300, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    virtualsize = models.BigIntegerField(db_column='VirtualSize', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixVirtualDiskImage'


class Tblcitrixvirtualinterface(models.Model):
    interfaceid = models.AutoField(db_column='InterfaceId', primary_key=True)  # Field name made lowercase.
    poolid = models.ForeignKey(Tblcitrixpool, models.DO_NOTHING, db_column='PoolId', blank=True, null=True)  # Field name made lowercase.
    device = models.CharField(db_column='Device', max_length=150)  # Field name made lowercase.
    mac = models.CharField(db_column='Mac', max_length=50)  # Field name made lowercase.
    mtu = models.BigIntegerField(db_column='Mtu', blank=True, null=True)  # Field name made lowercase.
    macautogenerated = models.BooleanField(db_column='MacAutoGenerated', blank=True, null=True)  # Field name made lowercase.
    gateway = models.CharField(db_column='Gateway', max_length=50, blank=True, null=True)  # Field name made lowercase.
    statuscode = models.BigIntegerField(db_column='StatusCode', blank=True, null=True)  # Field name made lowercase.
    statusdetails = models.CharField(db_column='StatusDetails', max_length=150, blank=True, null=True)  # Field name made lowercase.
    currentlyattached = models.BooleanField(db_column='CurrentlyAttached', blank=True, null=True)  # Field name made lowercase.
    qosalgorithmtype = models.CharField(db_column='QosAlgorithmType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qosalgorithms = models.CharField(db_column='QosAlgorithms', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lockingmode = models.CharField(db_column='LockingMode', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixVirtualInterface'


class Tblcitrixvirtualinterfaceaddress(models.Model):
    addressid = models.AutoField(db_column='AddressId', primary_key=True)  # Field name made lowercase.
    interfaceid = models.ForeignKey(Tblcitrixvirtualinterface, models.DO_NOTHING, db_column='InterfaceId')  # Field name made lowercase.
    ipversion = models.IntegerField(db_column='IpVersion')  # Field name made lowercase.
    ip = models.CharField(db_column='Ip', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCitrixVirtualInterfaceAddress'


class Tblcloudlogging(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    level = models.CharField(db_column='Level', max_length=10)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=4000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCloudLogging'


class Tblcodecfile(models.Model):
    win32_codecfileid = models.AutoField(db_column='Win32_CodecFileid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    archive = models.BooleanField(db_column='Archive', blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    compressed = models.BooleanField(db_column='Compressed', blank=True, null=True)  # Field name made lowercase.
    compressionmethod = models.CharField(db_column='CompressionMethod', max_length=200, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    drive = models.CharField(db_column='Drive', max_length=20, blank=True, null=True)  # Field name made lowercase.
    encrypted = models.BooleanField(db_column='Encrypted', blank=True, null=True)  # Field name made lowercase.
    encryptionmethod = models.CharField(db_column='EncryptionMethod', max_length=100, blank=True, null=True)  # Field name made lowercase.
    extension = models.CharField(db_column='Extension', max_length=50, blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    filesize = models.DecimalField(db_column='FileSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    filetype = models.CharField(db_column='FileType', max_length=300, blank=True, null=True)  # Field name made lowercase.
    fsname = models.CharField(db_column='FSName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    installdate = models.DateTimeField(db_column='InstallDate', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    system = models.BooleanField(db_column='System', blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblCodecFile'


class Tblcodecfilehist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    archive = models.BooleanField(db_column='Archive', blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    compressed = models.BooleanField(db_column='Compressed', blank=True, null=True)  # Field name made lowercase.
    compressionmethod = models.CharField(db_column='CompressionMethod', max_length=200, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    drive = models.CharField(db_column='Drive', max_length=20, blank=True, null=True)  # Field name made lowercase.
    encrypted = models.BooleanField(db_column='Encrypted', blank=True, null=True)  # Field name made lowercase.
    encryptionmethod = models.CharField(db_column='EncryptionMethod', max_length=100, blank=True, null=True)  # Field name made lowercase.
    extension = models.CharField(db_column='Extension', max_length=50, blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    filesize = models.DecimalField(db_column='FileSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    filetype = models.CharField(db_column='FileType', max_length=300, blank=True, null=True)  # Field name made lowercase.
    fsname = models.CharField(db_column='FSName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    installdate = models.DateTimeField(db_column='InstallDate', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    system = models.BooleanField(db_column='System', blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField()
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCodecFilehist'


class Tblcomponentcategory(models.Model):
    win32_componentcategoryid = models.AutoField(db_column='Win32_ComponentCategoryid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    categoryid = models.CharField(db_column='CategoryId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblComponentCategory'


class Tblcomponentcategoryhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    categoryid = models.CharField(db_column='CategoryId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblComponentCategoryHist'


class Tblcomputersystemproduct(models.Model):
    win32_computersystemproductid = models.AutoField(db_column='Win32_ComputerSystemProductid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    uuid = models.CharField(db_column='UUID', max_length=450, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblComputerSystemProduct'


class Tblcomputersystemproducthist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    uuid = models.CharField(db_column='UUID', max_length=450, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblComputerSystemProductHist'


class Tblcomputersystem(models.Model):
    computersystemid = models.AutoField(db_column='ComputersystemID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    adminpasswordstatus = models.DecimalField(db_column='AdminPasswordStatus', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    automaticresetbootoption = models.BooleanField(db_column='AutomaticResetBootOption', blank=True, null=True)  # Field name made lowercase.
    automaticresetcapability = models.BooleanField(db_column='AutomaticResetCapability', blank=True, null=True)  # Field name made lowercase.
    bootoptiononlimit = models.DecimalField(db_column='BootOptionOnLimit', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bootoptiononwatchdog = models.DecimalField(db_column='BootoptionOnWatchDog', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bootromsupported = models.BooleanField(db_column='BootRomSupported', blank=True, null=True)  # Field name made lowercase.
    chassisbootupstate = models.DecimalField(db_column='ChassisBootupState', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    currenttimezone = models.DecimalField(db_column='CurrentTimeZone', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    daylightineffect = models.BooleanField(db_column='DaylightInEffect', blank=True, null=True)  # Field name made lowercase.
    domainrole = models.ForeignKey('Tbldomainroles', models.DO_NOTHING, db_column='Domainrole', blank=True, null=True)  # Field name made lowercase.
    enabledaylightsavingstime = models.BooleanField(db_column='EnableDaylightSavingsTime', blank=True, null=True)  # Field name made lowercase.
    frontpanelresetstatus = models.DecimalField(db_column='FrontPanelResetStatus', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    infraredsupported = models.BooleanField(db_column='Infraredsupported', blank=True, null=True)  # Field name made lowercase.
    keyboardpasswordstatus = models.DecimalField(db_column='KeyboardPasswordStatus', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    networkservermodeenabled = models.BooleanField(db_column='NetworkServerModeEnabled', blank=True, null=True)  # Field name made lowercase.
    numberoflogicalprocessors = models.DecimalField(db_column='NumberOfLogicalProcessors', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    numberofprocessors = models.DecimalField(db_column='NumberOfProcessors', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    partofdomain = models.BooleanField(db_column='PartOfDomain', blank=True, null=True)  # Field name made lowercase.
    pauseafterreset = models.DecimalField(db_column='PauseAfterReset', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    poweronpasswordstatus = models.DecimalField(db_column='PowerOnPasswordStatus', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    powerstate = models.DecimalField(db_column='Powerstate', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    powersupplystate = models.DecimalField(db_column='PowerSupplyState', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    resetcapability = models.DecimalField(db_column='ResetCapability', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    resetcount = models.DecimalField(db_column='ResetCount', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    resetlimit = models.DecimalField(db_column='Resetlimit', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    roles = models.CharField(db_column='Roles', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    systemstartupdelay = models.DecimalField(db_column='SystemStartupDelay', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    systemstartupsetting = models.DecimalField(db_column='SystemStartupSetting', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    systemtype = models.CharField(db_column='SystemType', max_length=450, blank=True, null=True)  # Field name made lowercase.
    thermalstate = models.DecimalField(db_column='ThermalState', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    totalphysicalmemory = models.DecimalField(db_column='TotalPhysicalMemory', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    wakeuptype = models.DecimalField(db_column='Wakeuptype', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblComputersystem'


class Tblcomputersystemhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    adminpasswordstatus = models.DecimalField(db_column='AdminPasswordStatus', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    automaticresetbootoption = models.BooleanField(db_column='AutomaticResetBootOption', blank=True, null=True)  # Field name made lowercase.
    automaticresetcapability = models.BooleanField(db_column='AutomaticResetCapability', blank=True, null=True)  # Field name made lowercase.
    bootoptiononlimit = models.DecimalField(db_column='BootOptionOnLimit', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bootoptiononwatchdog = models.DecimalField(db_column='BootoptionOnWatchDog', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bootromsupported = models.BooleanField(db_column='BootRomSupported', blank=True, null=True)  # Field name made lowercase.
    chassisbootupstate = models.DecimalField(db_column='ChassisBootupState', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    currenttimezone = models.DecimalField(db_column='CurrentTimeZone', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    daylightineffect = models.BooleanField(db_column='DaylightInEffect', blank=True, null=True)  # Field name made lowercase.
    domainrole = models.IntegerField(db_column='Domainrole', blank=True, null=True)  # Field name made lowercase.
    enabledaylightsavingstime = models.BooleanField(db_column='EnableDaylightSavingsTime', blank=True, null=True)  # Field name made lowercase.
    frontpanelresetstatus = models.DecimalField(db_column='FrontPanelResetStatus', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    infraredsupported = models.BooleanField(db_column='Infraredsupported', blank=True, null=True)  # Field name made lowercase.
    keyboardpasswordstatus = models.DecimalField(db_column='KeyboardPasswordStatus', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    networkservermodeenabled = models.BooleanField(db_column='NetworkServerModeEnabled', blank=True, null=True)  # Field name made lowercase.
    numberoflogicalprocessors = models.DecimalField(db_column='NumberOfLogicalProcessors', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    numberofprocessors = models.DecimalField(db_column='NumberOfProcessors', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    partofdomain = models.BooleanField(db_column='PartOfDomain', blank=True, null=True)  # Field name made lowercase.
    pauseafterreset = models.DecimalField(db_column='PauseAfterReset', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    poweronpasswordstatus = models.DecimalField(db_column='PowerOnPasswordStatus', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    powerstate = models.DecimalField(db_column='Powerstate', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    powersupplystate = models.DecimalField(db_column='PowerSupplyState', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    resetcapability = models.DecimalField(db_column='ResetCapability', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    resetcount = models.DecimalField(db_column='ResetCount', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    resetlimit = models.DecimalField(db_column='Resetlimit', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    roles = models.CharField(db_column='Roles', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    systemstartupdelay = models.DecimalField(db_column='SystemStartupDelay', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    systemstartupsetting = models.DecimalField(db_column='SystemStartupSetting', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    systemtype = models.CharField(db_column='SystemType', max_length=450, blank=True, null=True)  # Field name made lowercase.
    thermalstate = models.DecimalField(db_column='ThermalState', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    totalphysicalmemory = models.DecimalField(db_column='TotalPhysicalMemory', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    wakeuptype = models.DecimalField(db_column='Wakeuptype', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblComputersystemHist'


class Tblconfiglog(models.Model):
    logid = models.AutoField(db_column='LogID', primary_key=True)  # Field name made lowercase.
    actionid = models.IntegerField(db_column='ActionID')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500)  # Field name made lowercase.
    oldvalue = models.CharField(db_column='OldValue', max_length=500, blank=True, null=True)  # Field name made lowercase.
    newvalue = models.CharField(db_column='NewValue', max_length=500, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    displayname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblConfigLog'


class Tblcustdevprinter(models.Model):
    devprintid = models.AutoField(db_column='DevprintID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    tonernr = models.DecimalField(db_column='Tonernr', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tonername = models.CharField(db_column='Tonername', max_length=150, blank=True, null=True)  # Field name made lowercase.
    tonercolorname = models.CharField(db_column='TonerColorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tonercolornr = models.DecimalField(db_column='TonerColorNr', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tonermaximum = models.DecimalField(db_column='TonerMaximum', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tonerremaining = models.DecimalField(db_column='TonerRemaining', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCustDevPrinter'


class Tbldcomapplication(models.Model):
    win32_dcomapplicationid = models.AutoField(db_column='Win32_DCOMApplicationid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDCOMApplication'


class Tbldcomapplicationhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDCOMApplicationHist'


class Tbldesktop(models.Model):
    win32_desktopid = models.AutoField(db_column='Win32_Desktopid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    borderwidth = models.DecimalField(db_column='BorderWidth', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    coolswitch = models.BooleanField(db_column='CoolSwitch', blank=True, null=True)  # Field name made lowercase.
    cursorblinkrate = models.DecimalField(db_column='CursorBlinkRate', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dragfullwindows = models.BooleanField(db_column='DragFullWindows', blank=True, null=True)  # Field name made lowercase.
    gridgranularity = models.DecimalField(db_column='GridGranularity', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    iconspacing = models.DecimalField(db_column='IconSpacing', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    icontitlefacename = models.CharField(db_column='IconTitleFaceName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    icontitlesize = models.DecimalField(db_column='IconTitleSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    icontitlewrap = models.BooleanField(db_column='IconTitleWrap', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=450, blank=True, null=True)  # Field name made lowercase.
    pattern = models.CharField(db_column='Pattern', max_length=450, blank=True, null=True)  # Field name made lowercase.
    screensaveractive = models.BooleanField(db_column='ScreenSaverActive', blank=True, null=True)  # Field name made lowercase.
    screensaverexecutable = models.CharField(db_column='ScreenSaverExecutable', max_length=450, blank=True, null=True)  # Field name made lowercase.
    screensaversecure = models.BooleanField(db_column='ScreenSaverSecure', blank=True, null=True)  # Field name made lowercase.
    screensavertimeout = models.DecimalField(db_column='ScreenSaverTimeout', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    wallpaper = models.CharField(db_column='Wallpaper', max_length=450, blank=True, null=True)  # Field name made lowercase.
    wallpaperstretched = models.BooleanField(db_column='WallpaperStretched', blank=True, null=True)  # Field name made lowercase.
    wallpapertiled = models.BooleanField(db_column='WallpaperTiled', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDesktop'


class Tbldesktopmonitor(models.Model):
    win32_desktopmonitorid = models.AutoField(db_column='Win32_DesktopMonitorid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    availability = models.DecimalField(db_column='Availability', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=450, blank=True, null=True)  # Field name made lowercase.
    monitormanufacturer = models.CharField(db_column='MonitorManufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    pixelsperxlogicalinch = models.DecimalField(db_column='PixelsPerXLogicalInch', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pixelsperylogicalinch = models.DecimalField(db_column='PixelsPerYLogicalInch', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    screenheight = models.DecimalField(db_column='ScreenHeight', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    screenwidth = models.DecimalField(db_column='ScreenWidth', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    pnpdeviceid = models.CharField(db_column='PNPDeviceID', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDesktopMonitor'


class Tbldesktopmonitorhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    availability = models.DecimalField(db_column='Availability', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=450, blank=True, null=True)  # Field name made lowercase.
    monitormanufacturer = models.CharField(db_column='MonitorManufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    pixelsperxlogicalinch = models.DecimalField(db_column='PixelsPerXLogicalInch', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pixelsperylogicalinch = models.DecimalField(db_column='PixelsPerYLogicalInch', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    screenheight = models.DecimalField(db_column='ScreenHeight', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    screenwidth = models.DecimalField(db_column='ScreenWidth', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.
    pnpdeviceid = models.CharField(db_column='PNPDeviceID', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDesktopMonitorHist'


class Tbldevicefingerprint(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', max_length=20)  # Field name made lowercase.
    protocol = models.IntegerField(db_column='Protocol')  # Field name made lowercase.
    isdirty = models.BooleanField(db_column='IsDirty')  # Field name made lowercase.
    messagetype = models.IntegerField(db_column='MessageType')  # Field name made lowercase.
    data = models.TextField(db_column='Data')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDeviceFingerPrint'


class Tbldevicerecognition(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', unique=True, max_length=20)  # Field name made lowercase.
    recognitiondate = models.DateTimeField(db_column='RecognitionDate')  # Field name made lowercase.
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    recogtype = models.CharField(db_column='RecogType', max_length=64, blank=True, null=True)  # Field name made lowercase.
    macvendor = models.CharField(db_column='MacVendor', max_length=64, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=64, blank=True, null=True)  # Field name made lowercase.
    osname = models.CharField(db_column='OsName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    osbuild = models.CharField(db_column='OsBuild', max_length=64, blank=True, null=True)  # Field name made lowercase.
    osversion = models.CharField(db_column='OsVersion', max_length=64, blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=64, blank=True, null=True)  # Field name made lowercase.
    type = models.ForeignKey('Tsysassettypes', models.DO_NOTHING, db_column='Type')  # Field name made lowercase.
    typename = models.CharField(db_column='TypeName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    typegroupname = models.CharField(db_column='TypeGroupName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    serial = models.CharField(db_column='Serial', max_length=100, blank=True, null=True)  # Field name made lowercase.
    typeid = models.BigIntegerField(db_column='TypeId', blank=True, null=True)  # Field name made lowercase.
    brandid = models.BigIntegerField(db_column='BrandId', blank=True, null=True)  # Field name made lowercase.
    modelid = models.BigIntegerField(db_column='ModelId', blank=True, null=True)  # Field name made lowercase.
    osid = models.BigIntegerField(db_column='OsId', blank=True, null=True)  # Field name made lowercase.
    hwcpe = models.CharField(db_column='HwCpe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fwcpe = models.CharField(db_column='FwCpe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oscpe = models.CharField(db_column='OsCpe', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDeviceRecognition'


class Tbldiskpartition(models.Model):
    win32_diskpartitionid = models.AutoField(db_column='Win32_DiskPartitionid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    blocksize = models.DecimalField(db_column='BlockSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bootable = models.BooleanField(db_column='Bootable', blank=True, null=True)  # Field name made lowercase.
    bootpartition = models.BooleanField(db_column='BootPartition', blank=True, null=True)  # Field name made lowercase.
    diskindex = models.DecimalField(db_column='DiskIndex', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    index = models.DecimalField(db_column='Index', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    numberofblocks = models.DecimalField(db_column='NumberOfBlocks', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    primarypartition = models.BooleanField(db_column='PrimaryPartition', blank=True, null=True)  # Field name made lowercase.
    size = models.DecimalField(db_column='Size', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    startingoffset = models.DecimalField(db_column='StartingOffset', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDiskPartition'


class Tbldiskpartitionhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    blocksize = models.DecimalField(db_column='BlockSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bootable = models.BooleanField(db_column='Bootable', blank=True, null=True)  # Field name made lowercase.
    bootpartition = models.BooleanField(db_column='BootPartition', blank=True, null=True)  # Field name made lowercase.
    diskindex = models.DecimalField(db_column='DiskIndex', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    index = models.DecimalField(db_column='Index', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    numberofblocks = models.DecimalField(db_column='NumberOfBlocks', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    primarypartition = models.BooleanField(db_column='PrimaryPartition', blank=True, null=True)  # Field name made lowercase.
    size = models.DecimalField(db_column='Size', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    startingoffset = models.DecimalField(db_column='StartingOffset', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDiskPartitionHist'


class Tbldiskdrives(models.Model):
    diskid = models.AutoField(db_column='diskID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=20, blank=True, null=True)  # Field name made lowercase.
    compressed = models.BooleanField(db_column='Compressed', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=450, blank=True, null=True)  # Field name made lowercase.
    drivetype = models.DecimalField(db_column='DriveType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    filesystem = models.CharField(db_column='FileSystem', max_length=50, blank=True, null=True)  # Field name made lowercase.
    freespace = models.DecimalField(db_column='Freespace', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    size = models.DecimalField(db_column='Size', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    volumename = models.CharField(db_column='Volumename', max_length=300, blank=True, null=True)  # Field name made lowercase.
    volumeserialnumber = models.CharField(db_column='Volumeserialnumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDiskdrives'


class Tbldisplayconfiguration(models.Model):
    win32_displayconfigurationid = models.AutoField(db_column='Win32_DisplayConfigurationid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    bitsperpel = models.DecimalField(db_column='BitsPerPel', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    displayflags = models.DecimalField(db_column='DisplayFlags', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    displayfrequency = models.DecimalField(db_column='DisplayFrequency', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    driverversion = models.CharField(db_column='DriverVersion', max_length=450, blank=True, null=True)  # Field name made lowercase.
    logpixels = models.DecimalField(db_column='LogPixels', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pelsheight = models.DecimalField(db_column='PelsHeight', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pelswidth = models.DecimalField(db_column='PelsWidth', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    specificationversion = models.DecimalField(db_column='SpecificationVersion', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblDisplayConfiguration'


class Tbldisplayconfigurationhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    bitsperpel = models.DecimalField(db_column='BitsPerPel', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    displayflags = models.DecimalField(db_column='DisplayFlags', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    displayfrequency = models.DecimalField(db_column='DisplayFrequency', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    driverversion = models.CharField(db_column='DriverVersion', max_length=450, blank=True, null=True)  # Field name made lowercase.
    logpixels = models.DecimalField(db_column='LogPixels', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pelsheight = models.DecimalField(db_column='PelsHeight', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pelswidth = models.DecimalField(db_column='PelsWidth', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    specificationversion = models.DecimalField(db_column='SpecificationVersion', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField()
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDisplayConfigurationHist'


class Tbldisplaycontrollerconfiguration(models.Model):
    win32_displaycontrollerconfigurationid = models.AutoField(db_column='Win32_DisplayControllerConfigurationid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    bitsperpixel = models.DecimalField(db_column='BitsPerPixel', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    colorplanes = models.DecimalField(db_column='ColorPlanes', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    deviceentriesinacolortable = models.DecimalField(db_column='DeviceEntriesInAColorTable', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    devicespecificpens = models.DecimalField(db_column='DeviceSpecificPens', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    horizontalresolution = models.DecimalField(db_column='HorizontalResolution', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    refreshrate = models.DecimalField(db_column='RefreshRate', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    verticalresolution = models.DecimalField(db_column='VerticalResolution', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    videomode = models.CharField(db_column='VideoMode', max_length=300, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDisplayControllerConfiguration'


class Tbldisplaycontrollerconfigurationhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    bitsperpixel = models.DecimalField(db_column='BitsPerPixel', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    colorplanes = models.DecimalField(db_column='ColorPlanes', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    deviceentriesinacolortable = models.DecimalField(db_column='DeviceEntriesInAColorTable', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    devicespecificpens = models.DecimalField(db_column='DeviceSpecificPens', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    horizontalresolution = models.DecimalField(db_column='HorizontalResolution', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    refreshrate = models.DecimalField(db_column='RefreshRate', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    verticalresolution = models.DecimalField(db_column='VerticalResolution', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    videomode = models.CharField(db_column='VideoMode', max_length=300, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDisplayControllerConfigurationHist'


class Tbldomainroles(models.Model):
    domainrole = models.IntegerField(db_column='Domainrole', primary_key=True)  # Field name made lowercase.
    domainrolename = models.CharField(db_column='Domainrolename', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDomainroles'


class Tblencryptablevolume(models.Model):
    win32_encryptablevolumeid = models.AutoField(db_column='Win32_EncryptableVolumeId', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    driveletter = models.CharField(db_column='DriveLetter', max_length=50, blank=True, null=True)  # Field name made lowercase.
    protectionstatus = models.IntegerField(db_column='ProtectionStatus', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblEncryptableVolume'


class Tblenvironment(models.Model):
    win32_environmentid = models.AutoField(db_column='Win32_Environmentid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=450, blank=True, null=True)  # Field name made lowercase.
    systemvariable = models.BooleanField(db_column='SystemVariable', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    variablevalue = models.CharField(db_column='VariableValue', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblEnvironment'


class Tblerrors(models.Model):
    teller = models.AutoField(db_column='Teller', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    cfgname = models.CharField(db_column='CFGname', max_length=20, blank=True, null=True)  # Field name made lowercase.
    errortext = models.CharField(db_column='ErrorText', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    errortype = models.ForeignKey('Tsysasseterrortypes', models.DO_NOTHING, db_column='ErrorType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblErrors'


class Tblexchangeactivesyncdevice(models.Model):
    activesyncdeviceid = models.AutoField(db_column='ActiveSyncDeviceId', primary_key=True)  # Field name made lowercase.
    serverid = models.ForeignKey('Tblexchangeserver', models.DO_NOTHING, db_column='ServerId')  # Field name made lowercase.
    clienttype = models.CharField(db_column='ClientType', max_length=150, blank=True, null=True)  # Field name made lowercase.
    deviceaccesscontrolrule = models.CharField(db_column='DeviceAccessControlRule', max_length=150, blank=True, null=True)  # Field name made lowercase.
    deviceaccessstate = models.CharField(db_column='DeviceAccessState', max_length=150, blank=True, null=True)  # Field name made lowercase.
    deviceaccessstatereason = models.CharField(db_column='DeviceAccessStateReason', max_length=256, blank=True, null=True)  # Field name made lowercase.
    deviceactivesyncversion = models.CharField(db_column='DeviceActiveSyncVersion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    devicefriendlyname = models.CharField(db_column='DeviceFriendlyName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    devicemodel = models.CharField(db_column='DeviceModel', max_length=256, blank=True, null=True)  # Field name made lowercase.
    deviceos = models.CharField(db_column='DeviceOs', max_length=256, blank=True, null=True)  # Field name made lowercase.
    devicepolicyapplicationstatus = models.CharField(db_column='DevicePolicyApplicationStatus', max_length=150, blank=True, null=True)  # Field name made lowercase.
    devicetype = models.CharField(db_column='DeviceType', max_length=256, blank=True, null=True)  # Field name made lowercase.
    deviceuseragent = models.CharField(db_column='DeviceUserAgent', max_length=500, blank=True, null=True)  # Field name made lowercase.
    devicewiperequesttime = models.DateTimeField(db_column='DeviceWipeRequestTime', blank=True, null=True)  # Field name made lowercase.
    devicewipesenttime = models.DateTimeField(db_column='DeviceWipeSentTime', blank=True, null=True)  # Field name made lowercase.
    devicewipeacktime = models.DateTimeField(db_column='DeviceWipeAckTime', blank=True, null=True)  # Field name made lowercase.
    firstsynctime = models.DateTimeField(db_column='FirstSyncTime', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36, blank=True, null=True)  # Field name made lowercase.
    identity = models.CharField(db_column='Identity', max_length=256, blank=True, null=True)  # Field name made lowercase.
    lastpolicyupdatetime = models.DateTimeField(db_column='LastPolicyUpdateTime', blank=True, null=True)  # Field name made lowercase.
    lastsyncattempttime = models.DateTimeField(db_column='LastSyncAttemptTime', blank=True, null=True)  # Field name made lowercase.
    lastsuccesssync = models.DateTimeField(db_column='LastSuccessSync', blank=True, null=True)  # Field name made lowercase.
    lastdevicewiperequestor = models.CharField(db_column='LastDeviceWipeRequestor', max_length=256, blank=True, null=True)  # Field name made lowercase.
    mailbox = models.CharField(db_column='Mailbox', max_length=256, blank=True, null=True)  # Field name made lowercase.
    deviceimei = models.CharField(db_column='DeviceImei', max_length=100, blank=True, null=True)  # Field name made lowercase.
    deviceoslanguage = models.CharField(db_column='DeviceOSLanguage', max_length=50, blank=True, null=True)  # Field name made lowercase.
    devicephonenumber = models.CharField(db_column='DevicePhoneNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    devicemobileoperator = models.CharField(db_column='DeviceMobileOperator', max_length=100, blank=True, null=True)  # Field name made lowercase.
    numberoffolderssynced = models.IntegerField(db_column='NumberOfFoldersSynced', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExchangeActiveSyncDevice'


class Tblexchangegroup(models.Model):
    groupid = models.AutoField(db_column='GroupId', primary_key=True)  # Field name made lowercase.
    serverid = models.ForeignKey('Tblexchangeserver', models.DO_NOTHING, db_column='ServerId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    grouptype = models.CharField(db_column='GroupType', max_length=256, blank=True, null=True)  # Field name made lowercase.
    samaccountname = models.CharField(db_column='SamAccountName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sid = models.CharField(db_column='Sid', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sidhistory = models.CharField(db_column='SidHistory', max_length=256, blank=True, null=True)  # Field name made lowercase.
    simpledisplayname = models.CharField(db_column='SimpleDisplayName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    recipienttype = models.CharField(db_column='RecipientType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recipienttypedetails = models.CharField(db_column='RecipientTypeDetails', max_length=256, blank=True, null=True)  # Field name made lowercase.
    windowsemailaddress = models.CharField(db_column='WindowsEmailAddress', max_length=256, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    phoneticdisplayname = models.CharField(db_column='PhoneticDisplayName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    organizationalunit = models.CharField(db_column='OrganizationalUnit', max_length=256, blank=True, null=True)  # Field name made lowercase.
    seniorityindex = models.CharField(db_column='SeniorityIndex', max_length=16, blank=True, null=True)  # Field name made lowercase.
    ishierarchicalgroup = models.BooleanField(db_column='IsHierarchicalGroup', blank=True, null=True)  # Field name made lowercase.
    isdirsynced = models.BooleanField(db_column='IsDirSynced', blank=True, null=True)  # Field name made lowercase.
    identity = models.CharField(db_column='Identity', max_length=256, blank=True, null=True)  # Field name made lowercase.
    isvalid = models.BooleanField(db_column='IsValid', blank=True, null=True)  # Field name made lowercase.
    exchangeversion = models.CharField(db_column='ExchangeVersion', max_length=256, blank=True, null=True)  # Field name made lowercase.
    distinguishedname = models.CharField(db_column='DistinguishedName', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36, blank=True, null=True)  # Field name made lowercase.
    whenchangedutc = models.DateTimeField(db_column='WhenChangedUTC', blank=True, null=True)  # Field name made lowercase.
    whencreatedutc = models.DateTimeField(db_column='WhenCreatedUTC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExchangeGroup'


class Tblexchangegroupmember(models.Model):
    memberid = models.AutoField(db_column='MemberId', primary_key=True)  # Field name made lowercase.
    groupid = models.ForeignKey(Tblexchangegroup, models.DO_NOTHING, db_column='GroupId')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    childgroupid = models.IntegerField(db_column='ChildGroupId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExchangeGroupMember'


class Tblexchangelicense(models.Model):
    licenseid = models.AutoField(db_column='LicenseId', primary_key=True)  # Field name made lowercase.
    serverid = models.ForeignKey('Tblexchangeserver', models.DO_NOTHING, db_column='ServerId')  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=256)  # Field name made lowercase.
    unitlabel = models.CharField(db_column='UnitLabel', max_length=50)  # Field name made lowercase.
    licensename = models.CharField(db_column='LicenseName', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExchangeLicense'


class Tblexchangemailbox(models.Model):
    mailboxid = models.AutoField(db_column='MailboxId', primary_key=True)  # Field name made lowercase.
    serverid = models.ForeignKey('Tblexchangeserver', models.DO_NOTHING, db_column='ServerId')  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=256)  # Field name made lowercase.
    identity = models.CharField(db_column='Identity', max_length=256, blank=True, null=True)  # Field name made lowercase.
    database = models.CharField(db_column='Database', max_length=256, blank=True, null=True)  # Field name made lowercase.
    messagecopyforsentasenabled = models.BooleanField(db_column='MessageCopyForSentAsEnabled', blank=True, null=True)  # Field name made lowercase.
    messagecopyforsendonbehalfenabled = models.BooleanField(db_column='MessageCopyForSendOnBehalfEnabled', blank=True, null=True)  # Field name made lowercase.
    mailboxprovisioningpreferences = models.CharField(db_column='MailboxProvisioningPreferences', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    usedatabaseretentiondefaults = models.BooleanField(db_column='UseDatabaseRetentionDefaults', blank=True, null=True)  # Field name made lowercase.
    retaindeleteditemsuntilbackup = models.BooleanField(db_column='RetainDeletedItemsUntilBackup', blank=True, null=True)  # Field name made lowercase.
    delivertomailboxandforward = models.BooleanField(db_column='DeliverToMailboxAndForward', blank=True, null=True)  # Field name made lowercase.
    isexcludedfromservinghierarchy = models.BooleanField(db_column='IsExcludedFromServingHierarchy', blank=True, null=True)  # Field name made lowercase.
    ishierarchyready = models.BooleanField(db_column='IsHierarchyReady', blank=True, null=True)  # Field name made lowercase.
    ishierarchysyncenabled = models.BooleanField(db_column='IsHierarchySyncEnabled', blank=True, null=True)  # Field name made lowercase.
    litigationholdenabled = models.BooleanField(db_column='LitigationHoldEnabled', blank=True, null=True)  # Field name made lowercase.
    singleitemrecoveryenabled = models.BooleanField(db_column='SingleItemRecoveryEnabled', blank=True, null=True)  # Field name made lowercase.
    retentionholdenabled = models.BooleanField(db_column='RetentionHoldEnabled', blank=True, null=True)  # Field name made lowercase.
    enddateforretentionhold = models.DateTimeField(db_column='EndDateForRetentionHold', blank=True, null=True)  # Field name made lowercase.
    startdateforretentionhold = models.DateTimeField(db_column='StartDateForRetentionHold', blank=True, null=True)  # Field name made lowercase.
    retentioncomment = models.CharField(db_column='RetentionComment', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    retentionurl = models.CharField(db_column='RetentionUrl', max_length=500, blank=True, null=True)  # Field name made lowercase.
    litigationholddate = models.DateTimeField(db_column='LitigationHoldDate', blank=True, null=True)  # Field name made lowercase.
    litigationholdowner = models.CharField(db_column='LitigationHoldOwner', max_length=256, blank=True, null=True)  # Field name made lowercase.
    litigationholdduration = models.CharField(db_column='LitigationHoldDuration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    managedfoldermailboxpolicy = models.CharField(db_column='ManagedFolderMailboxPolicy', max_length=256, blank=True, null=True)  # Field name made lowercase.
    retentionpolicy = models.CharField(db_column='RetentionPolicy', max_length=256, blank=True, null=True)  # Field name made lowercase.
    addressbookpolicy = models.CharField(db_column='AddressBookPolicy', max_length=256, blank=True, null=True)  # Field name made lowercase.
    calendarrepairdisabled = models.BooleanField(db_column='CalendarRepairDisabled', blank=True, null=True)  # Field name made lowercase.
    exchangesecuritydescriptor = models.CharField(db_column='ExchangeSecurityDescriptor', max_length=256, blank=True, null=True)  # Field name made lowercase.
    exchangeuseraccountcontrol = models.CharField(db_column='ExchangeUserAccountControl', max_length=256, blank=True, null=True)  # Field name made lowercase.
    messagetrackingreadstatusenabled = models.BooleanField(db_column='MessageTrackingReadStatusEnabled', blank=True, null=True)  # Field name made lowercase.
    externaloofoptions = models.CharField(db_column='ExternalOofOptions', max_length=256, blank=True, null=True)  # Field name made lowercase.
    forwardingaddress = models.CharField(db_column='ForwardingAddress', max_length=256, blank=True, null=True)  # Field name made lowercase.
    retaindeleteditemsfor = models.CharField(db_column='RetainDeletedItemsFor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ismailboxenabled = models.BooleanField(db_column='IsMailboxEnabled', blank=True, null=True)  # Field name made lowercase.
    languages = models.CharField(db_column='Languages', max_length=100, blank=True, null=True)  # Field name made lowercase.
    offlineaddressbook = models.CharField(db_column='OfflineAddressBook', max_length=256, blank=True, null=True)  # Field name made lowercase.
    prohibitsendquota = models.CharField(db_column='ProhibitSendQuota', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prohibitsendreceivequota = models.CharField(db_column='ProhibitSendReceiveQuota', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recoverableitemsquota = models.CharField(db_column='RecoverableItemsQuota', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recoverableitemswarningquota = models.CharField(db_column='RecoverableItemsWarningQuota', max_length=50, blank=True, null=True)  # Field name made lowercase.
    downgradehighprioritymessagesenabled = models.BooleanField(db_column='DowngradeHighPriorityMessagesEnabled', blank=True, null=True)  # Field name made lowercase.
    protocolsettings = models.CharField(db_column='ProtocolSettings', max_length=256, blank=True, null=True)  # Field name made lowercase.
    recipientlimits = models.CharField(db_column='RecipientLimits', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isresource = models.BooleanField(db_column='IsResource', blank=True, null=True)  # Field name made lowercase.
    islinked = models.BooleanField(db_column='IsLinked', blank=True, null=True)  # Field name made lowercase.
    isshared = models.BooleanField(db_column='IsShared', blank=True, null=True)  # Field name made lowercase.
    linkedmasteraccount = models.CharField(db_column='LinkedMasterAccount', max_length=256, blank=True, null=True)  # Field name made lowercase.
    resetpasswordonnextlogon = models.BooleanField(db_column='ResetPasswordOnNextLogon', blank=True, null=True)  # Field name made lowercase.
    resourcecapacity = models.IntegerField(db_column='ResourceCapacity', blank=True, null=True)  # Field name made lowercase.
    resourcecustom = models.CharField(db_column='ResourceCustom', max_length=256, blank=True, null=True)  # Field name made lowercase.
    resourcetype = models.CharField(db_column='ResourceType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scldeletethreshold = models.IntegerField(db_column='SCLDeleteThreshold', blank=True, null=True)  # Field name made lowercase.
    scldeleteenabled = models.BooleanField(db_column='SCLDeleteEnabled', blank=True, null=True)  # Field name made lowercase.
    sclrejectthreshold = models.IntegerField(db_column='SCLRejectThreshold', blank=True, null=True)  # Field name made lowercase.
    sclrejectenabled = models.BooleanField(db_column='SCLRejectEnabled', blank=True, null=True)  # Field name made lowercase.
    sclquarantinethreshold = models.IntegerField(db_column='SCLQuarantineThreshold', blank=True, null=True)  # Field name made lowercase.
    sclquarantineenabled = models.BooleanField(db_column='SCLQuarantineEnabled', blank=True, null=True)  # Field name made lowercase.
    scljunkthreshold = models.IntegerField(db_column='SCLJunkThreshold', blank=True, null=True)  # Field name made lowercase.
    scljunkenabled = models.BooleanField(db_column='SCLJunkEnabled', blank=True, null=True)  # Field name made lowercase.
    antispambypassenabled = models.BooleanField(db_column='AntispamBypassEnabled', blank=True, null=True)  # Field name made lowercase.
    usedatabasequotadefaults = models.BooleanField(db_column='UseDatabaseQuotaDefaults', blank=True, null=True)  # Field name made lowercase.
    issuewarningquota = models.CharField(db_column='IssueWarningQuota', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rulesquota = models.CharField(db_column='RulesQuota', max_length=50, blank=True, null=True)  # Field name made lowercase.
    office = models.CharField(db_column='Office', max_length=256, blank=True, null=True)  # Field name made lowercase.
    umenabled = models.BooleanField(db_column='UMEnabled', blank=True, null=True)  # Field name made lowercase.
    maxsafesenders = models.IntegerField(db_column='MaxSafeSenders', blank=True, null=True)  # Field name made lowercase.
    maxblockedsenders = models.IntegerField(db_column='MaxBlockedSenders', blank=True, null=True)  # Field name made lowercase.
    throttlingpolicy = models.CharField(db_column='ThrottlingPolicy', max_length=256, blank=True, null=True)  # Field name made lowercase.
    roleassignmentpolicy = models.CharField(db_column='RoleAssignmentPolicy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sharingpolicy = models.CharField(db_column='SharingPolicy', max_length=256, blank=True, null=True)  # Field name made lowercase.
    mailboxplan = models.CharField(db_column='MailboxPlan', max_length=256, blank=True, null=True)  # Field name made lowercase.
    archiveguid = models.CharField(db_column='ArchiveGuid', max_length=36, blank=True, null=True)  # Field name made lowercase.
    archivename = models.CharField(db_column='ArchiveName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    archivequota = models.CharField(db_column='ArchiveQuota', max_length=50, blank=True, null=True)  # Field name made lowercase.
    archivewarningquota = models.CharField(db_column='ArchiveWarningQuota', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispersontopersontextmessagingenabled = models.BooleanField(db_column='IsPersonToPersonTextMessagingEnabled', blank=True, null=True)  # Field name made lowercase.
    ismachinetopersontextmessagingenabled = models.BooleanField(db_column='IsMachineToPersonTextMessagingEnabled', blank=True, null=True)  # Field name made lowercase.
    usersmimecertificate = models.CharField(db_column='UserSMimeCertificate', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    calendarversionstoredisabled = models.BooleanField(db_column='CalendarVersionStoreDisabled', blank=True, null=True)  # Field name made lowercase.
    immutableid = models.CharField(db_column='ImmutableId', max_length=256, blank=True, null=True)  # Field name made lowercase.
    whenmailboxcreated = models.DateTimeField(db_column='WhenMailboxCreated', blank=True, null=True)  # Field name made lowercase.
    issoftdeletedbyremove = models.BooleanField(db_column='IsSoftDeletedByRemove', blank=True, null=True)  # Field name made lowercase.
    issoftdeletedbydisable = models.BooleanField(db_column='IsSoftDeletedByDisable', blank=True, null=True)  # Field name made lowercase.
    isinactivemailbox = models.BooleanField(db_column='IsInactiveMailbox', blank=True, null=True)  # Field name made lowercase.
    whensoftdeleted = models.DateTimeField(db_column='WhenSoftDeleted', blank=True, null=True)  # Field name made lowercase.
    alias = models.CharField(db_column='Alias', max_length=256, blank=True, null=True)  # Field name made lowercase.
    legacyexchangedn = models.CharField(db_column='LegacyExchangeDN', max_length=256, blank=True, null=True)  # Field name made lowercase.
    maxsendsize = models.CharField(db_column='MaxSendSize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maxreceivesize = models.CharField(db_column='MaxReceiveSize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    policiesincluded = models.CharField(db_column='PoliciesIncluded', max_length=500, blank=True, null=True)  # Field name made lowercase.
    policiesexcluded_field = models.CharField(db_column='PoliciesExcluded ', max_length=500, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    emailaddresspolicyenabled = models.BooleanField(db_column='EmailAddressPolicyEnabled', blank=True, null=True)  # Field name made lowercase.
    primarysmtpaddress = models.CharField(db_column='PrimarySmtpAddress', max_length=256, blank=True, null=True)  # Field name made lowercase.
    recipienttype = models.CharField(db_column='RecipientType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipienttypedetails = models.CharField(db_column='RecipientTypeDetails', max_length=256, blank=True, null=True)  # Field name made lowercase.
    userprincipalname = models.CharField(db_column='UserPrincipalName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    owaenabled = models.BooleanField(db_column='OWAEnabled', blank=True, null=True)  # Field name made lowercase.
    journalrecipient = models.CharField(db_column='JournalRecipient', max_length=256, blank=True, null=True)  # Field name made lowercase.
    activesyncenabled = models.BooleanField(db_column='ActiveSyncEnabled', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExchangeMailbox'


class Tblexchangemailboxaddress(models.Model):
    addressid = models.AutoField(db_column='AddressId', primary_key=True)  # Field name made lowercase.
    mailboxid = models.ForeignKey(Tblexchangemailbox, models.DO_NOTHING, db_column='MailboxId')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExchangeMailboxAddress'


class Tblexchangemailboxstatistics(models.Model):
    statisticsid = models.AutoField(db_column='StatisticsId', primary_key=True)  # Field name made lowercase.
    mailboxid = models.ForeignKey(Tblexchangemailbox, models.DO_NOTHING, db_column='MailboxId')  # Field name made lowercase.
    itemcount = models.IntegerField(db_column='ItemCount', blank=True, null=True)  # Field name made lowercase.
    associateditemcount = models.IntegerField(db_column='AssociatedItemCount', blank=True, null=True)  # Field name made lowercase.
    deleteditemcount = models.IntegerField(db_column='DeletedItemCount', blank=True, null=True)  # Field name made lowercase.
    totaldeleteditemsize = models.CharField(db_column='TotalDeletedItemSize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    totalitemsize = models.CharField(db_column='TotalItemSize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    messagetabletotalsize = models.CharField(db_column='MessageTableTotalSize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    messagetableavailablesize = models.CharField(db_column='MessageTableAvailableSize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    attachmenttabletotalsize = models.CharField(db_column='AttachmentTableTotalSize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    attachmenttableavailablesize = models.CharField(db_column='AttachmentTableAvailableSize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    othertablestotalsize = models.CharField(db_column='OtherTablesTotalSize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    othertablesavailablesize = models.CharField(db_column='OtherTablesAvailableSize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isencrypted = models.BooleanField(db_column='IsEncrypted', blank=True, null=True)  # Field name made lowercase.
    disconnectdate = models.DateTimeField(db_column='DisconnectDate', blank=True, null=True)  # Field name made lowercase.
    disconnectreason = models.CharField(db_column='DisconnectReason', max_length=256, blank=True, null=True)  # Field name made lowercase.
    lastloggedonuseraccount = models.CharField(db_column='LastLoggedOnUserAccount', max_length=256, blank=True, null=True)  # Field name made lowercase.
    lastlogofftime = models.DateTimeField(db_column='LastLogoffTime', blank=True, null=True)  # Field name made lowercase.
    lastlogontime = models.DateTimeField(db_column='LastLogonTime', blank=True, null=True)  # Field name made lowercase.
    isdatabasecopyactive = models.BooleanField(db_column='IsDatabaseCopyActive', blank=True, null=True)  # Field name made lowercase.
    isclutterenabled = models.BooleanField(db_column='IsClutterEnabled', blank=True, null=True)  # Field name made lowercase.
    isquarantined = models.BooleanField(db_column='IsQuarantined', blank=True, null=True)  # Field name made lowercase.
    totalbytes = models.BigIntegerField(db_column='TotalBytes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExchangeMailboxStatistics'


class Tblexchangeserver(models.Model):
    serverid = models.AutoField(db_column='ServerId', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.
    datapath = models.CharField(db_column='DataPath', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    edition = models.CharField(db_column='Edition', max_length=256, blank=True, null=True)  # Field name made lowercase.
    exchangelegacydn = models.CharField(db_column='ExchangeLegacyDN', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    exchangelegacyserverrole = models.IntegerField(db_column='ExchangeLegacyServerRole', blank=True, null=True)  # Field name made lowercase.
    customerfeedbackenabled = models.BooleanField(db_column='CustomerFeedbackEnabled', blank=True, null=True)  # Field name made lowercase.
    internetwebproxy = models.CharField(db_column='InternetWebProxy', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    ishubtransportserver = models.BooleanField(db_column='IsHubTransportServer', blank=True, null=True)  # Field name made lowercase.
    isclientaccessserver = models.BooleanField(db_column='IsClientAccessServer', blank=True, null=True)  # Field name made lowercase.
    isexchange2007orlater = models.BooleanField(db_column='IsExchange2007OrLater', blank=True, null=True)  # Field name made lowercase.
    isedgeserver = models.BooleanField(db_column='IsEdgeServer', blank=True, null=True)  # Field name made lowercase.
    ismailboxserver = models.BooleanField(db_column='IsMailboxServer', blank=True, null=True)  # Field name made lowercase.
    ise14orlater = models.BooleanField(db_column='IsE14OrLater', blank=True, null=True)  # Field name made lowercase.
    ise15orlater = models.BooleanField(db_column='IsE15OrLater', blank=True, null=True)  # Field name made lowercase.
    isprovisionedserver = models.BooleanField(db_column='IsProvisionedServer', blank=True, null=True)  # Field name made lowercase.
    isunifiedmessagingserver = models.BooleanField(db_column='IsUnifiedMessagingServer', blank=True, null=True)  # Field name made lowercase.
    isfrontendtransportserver = models.BooleanField(db_column='IsFrontendTransportServer', blank=True, null=True)  # Field name made lowercase.
    networkaddress = models.CharField(db_column='NetworkAddress', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    organizationalunit = models.CharField(db_column='OrganizationalUnit', max_length=300, blank=True, null=True)  # Field name made lowercase.
    admindisplayversion = models.CharField(db_column='AdminDisplayVersion', max_length=256, blank=True, null=True)  # Field name made lowercase.
    site = models.CharField(db_column='Site', max_length=300, blank=True, null=True)  # Field name made lowercase.
    serverrole = models.CharField(db_column='ServerRole', max_length=100, blank=True, null=True)  # Field name made lowercase.
    errorreportingenabled = models.BooleanField(db_column='ErrorReportingEnabled', blank=True, null=True)  # Field name made lowercase.
    staticdomaincontrollers = models.CharField(db_column='StaticDomainControllers', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    staticglobalcatalogs = models.CharField(db_column='StaticGlobalCatalogs', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    staticconfigdomaincontroller = models.CharField(db_column='StaticConfigDomainController', max_length=256, blank=True, null=True)  # Field name made lowercase.
    staticexcludeddomaincontrollers = models.CharField(db_column='StaticExcludedDomainControllers', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    monitoringgroup = models.CharField(db_column='MonitoringGroup', max_length=256, blank=True, null=True)  # Field name made lowercase.
    currentdomaincontrollers = models.CharField(db_column='CurrentDomainControllers', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    currentglobalcatalogs = models.CharField(db_column='CurrentGlobalCatalogs', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    currentconfigdomaincontroller = models.CharField(db_column='CurrentConfigDomainController', max_length=256, blank=True, null=True)  # Field name made lowercase.
    productid = models.CharField(db_column='ProductId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isexchangetrialedition = models.BooleanField(db_column='IsExchangeTrialEdition', blank=True, null=True)  # Field name made lowercase.
    isexpiredexchangetrialedition = models.BooleanField(db_column='IsExpiredExchangeTrialEdition', blank=True, null=True)  # Field name made lowercase.
    mailboxprovisioningattributes = models.CharField(db_column='MailboxProvisioningAttributes', max_length=300, blank=True, null=True)  # Field name made lowercase.
    remainingtrialperiod = models.CharField(db_column='RemainingTrialPeriod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    identity = models.CharField(db_column='Identity', max_length=256, blank=True, null=True)  # Field name made lowercase.
    isvalid = models.BooleanField(db_column='IsValid', blank=True, null=True)  # Field name made lowercase.
    exchangeversion = models.CharField(db_column='ExchangeVersion', max_length=256, blank=True, null=True)  # Field name made lowercase.
    distinguishedname = models.CharField(db_column='DistinguishedName', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36, blank=True, null=True)  # Field name made lowercase.
    whenchangedutc = models.DateTimeField(db_column='WhenChangedUTC', blank=True, null=True)  # Field name made lowercase.
    whencreatedutc = models.DateTimeField(db_column='WhenCreatedUTC', blank=True, null=True)  # Field name made lowercase.
    organizationid = models.CharField(db_column='OrganizationId', max_length=256, blank=True, null=True)  # Field name made lowercase.
    originatingserver = models.CharField(db_column='OriginatingServer', max_length=256, blank=True, null=True)  # Field name made lowercase.
    lastscanned = models.DateTimeField(db_column='LastScanned', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExchangeServer'


class Tblexchangeuser(models.Model):
    userid = models.AutoField(db_column='UserId', primary_key=True)  # Field name made lowercase.
    serverid = models.ForeignKey(Tblexchangeserver, models.DO_NOTHING, db_column='ServerId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.
    samaccountname = models.CharField(db_column='SamAccountName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    issecurityprincipal = models.BooleanField(db_column='IsSecurityPrincipal', blank=True, null=True)  # Field name made lowercase.
    sid = models.CharField(db_column='Sid', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sidhistory = models.CharField(db_column='SidHistory', max_length=256, blank=True, null=True)  # Field name made lowercase.
    userprincipalname = models.CharField(db_column='UserPrincipalName', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    resetpasswordonnextlogon = models.BooleanField(db_column='ResetPasswordOnNextLogon', blank=True, null=True)  # Field name made lowercase.
    certificatesubject = models.CharField(db_column='CertificateSubject', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    remotepowershellenabled = models.BooleanField(db_column='RemotePowerShellEnabled', blank=True, null=True)  # Field name made lowercase.
    microsoftonlineservicesid = models.CharField(db_column='MicrosoftOnlineServicesId', max_length=256, blank=True, null=True)  # Field name made lowercase.
    useraccountcontrol = models.CharField(db_column='UserAccountControl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    organizationalunit = models.CharField(db_column='OrganizationalUnit', max_length=300, blank=True, null=True)  # Field name made lowercase.
    islinked = models.BooleanField(db_column='IsLinked', blank=True, null=True)  # Field name made lowercase.
    linkedmasteraccount = models.CharField(db_column='LinkedMasterAccount', max_length=256, blank=True, null=True)  # Field name made lowercase.
    issoftdeletedbyremove = models.BooleanField(db_column='IsSoftDeletedByRemove', blank=True, null=True)  # Field name made lowercase.
    issoftdeletedbydisable = models.BooleanField(db_column='IsSoftDeletedByDisable', blank=True, null=True)  # Field name made lowercase.
    whensoftdeleted = models.DateTimeField(db_column='WhenSoftDeleted', blank=True, null=True)  # Field name made lowercase.
    legacyexchangedn = models.CharField(db_column='LegacyExchangeDN', max_length=256, blank=True, null=True)  # Field name made lowercase.
    accountdisabled = models.BooleanField(db_column='AccountDisabled', blank=True, null=True)  # Field name made lowercase.
    authenticationpolicy = models.CharField(db_column='AuthenticationPolicy', max_length=256, blank=True, null=True)  # Field name made lowercase.
    mailboxlocations = models.CharField(db_column='MailboxLocations', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    administrativeunits = models.CharField(db_column='AdministrativeUnits', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    assistantname = models.CharField(db_column='AssistantName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=256, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=256, blank=True, null=True)  # Field name made lowercase.
    countryorregion = models.CharField(db_column='CountryOrRegion', max_length=256, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=256, blank=True, null=True)  # Field name made lowercase.
    directreports = models.TextField(db_column='DirectReports', blank=True, null=True)  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=256, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    geocoordinates = models.CharField(db_column='GeoCoordinates', max_length=50, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=256, blank=True, null=True)  # Field name made lowercase.
    initials = models.CharField(db_column='Initials', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isdirsynced = models.BooleanField(db_column='IsDirSynced', blank=True, null=True)  # Field name made lowercase.
    manager = models.CharField(db_column='Manager', max_length=256, blank=True, null=True)  # Field name made lowercase.
    mobilephone = models.CharField(db_column='MobilePhone', max_length=256, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    office = models.CharField(db_column='Office', max_length=256, blank=True, null=True)  # Field name made lowercase.
    otherfax = models.CharField(db_column='OtherFax', max_length=256, blank=True, null=True)  # Field name made lowercase.
    otherhomephone = models.CharField(db_column='OtherHomePhone', max_length=256, blank=True, null=True)  # Field name made lowercase.
    othertelephone = models.CharField(db_column='OtherTelephone', max_length=256, blank=True, null=True)  # Field name made lowercase.
    pager = models.CharField(db_column='Pager', max_length=256, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=256, blank=True, null=True)  # Field name made lowercase.
    phoneticdisplayname = models.CharField(db_column='PhoneticDisplayName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=40, blank=True, null=True)  # Field name made lowercase.
    postofficebox = models.CharField(db_column='PostOfficeBox', max_length=256, blank=True, null=True)  # Field name made lowercase.
    recipienttype = models.CharField(db_column='RecipientType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipienttypedetails = models.CharField(db_column='RecipientTypeDetails', max_length=256, blank=True, null=True)  # Field name made lowercase.
    simpledisplayname = models.CharField(db_column='SimpleDisplayName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    stateorprovince = models.CharField(db_column='StateOrProvince', max_length=256, blank=True, null=True)  # Field name made lowercase.
    streetaddress = models.CharField(db_column='StreetAddress', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=256, blank=True, null=True)  # Field name made lowercase.
    umdialplan = models.CharField(db_column='UMDialPlan', max_length=256, blank=True, null=True)  # Field name made lowercase.
    umdtmfmap = models.CharField(db_column='UMDtmfMap', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    allowumcallsfromnonusers = models.CharField(db_column='AllowUMCallsFromNonUsers', max_length=256, blank=True, null=True)  # Field name made lowercase.
    webpage = models.CharField(db_column='WebPage', max_length=500, blank=True, null=True)  # Field name made lowercase.
    telephoneassistant = models.CharField(db_column='TelephoneAssistant', max_length=256, blank=True, null=True)  # Field name made lowercase.
    windowsemailaddress = models.CharField(db_column='WindowsEmailAddress', max_length=256, blank=True, null=True)  # Field name made lowercase.
    umcallinglineids = models.CharField(db_column='UMCallingLineIds', max_length=256, blank=True, null=True)  # Field name made lowercase.
    seniorityindex = models.CharField(db_column='SeniorityIndex', max_length=16, blank=True, null=True)  # Field name made lowercase.
    voicemailsettings = models.CharField(db_column='VoiceMailSettings', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    identity = models.CharField(db_column='Identity', max_length=256, blank=True, null=True)  # Field name made lowercase.
    isvalid = models.BooleanField(db_column='IsValid', blank=True, null=True)  # Field name made lowercase.
    exchangeversion = models.CharField(db_column='ExchangeVersion', max_length=256, blank=True, null=True)  # Field name made lowercase.
    distinguishedname = models.CharField(db_column='DistinguishedName', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36, blank=True, null=True)  # Field name made lowercase.
    whenchangedutc = models.DateTimeField(db_column='WhenChangedUTC', blank=True, null=True)  # Field name made lowercase.
    whencreatedutc = models.DateTimeField(db_column='WhenCreatedUTC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExchangeUser'


class Tblexchangeuserlicense(models.Model):
    userlicenseid = models.AutoField(db_column='UserLicenseId', primary_key=True)  # Field name made lowercase.
    licenseid = models.ForeignKey(Tblexchangelicense, models.DO_NOTHING, db_column='LicenseId')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExchangeUserLicense'


class Tblextendeddisplayuni(models.Model):
    extendeddisplayuniid = models.AutoField(db_column='ExtendedDisplayUniId', primary_key=True)  # Field name made lowercase.
    sizeininch = models.DecimalField(db_column='SizeInInch', max_digits=9, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    maxresolution = models.CharField(db_column='MaxResolution', max_length=20, blank=True, null=True)  # Field name made lowercase.
    aspectratio = models.CharField(db_column='AspectRatio', max_length=20, blank=True, null=True)  # Field name made lowercase.
    responsetimeinms = models.DecimalField(db_column='ResponseTimeInMs', max_digits=9, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hdtype = models.CharField(db_column='HDType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    displaytech = models.CharField(db_column='DisplayTech', max_length=50, blank=True, null=True)  # Field name made lowercase.
    refreshrate = models.DecimalField(db_column='RefreshRate', max_digits=9, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    panel = models.CharField(db_column='Panel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    heightincm = models.DecimalField(db_column='HeightInCm', max_digits=9, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    widthincm = models.DecimalField(db_column='WidthInCm', max_digits=9, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    diagonalincm = models.DecimalField(db_column='DiagonalInCm', max_digits=9, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasspeakers = models.BooleanField(db_column='HasSpeakers', blank=True, null=True)  # Field name made lowercase.
    hascamera = models.BooleanField(db_column='HasCamera', blank=True, null=True)  # Field name made lowercase.
    hasusbhub = models.BooleanField(db_column='HasUsbHub', blank=True, null=True)  # Field name made lowercase.
    usbupstream = models.CharField(db_column='UsbUpstream', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nrofusbupstream = models.IntegerField(db_column='NrOfUsbUpstream', blank=True, null=True)  # Field name made lowercase.
    usbtypeadownstream = models.IntegerField(db_column='UsbTypeADownstream', blank=True, null=True)  # Field name made lowercase.
    nrofvga = models.IntegerField(db_column='NrOfVGA', blank=True, null=True)  # Field name made lowercase.
    nrofdvi = models.IntegerField(db_column='NrOfDVI', blank=True, null=True)  # Field name made lowercase.
    nrofhdmi = models.IntegerField(db_column='NrOfHdmi', blank=True, null=True)  # Field name made lowercase.
    hdmiversion = models.CharField(db_column='HDMIVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numberofdisplayports = models.IntegerField(db_column='NumberOfDisplayPorts', blank=True, null=True)  # Field name made lowercase.
    displayportversion = models.CharField(db_column='DisplayPortVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    energyclass = models.CharField(db_column='EnergyClass', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sdrper1000u = models.DecimalField(db_column='SDRPer1000u', max_digits=9, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    averagewattusage = models.DecimalField(db_column='AverageWattUsage', max_digits=9, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    standbywattusage = models.DecimalField(db_column='StandByWattUsage', max_digits=9, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    maxwattusage = models.DecimalField(db_column='MaxWattUsage', max_digits=9, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    wattusagewhenoff = models.DecimalField(db_column='WattUsageWhenOff', max_digits=9, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    wattpowersave = models.DecimalField(db_column='WattPowerSave', max_digits=9, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    acvoltage = models.CharField(db_column='ACVoltage', max_length=50, blank=True, null=True)  # Field name made lowercase.
    acfreqinhz = models.CharField(db_column='ACFreqInHz', max_length=50, blank=True, null=True)  # Field name made lowercase.
    currentina = models.DecimalField(db_column='CurrentInA', max_digits=9, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate')  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=250)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExtendedDisplayUni'


class Tblfeature(models.Model):
    featureid = models.AutoField(db_column='FeatureId', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    featuniid = models.ForeignKey('Tblfeatureuni', models.DO_NOTHING, db_column='featUniId')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblFeature'


class Tblfeatureuni(models.Model):
    featuniid = models.AutoField(db_column='featUniID', primary_key=True)  # Field name made lowercase.
    featurename = models.CharField(db_column='featureName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    featurecaption = models.CharField(db_column='featureCaption', max_length=150, blank=True, null=True)  # Field name made lowercase.
    addeddate = models.DateTimeField(db_column='addedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblFeatureUni'
        unique_together = (('featurename', 'featurecaption'),)


class Tblfileversions(models.Model):
    versionid = models.AutoField(db_column='VersionID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    found = models.BooleanField(db_column='Found', blank=True, null=True)  # Field name made lowercase.
    filepathfull = models.CharField(db_column='FilePathfull', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    fileversion = models.CharField(db_column='FileVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    filesize = models.DecimalField(db_column='Filesize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    lastaccessed = models.DateTimeField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblFileVersions'


class Tblfloppy(models.Model):
    floppyid = models.AutoField(db_column='floppyID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    bytespersector = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    interfacetype = models.CharField(db_column='InterfaceType', max_length=450, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=450, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=450, blank=True, null=True)  # Field name made lowercase.
    partitions = models.DecimalField(db_column='Partitions', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    sectorspertrack = models.DecimalField(db_column='Sectorspertrack', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    size = models.DecimalField(db_column='Size', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    totalcylinders = models.DecimalField(db_column='Totalcylinders', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    totalheads = models.DecimalField(db_column='Totalheads', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    totalsectors = models.DecimalField(db_column='Totalsectors', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    totaltracks = models.DecimalField(db_column='Totaltracks', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    trackspercylinder = models.DecimalField(db_column='TracksperCylinder', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    firmwarerevision = models.CharField(db_column='FirmwareRevision', max_length=250, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=250, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblFloppy'


class Tblfloppyhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    bytespersector = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    interfacetype = models.CharField(db_column='InterfaceType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=300, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=450, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=450, blank=True, null=True)  # Field name made lowercase.
    partitions = models.DecimalField(db_column='Partitions', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    sectorspertrack = models.DecimalField(db_column='Sectorspertrack', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    size = models.DecimalField(db_column='Size', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    totalcylinders = models.DecimalField(db_column='Totalcylinders', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    totalheads = models.DecimalField(db_column='Totalheads', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    totalsectors = models.DecimalField(db_column='Totalsectors', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    totaltracks = models.DecimalField(db_column='Totaltracks', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    trackspercylinder = models.DecimalField(db_column='TracksperCylinder', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    firmwarerevision = models.CharField(db_column='FirmwareRevision', max_length=250, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=250, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblFloppyHist'


class Tblgroupuni(models.Model):
    groupid = models.AutoField(db_column='GroupID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sid = models.CharField(db_column='SID', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblGroupUni'
        unique_together = (('name', 'sid'),)


class Tblgroups(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    groupid = models.ForeignKey(Tblgroupuni, models.DO_NOTHING, db_column='GroupID')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblGroups'


class Tblgroupshist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblGroupsHist'


class Tblhypervguest(models.Model):
    hypervguestid = models.AutoField(db_column='hypervguestID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enabledstate = models.BigIntegerField(db_column='Enabledstate', blank=True, null=True)  # Field name made lowercase.
    healthstate = models.BigIntegerField(db_column='Healthstate', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    memory = models.IntegerField(db_column='Memory', blank=True, null=True)  # Field name made lowercase.
    instanceid = models.CharField(db_column='InstanceID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    guestassetid = models.IntegerField(db_column='GuestAssetId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblHyperVGuest'


class Tblhypervlog(models.Model):
    hypervlogid = models.AutoField(db_column='HyperVLogId', primary_key=True)  # Field name made lowercase.
    hypervhostscannedid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='HyperVHostScannedId', blank=True, null=True)  # Field name made lowercase.
    hypervhostsourceid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='HyperVHostSourceId', blank=True, null=True)  # Field name made lowercase.
    hypervhostdestinationid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='HyperVHostDestinationId', blank=True, null=True)  # Field name made lowercase.
    hypervguestid = models.ForeignKey(Tblhypervguest, models.DO_NOTHING, db_column='HyperVGuestId', blank=True, null=True)  # Field name made lowercase.
    action = models.IntegerField(db_column='Action', blank=True, null=True)  # Field name made lowercase.
    eventtimecreated = models.DateTimeField(db_column='EventTimeCreated')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EventId')  # Field name made lowercase.
    eventlevelid = models.IntegerField(db_column='EventLevelId')  # Field name made lowercase.
    eventmessageid = models.ForeignKey('Tblntlogmessage', models.DO_NOTHING, db_column='EventMessageId')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblHyperVLog'


class Tblidecontroller(models.Model):
    win32_idecontrollerid = models.AutoField(db_column='Win32_IDEControllerid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    protocolsupported = models.DecimalField(db_column='ProtocolSupported', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblIDEController'


class Tblidecontrollerhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    protocolsupported = models.DecimalField(db_column='ProtocolSupported', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblIDEControllerHist'


class Tblieactivex(models.Model):
    ieactivexid = models.AutoField(db_column='IEactivexID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    control = models.CharField(db_column='Control', max_length=150, blank=True, null=True)  # Field name made lowercase.
    codebase = models.CharField(db_column='CodeBase', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    inf = models.CharField(db_column='Inf', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    osd = models.CharField(db_column='OSD', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblIEActiveX'


class Tblieactivexhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    control = models.CharField(db_column='Control', max_length=150, blank=True, null=True)  # Field name made lowercase.
    codebase = models.CharField(db_column='CodeBase', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    inf = models.CharField(db_column='Inf', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    osd = models.CharField(db_column='OSD', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblIEActiveXHist'


class Tbliebho(models.Model):
    iebhoid = models.AutoField(db_column='IEbhoID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    control = models.CharField(db_column='Control', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblIEBHO'


class Tbliebhohist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    control = models.CharField(db_column='Control', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblIEBHOHist'


class Tbliebars(models.Model):
    iebarid = models.AutoField(db_column='IEbarID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    control = models.CharField(db_column='Control', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblIEBars'


class Tbliebarshist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    control = models.CharField(db_column='Control', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblIEBarsHist'


class Tblieextensions(models.Model):
    ieextid = models.AutoField(db_column='IEextID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    control = models.CharField(db_column='Control', max_length=50, blank=True, null=True)  # Field name made lowercase.
    buttontext = models.CharField(db_column='Buttontext', max_length=500, blank=True, null=True)  # Field name made lowercase.
    clsid = models.CharField(db_column='CLSID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    exec = models.CharField(db_column='Exec', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    menutext = models.CharField(db_column='Menutext', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblIEExtensions'


class Tblieextensionshist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    control = models.CharField(db_column='Control', max_length=50, blank=True, null=True)  # Field name made lowercase.
    buttontext = models.CharField(db_column='Buttontext', max_length=500, blank=True, null=True)  # Field name made lowercase.
    clsid = models.CharField(db_column='CLSID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    exec = models.CharField(db_column='Exec', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    menutext = models.CharField(db_column='Menutext', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblIEExtensionsHist'


class Tblinfrareddevice(models.Model):
    win32_infrareddeviceid = models.AutoField(db_column='Win32_InfraredDeviceid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    availability = models.DecimalField(db_column='Availability', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    configmanagererrorcode = models.DecimalField(db_column='ConfigManagerErrorCode', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    configmanageruserconfig = models.BooleanField(db_column='ConfigManagerUserConfig', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    protocolsupported = models.BooleanField(db_column='ProtocolSupported', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfraredDevice'


class Tblinfrareddevicehist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    availability = models.DecimalField(db_column='Availability', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    configmanagererrorcode = models.DecimalField(db_column='ConfigManagerErrorCode', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    configmanageruserconfig = models.BooleanField(db_column='ConfigManagerUserConfig', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    protocolsupported = models.BooleanField(db_column='ProtocolSupported', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfraredDeviceHist'


class Tblintuneapplication(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    intuneid = models.CharField(db_column='IntuneId', max_length=100)  # Field name made lowercase.
    intunecontainerid = models.ForeignKey('Tblintunecontainer', models.DO_NOTHING, db_column='IntuneContainerId')  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=255)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sizeinbyte = models.BigIntegerField(db_column='SizeInByte', blank=True, null=True)  # Field name made lowercase.
    devicecount = models.IntegerField(db_column='DeviceCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblIntuneApplication'


class Tblintunecontainer(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    intuneaccount = models.CharField(db_column='IntuneAccount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    appid = models.CharField(db_column='AppId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tenantid = models.CharField(db_column='TenantId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblIntuneContainer'


class Tblintunedevice(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    intunecontainerid = models.ForeignKey(Tblintunecontainer, models.DO_NOTHING, db_column='IntuneContainerId')  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    intuneid = models.CharField(db_column='IntuneId', max_length=100)  # Field name made lowercase.
    remoteassistancesessionerrordetails = models.CharField(db_column='RemoteAssistanceSessionErrorDetails', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isencrypted = models.BooleanField(db_column='IsEncrypted', blank=True, null=True)  # Field name made lowercase.
    userprincipalname = models.CharField(db_column='UserPrincipalName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=100, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    imei = models.CharField(db_column='Imei', max_length=100, blank=True, null=True)  # Field name made lowercase.
    compliancegraceperiodexpirationdatetime = models.DateTimeField(db_column='ComplianceGracePeriodExpirationDateTime', blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    androidsecuritypatchlevel = models.CharField(db_column='AndroidSecurityPatchLevel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    userdisplayname = models.CharField(db_column='UserDisplayName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    wifimacaddress = models.CharField(db_column='WiFiMacAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    subscribercarrier = models.CharField(db_column='SubscriberCarrier', max_length=50, blank=True, null=True)  # Field name made lowercase.
    meid = models.CharField(db_column='Meid', max_length=20, blank=True, null=True)  # Field name made lowercase.
    totalstoragespaceinbytes = models.BigIntegerField(db_column='TotalStorageSpaceInBytes', blank=True, null=True)  # Field name made lowercase.
    freestoragespaceinbytes = models.BigIntegerField(db_column='FreeStorageSpaceInBytes', blank=True, null=True)  # Field name made lowercase.
    manageddevicename = models.CharField(db_column='ManagedDeviceName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    partnerreportedthreatstate = models.CharField(db_column='PartnerReportedThreatState', max_length=20, blank=True, null=True)  # Field name made lowercase.
    remoteassistancesessionurl = models.CharField(db_column='RemoteAssistanceSessionUrl', max_length=50, blank=True, null=True)  # Field name made lowercase.
    exchangeaccessstate = models.CharField(db_column='ExchangeAccessState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    exchangeaccessstatereason = models.CharField(db_column='ExchangeAccessStateReason', max_length=50, blank=True, null=True)  # Field name made lowercase.
    exchangelastsuccessfulsyncdatetime = models.DateTimeField(db_column='ExchangeLastSuccessfulSyncDateTime', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    devicename = models.CharField(db_column='DeviceName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manageddeviceownertype = models.CharField(db_column='ManagedDeviceOwnerType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    enrolleddatetime = models.DateTimeField(db_column='EnrolledDateTime', blank=True, null=True)  # Field name made lowercase.
    lastsyncdatetime = models.DateTimeField(db_column='LastSyncDateTime', blank=True, null=True)  # Field name made lowercase.
    operatingsystem = models.CharField(db_column='OperatingSystem', max_length=50, blank=True, null=True)  # Field name made lowercase.
    compliancestate = models.CharField(db_column='ComplianceState', max_length=20, blank=True, null=True)  # Field name made lowercase.
    jailbroken = models.CharField(db_column='JailBroken', max_length=50, blank=True, null=True)  # Field name made lowercase.
    managementagent = models.CharField(db_column='ManagementAgent', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osversion = models.CharField(db_column='OsVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    easdeviceid = models.CharField(db_column='EasDeviceId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    easactivationdatetime = models.DateTimeField(db_column='EasActivationDateTime', blank=True, null=True)  # Field name made lowercase.
    isazureadregistered = models.BooleanField(db_column='IsAzureADRegistered', blank=True, null=True)  # Field name made lowercase.
    deviceenrollmenttype = models.CharField(db_column='DeviceEnrollmentType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    activationlockbypasscode = models.CharField(db_column='ActivationLockBypassCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    azureaddeviceid = models.CharField(db_column='AzureADDeviceId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deviceregistrationstate = models.CharField(db_column='DeviceRegistrationState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    issupervised = models.BooleanField(db_column='IsSupervised', blank=True, null=True)  # Field name made lowercase.
    iseasactivated = models.BooleanField(db_column='IsEasActivated', blank=True, null=True)  # Field name made lowercase.
    hasfeatureinventory = models.BooleanField(db_column='HasFeatureInventory', blank=True, null=True)  # Field name made lowercase.
    hasfeaturemodernapps = models.BooleanField(db_column='HasFeatureModernApps', blank=True, null=True)  # Field name made lowercase.
    hasfeatureresourceaccess = models.BooleanField(db_column='HasFeatureResourceAccess', blank=True, null=True)  # Field name made lowercase.
    hasfeaturedeviceconfiguration = models.BooleanField(db_column='HasFeatureDeviceConfiguration', blank=True, null=True)  # Field name made lowercase.
    hasfeaturecompliancepolicy = models.BooleanField(db_column='HasFeatureCompliancePolicy', blank=True, null=True)  # Field name made lowercase.
    hasfeaturewindowsupdateforbusiness = models.BooleanField(db_column='HasFeatureWindowsUpdateForBusiness', blank=True, null=True)  # Field name made lowercase.
    healthstatusmismatchinfo = models.CharField(db_column='HealthStatusMismatchInfo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    operatingsystemkerneldebugging = models.CharField(db_column='OperatingSystemKernelDebugging', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codeintegrity = models.CharField(db_column='CodeIntegrity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    testsigning = models.CharField(db_column='TestSigning', max_length=50, blank=True, null=True)  # Field name made lowercase.
    safemode = models.CharField(db_column='SafeMode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    windowspe = models.CharField(db_column='WindowsPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    earlylaunchantimalwaredriverprotection = models.CharField(db_column='EarlyLaunchAntiMalwareDriverProtection', max_length=50, blank=True, null=True)  # Field name made lowercase.
    virtualsecuremode = models.CharField(db_column='VirtualSecureMode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pcrhashalgorithm = models.CharField(db_column='PcrHashAlgorithm', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bootappsecurityversion = models.CharField(db_column='BootAppSecurityVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bootmanagersecurityversion = models.CharField(db_column='BootManagerSecurityVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tpmversion = models.CharField(db_column='TpmVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pcr0 = models.CharField(db_column='Pcr0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    securebootconfigurationpolicyfingerprint = models.CharField(db_column='SecureBootConfigurationPolicyFingerPrint', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codeintegritypolicy = models.CharField(db_column='CodeIntegrityPolicy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bootrevisionlistinfo = models.CharField(db_column='BootRevisionListInfo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    operatingsystemrevlistinfo = models.CharField(db_column='OperatingSystemRevListInfo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastupdatedatetime = models.CharField(db_column='LastUpdateDateTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contentnamespaceurl = models.CharField(db_column='ContentNamespaceUrl', max_length=50, blank=True, null=True)  # Field name made lowercase.
    devicehealthattestationstatus = models.CharField(db_column='DeviceHealthAttestationStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contentversion = models.CharField(db_column='ContentVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    issueddatetime = models.DateTimeField(db_column='IssuedDateTime', blank=True, null=True)  # Field name made lowercase.
    attestationidentitykey = models.CharField(db_column='AttestationIdentityKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    healthattestationsupportedstatus = models.CharField(db_column='HealthAttestationSupportedStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    resetcount = models.BigIntegerField(db_column='ResetCount', blank=True, null=True)  # Field name made lowercase.
    restartcount = models.BigIntegerField(db_column='RestartCount', blank=True, null=True)  # Field name made lowercase.
    dataexcutionpolicy = models.CharField(db_column='DataExcutionPolicy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bitlockerstatus = models.CharField(db_column='BitLockerStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bootmanagerversion = models.CharField(db_column='BootManagerVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codeintegritycheckversion = models.CharField(db_column='CodeIntegrityCheckVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    secureboot = models.CharField(db_column='SecureBoot', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bootdebugging = models.CharField(db_column='BootDebugging', max_length=50, blank=True, null=True)  # Field name made lowercase.
    devicecategoryid = models.CharField(db_column='DeviceCategoryId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    devicecategorydisplayname = models.CharField(db_column='DeviceCategoryDisplayName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    devicecategorydescription = models.CharField(db_column='DeviceCategoryDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastupdatedatetimeutc = models.DateTimeField(db_column='LastUpdateDateTimeUtc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblIntuneDevice'


class Tblintunedeviceactionresult(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    intunedeviceid = models.ForeignKey(Tblintunedevice, models.DO_NOTHING, db_column='IntuneDeviceId')  # Field name made lowercase.
    actionname = models.CharField(db_column='ActionName', max_length=50)  # Field name made lowercase.
    actionstate = models.CharField(db_column='ActionState', max_length=20, blank=True, null=True)  # Field name made lowercase.
    startdatetime = models.DateTimeField(db_column='StartDateTime', blank=True, null=True)  # Field name made lowercase.
    lastupdateddatetime = models.DateTimeField(db_column='LastUpdatedDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblIntuneDeviceActionResult'


class Tblintunedeviceapplication(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    intunedeviceid = models.ForeignKey(Tblintunedevice, models.DO_NOTHING, db_column='IntuneDeviceId')  # Field name made lowercase.
    intuneapplicationid = models.ForeignKey(Tblintuneapplication, models.DO_NOTHING, db_column='IntuneApplicationId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblIntuneDeviceApplication'


class Tblkeyboard(models.Model):
    win32_keyboardid = models.AutoField(db_column='Win32_Keyboardid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    configmanagererrorcode = models.DecimalField(db_column='ConfigManagerErrorCode', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    configmanageruserconfig = models.BooleanField(db_column='ConfigManagerUserConfig', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=450, blank=True, null=True)  # Field name made lowercase.
    layout = models.CharField(db_column='Layout', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numberoffunctionkeys = models.DecimalField(db_column='NumberOfFunctionKeys', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblKeyboard'


class Tblkeyboardhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    configmanagererrorcode = models.DecimalField(db_column='ConfigManagerErrorCode', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    configmanageruserconfig = models.BooleanField(db_column='ConfigManagerUserConfig', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=450, blank=True, null=True)  # Field name made lowercase.
    layout = models.CharField(db_column='Layout', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numberoffunctionkeys = models.DecimalField(db_column='NumberOfFunctionKeys', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblKeyboardHist'


class Tbllanguages(models.Model):
    languagecode = models.IntegerField(db_column='LanguageCode', primary_key=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLanguages'


class Tbllicenses(models.Model):
    licenseidid = models.AutoField(db_column='LicenseidID', primary_key=True)  # Field name made lowercase.
    softwarename = models.CharField(db_column='softwareName', unique=True, max_length=300)  # Field name made lowercase.
    priceperlicense = models.DecimalField(db_column='Priceperlicense', max_digits=19, decimal_places=4)  # Field name made lowercase.
    licensetype = models.ForeignKey('Tsyslicensetype', models.DO_NOTHING, db_column='LicenseType', blank=True, null=True)  # Field name made lowercase.
    licensetypecomments = models.TextField(db_column='LicenseTypeComments', blank=True, null=True)  # Field name made lowercase.
    licensecontract = models.BooleanField(db_column='LicenseContract')  # Field name made lowercase.
    licenseexpiration = models.DateTimeField(db_column='LicenseExpiration', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    licensecontact = models.CharField(db_column='LicenseContact', max_length=500, blank=True, null=True)  # Field name made lowercase.
    licenseowner = models.CharField(db_column='LicenseOwner', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLicenses'


class Tbllinuxbaseboard(models.Model):
    baseboardid = models.AutoField(db_column='BaseBoardID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=50, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationinchassis = models.CharField(db_column='LocationInChassis', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxBaseBoard'


class Tbllinuxbios(models.Model):
    biosid = models.AutoField(db_column='BiosID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=150, blank=True, null=True)  # Field name made lowercase.
    releasedate = models.CharField(db_column='ReleaseDate', max_length=150, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, blank=True, null=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=150, blank=True, null=True)  # Field name made lowercase.
    runtimesize = models.CharField(db_column='RuntimeSize', max_length=150, blank=True, null=True)  # Field name made lowercase.
    romsize = models.CharField(db_column='ROMSize', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    releasedateutc = models.DateTimeField(db_column='ReleaseDateUtc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxBios'


class Tbllinuxenclosure(models.Model):
    linuxenclosureid = models.AutoField(db_column='LinuxEnclosureId', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    chassistypes = models.DecimalField(db_column='ChassisTypes', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lockpresent = models.BooleanField(db_column='LockPresent', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    securitystatus = models.DecimalField(db_column='SecurityStatus', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=300, blank=True, null=True)  # Field name made lowercase.
    smbiosassettag = models.CharField(db_column='SMBIOSAssetTag', max_length=300, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=300, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxEnclosure'


class Tbllinuxfileinfo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    filepath = models.CharField(db_column='FilePath', max_length=1000)  # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=500, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=100, blank=True, null=True)  # Field name made lowercase.
    size = models.IntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    found = models.BooleanField(db_column='Found')  # Field name made lowercase.
    lastaccessed = models.DateTimeField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxFileInfo'


class Tbllinuxgraphicscards(models.Model):
    graphicsid = models.AutoField(db_column='GraphicsID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=200, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=200, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    subsystemname = models.CharField(db_column='SubsystemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    subsystemmanufacturer = models.CharField(db_column='SubsystemManufacturer', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxGraphicsCards'


class Tbllinuxgroup(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=20)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxGroup'


class Tbllinuxharddisks(models.Model):
    harddiskid = models.AutoField(db_column='HardDiskID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    filesystem = models.CharField(db_column='Filesystem', max_length=400, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=30, blank=True, null=True)  # Field name made lowercase.
    used = models.CharField(db_column='Used', max_length=30, blank=True, null=True)  # Field name made lowercase.
    available = models.CharField(db_column='Available', max_length=30, blank=True, null=True)  # Field name made lowercase.
    percentage = models.CharField(db_column='Percentage', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mountedon = models.CharField(db_column='MountedOn', max_length=300, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxHardDisks'


class Tbllinuxlogicalvolume(models.Model):
    logicalvolumeid = models.AutoField(db_column='LogicalVolumeID', primary_key=True)  # Field name made lowercase.
    volumegroupid = models.ForeignKey('Tbllinuxvolumegroup', models.DO_NOTHING, db_column='VolumeGroupID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=500, blank=True, null=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='Uuid', max_length=500, blank=True, null=True)  # Field name made lowercase.
    devicemapperpath = models.CharField(db_column='DeviceMapperPath', max_length=500, blank=True, null=True)  # Field name made lowercase.
    size = models.BigIntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    blockdevice = models.CharField(db_column='BlockDevice', max_length=500, blank=True, null=True)  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxLogicalVolume'


class Tbllinuxmemorycontroller(models.Model):
    controllerid = models.AutoField(db_column='ControllerID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    supportedinterleave = models.CharField(db_column='SupportedInterleave', max_length=50, blank=True, null=True)  # Field name made lowercase.
    currentinterleave = models.CharField(db_column='CurrentInterleave', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maxmemorymodulesize = models.CharField(db_column='MaxMemoryModuleSize', max_length=20, blank=True, null=True)  # Field name made lowercase.
    maxtotalmemorysize = models.CharField(db_column='MaxTotalMemorySize', max_length=20, blank=True, null=True)  # Field name made lowercase.
    supportedspeeds = models.CharField(db_column='SupportedSpeeds', max_length=100, blank=True, null=True)  # Field name made lowercase.
    supportedmemtypes = models.CharField(db_column='SupportedMemTypes', max_length=100, blank=True, null=True)  # Field name made lowercase.
    memorymodulevoltage = models.CharField(db_column='MemoryModuleVoltage', max_length=10, blank=True, null=True)  # Field name made lowercase.
    numberofslots = models.CharField(db_column='NumberOfSlots', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxMemoryController'


class Tbllinuxmemorydevices(models.Model):
    memorydeviceid = models.AutoField(db_column='MemoryDeviceID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    totalwidth = models.CharField(db_column='TotalWidth', max_length=20, blank=True, null=True)  # Field name made lowercase.
    datawidth = models.CharField(db_column='DataWidth', max_length=20, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=20, blank=True, null=True)  # Field name made lowercase.
    formfactor = models.CharField(db_column='FormFactor', max_length=20, blank=True, null=True)  # Field name made lowercase.
    set = models.CharField(db_column='Set', max_length=20, blank=True, null=True)  # Field name made lowercase.
    locator = models.CharField(db_column='Locator', max_length=20, blank=True, null=True)  # Field name made lowercase.
    banklocator = models.CharField(db_column='BankLocator', max_length=20, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    typedetail = models.CharField(db_column='TypeDetail', max_length=40, blank=True, null=True)  # Field name made lowercase.
    speed = models.CharField(db_column='Speed', max_length=20, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=40, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxMemoryDevices'


class Tbllinuxmemorymodules(models.Model):
    memorymoduleid = models.AutoField(db_column='MemoryModuleID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    socket = models.CharField(db_column='Socket', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bankconnections = models.CharField(db_column='BankConnections', max_length=20, blank=True, null=True)  # Field name made lowercase.
    currentspeed = models.CharField(db_column='CurrentSpeed', max_length=20, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    installedsize = models.CharField(db_column='InstalledSize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enabledsize = models.CharField(db_column='EnabledSize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    errorstatus = models.CharField(db_column='ErrorStatus', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxMemoryModules'


class Tbllinuxnetworkdetection(models.Model):
    networkid = models.AutoField(db_column='NetworkID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    linkencap = models.CharField(db_column='LinkEncap', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mac = models.CharField(db_column='Mac', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ipv4 = models.CharField(db_column='Ipv4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ipv6 = models.CharField(db_column='Ipv6', max_length=200, blank=True, null=True)  # Field name made lowercase.
    broadcast = models.CharField(db_column='Broadcast', max_length=200, blank=True, null=True)  # Field name made lowercase.
    subnetmask = models.CharField(db_column='Subnetmask', max_length=200, blank=True, null=True)  # Field name made lowercase.
    scope = models.CharField(db_column='Scope', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    gateway = models.CharField(db_column='Gateway', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qdisc = models.CharField(db_column='QDisc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    master = models.CharField(db_column='Master', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mtu = models.IntegerField(db_column='Mtu', blank=True, null=True)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=200, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxNetworkDetection'


class Tbllinuxopticaldrives(models.Model):
    opticaldriveid = models.AutoField(db_column='OpticalDriveID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(db_column='Path', max_length=20, blank=True, null=True)  # Field name made lowercase.
    product = models.CharField(db_column='Product', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bus = models.CharField(db_column='Bus', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mount = models.CharField(db_column='Mount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxOpticalDrives'


class Tbllinuxpcicards(models.Model):
    pciid = models.AutoField(db_column='PciID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=300, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=300, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=300, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=300, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    subsystemname = models.CharField(db_column='SubsystemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    subsystemmanufacturer = models.CharField(db_column='SubsystemManufacturer', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxPciCards'


class Tbllinuxphysicalharddisk(models.Model):
    physicalharddiskid = models.AutoField(db_column='PhysicalHardDiskID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=500, blank=True, null=True)  # Field name made lowercase.
    size = models.BigIntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=500, blank=True, null=True)  # Field name made lowercase.
    hctl = models.CharField(db_column='Hctl', max_length=500, blank=True, null=True)  # Field name made lowercase.
    majmin = models.CharField(db_column='MajMin', max_length=500, blank=True, null=True)  # Field name made lowercase.
    hotplug = models.BooleanField(db_column='Hotplug', blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=500, blank=True, null=True)  # Field name made lowercase.
    serial = models.CharField(db_column='Serial', max_length=500, blank=True, null=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rev = models.CharField(db_column='Rev', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxPhysicalHardDisk'


class Tbllinuxphysicalprocessor(models.Model):
    physicalprocessorid = models.AutoField(db_column='PhysicalProcessorID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    modelname = models.CharField(db_column='ModelName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    modeltype = models.CharField(db_column='ModelType', max_length=500, blank=True, null=True)  # Field name made lowercase.
    stepping = models.IntegerField(db_column='Stepping', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=500, blank=True, null=True)  # Field name made lowercase.
    family = models.CharField(db_column='Family', max_length=500, blank=True, null=True)  # Field name made lowercase.
    architecture = models.CharField(db_column='Architecture', max_length=500, blank=True, null=True)  # Field name made lowercase.
    opmodes = models.CharField(db_column='OpModes', max_length=500, blank=True, null=True)  # Field name made lowercase.
    numberofphysicalcores = models.IntegerField(db_column='NumberOfPhysicalCores', blank=True, null=True)  # Field name made lowercase.
    threadsperphysicalcore = models.IntegerField(db_column='ThreadsPerPhysicalCore', blank=True, null=True)  # Field name made lowercase.
    numberoflogicalcores = models.IntegerField(db_column='NumberOfLogicalCores', blank=True, null=True)  # Field name made lowercase.
    sockets = models.IntegerField(db_column='Sockets', blank=True, null=True)  # Field name made lowercase.
    currentclockspeed = models.CharField(db_column='CurrentClockSpeed', max_length=500, blank=True, null=True)  # Field name made lowercase.
    minimumclockspeed = models.CharField(db_column='MinimumClockSpeed', max_length=500, blank=True, null=True)  # Field name made lowercase.
    maximumclockspeed = models.CharField(db_column='MaximumClockSpeed', max_length=500, blank=True, null=True)  # Field name made lowercase.
    bogomips = models.CharField(db_column='BogoMIPS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    l1dcachesize = models.CharField(db_column='L1dCacheSize', max_length=500, blank=True, null=True)  # Field name made lowercase.
    l1icachesize = models.CharField(db_column='L1iCacheSize', max_length=500, blank=True, null=True)  # Field name made lowercase.
    l2cachesize = models.CharField(db_column='L2CacheSize', max_length=500, blank=True, null=True)  # Field name made lowercase.
    l3cachesize = models.CharField(db_column='L3CacheSize', max_length=500, blank=True, null=True)  # Field name made lowercase.
    byteorder = models.CharField(db_column='ByteOrder', max_length=500, blank=True, null=True)  # Field name made lowercase.
    addresssizes = models.CharField(db_column='AddressSizes', max_length=500, blank=True, null=True)  # Field name made lowercase.
    virtualization = models.CharField(db_column='Virtualization', max_length=500, blank=True, null=True)  # Field name made lowercase.
    hypervisorvendor = models.CharField(db_column='HypervisorVendor', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxPhysicalProcessor'


class Tbllinuxphysicalvolume(models.Model):
    physicalvolumeid = models.AutoField(db_column='PhysicalVolumeID', primary_key=True)  # Field name made lowercase.
    volumegroupid = models.ForeignKey('Tbllinuxvolumegroup', models.DO_NOTHING, db_column='VolumeGroupID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=500, blank=True, null=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='Uuid', max_length=500, blank=True, null=True)  # Field name made lowercase.
    size = models.BigIntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    free = models.BigIntegerField(db_column='Free', blank=True, null=True)  # Field name made lowercase.
    used = models.BigIntegerField(db_column='Used', blank=True, null=True)  # Field name made lowercase.
    inuse = models.CharField(db_column='InUse', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxPhysicalVolume'


class Tbllinuxprocessors(models.Model):
    processorid = models.AutoField(db_column='ProcessorID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    socket = models.CharField(db_column='Socket', max_length=200, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=200, blank=True, null=True)  # Field name made lowercase.
    family = models.CharField(db_column='Family', max_length=200, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=200, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=200, blank=True, null=True)  # Field name made lowercase.
    voltage = models.CharField(db_column='Voltage', max_length=200, blank=True, null=True)  # Field name made lowercase.
    externalclock = models.CharField(db_column='ExternalClock', max_length=200, blank=True, null=True)  # Field name made lowercase.
    maxspeed = models.CharField(db_column='MaxSpeed', max_length=200, blank=True, null=True)  # Field name made lowercase.
    currentspeed = models.CharField(db_column='CurrentSpeed', max_length=200, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=200, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxProcessors'


class Tbllinuxsoftware(models.Model):
    softwareid = models.AutoField(db_column='SoftwareID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    softwareuniid = models.ForeignKey('Tblsoftwareuni', models.DO_NOTHING, db_column='SoftwareUniID')  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=50, blank=True, null=True)  # Field name made lowercase.
    release = models.CharField(db_column='Release', max_length=50, blank=True, null=True)  # Field name made lowercase.
    architecture = models.CharField(db_column='Architecture', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desired = models.CharField(db_column='Desired', max_length=20, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    error = models.CharField(db_column='Error', max_length=20, blank=True, null=True)  # Field name made lowercase.
    installdate = models.CharField(db_column='InstallDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    installdateutc = models.DateTimeField(db_column='InstallDateUtc', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    size = models.BigIntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    type = models.ForeignKey('Tsyslinuxsoftwaretype', models.DO_NOTHING, db_column='Type')  # Field name made lowercase.
    path = models.CharField(db_column='Path', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    catalogsoftwareid = models.ForeignKey(Tblcatalogsoftware, models.DO_NOTHING, db_column='CatalogSoftwareId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxSoftware'


class Tbllinuxsoundcards(models.Model):
    soundid = models.AutoField(db_column='SoundID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    card = models.CharField(db_column='Card', max_length=300, blank=True, null=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parent = models.CharField(db_column='Parent', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=200, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    subsystemname = models.CharField(db_column='SubsystemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    subsystemmanufacturer = models.CharField(db_column='SubsystemManufacturer', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxSoundCards'


class Tbllinuxsystem(models.Model):
    systemid = models.AutoField(db_column='SystemID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=150, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=150, blank=True, null=True)  # Field name made lowercase.
    serial = models.CharField(db_column='Serial', max_length=150, blank=True, null=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='UUID', max_length=150, blank=True, null=True)  # Field name made lowercase.
    wakeuptime = models.CharField(db_column='WakeupTime', max_length=150, blank=True, null=True)  # Field name made lowercase.
    bootstatus = models.CharField(db_column='BootStatus', max_length=150, blank=True, null=True)  # Field name made lowercase.
    networknodehostname = models.CharField(db_column='NetworkNodeHostname', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kernelname = models.CharField(db_column='KernelName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kernelrelease = models.CharField(db_column='KernelRelease', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kernelversion = models.CharField(db_column='KernelVersion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    machinehardwarename = models.CharField(db_column='MachineHardwareName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    processortype = models.CharField(db_column='ProcessorType', max_length=150, blank=True, null=True)  # Field name made lowercase.
    hardwareplatform = models.CharField(db_column='HardwarePlatform', max_length=150, blank=True, null=True)  # Field name made lowercase.
    operatingsystem = models.CharField(db_column='OperatingSystem', max_length=150, blank=True, null=True)  # Field name made lowercase.
    osrelease = models.CharField(db_column='OSRelease', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    systemsku = models.CharField(db_column='SystemSku', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxSystem'


class Tbllinuxuser(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupId')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=20)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    homedirectory = models.TextField(db_column='HomeDirectory', blank=True, null=True)  # Field name made lowercase.
    loginshell = models.TextField(db_column='LoginShell', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxUser'


class Tbllinuxusergroupmembership(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    memberuserid = models.IntegerField(db_column='MemberUserId')  # Field name made lowercase.
    membergroupid = models.ForeignKey(Tbllinuxgroup, models.DO_NOTHING, db_column='MemberGroupId')  # Field name made lowercase.
    assetid = models.IntegerField(db_column='AssetId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxUserGroupMembership'


class Tbllinuxuserlogon(models.Model):
    id = models.OneToOneField(Tbllinuxuser, models.DO_NOTHING, db_column='Id', primary_key=True)  # Field name made lowercase.
    port = models.CharField(db_column='Port', max_length=40)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IpAddress', max_length=15)  # Field name made lowercase.
    logontime = models.DateTimeField(db_column='LogonTime')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxUserLogon'


class Tbllinuxvolumegroup(models.Model):
    volumegroupid = models.AutoField(db_column='VolumeGroupID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=500, blank=True, null=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='Uuid', max_length=500, blank=True, null=True)  # Field name made lowercase.
    size = models.BigIntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    free = models.BigIntegerField(db_column='Free', blank=True, null=True)  # Field name made lowercase.
    access = models.CharField(db_column='Access', max_length=500, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=500, blank=True, null=True)  # Field name made lowercase.
    format = models.CharField(db_column='Format', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxVolumeGroup'


class Tbllinuxvolumes(models.Model):
    volumeid = models.AutoField(db_column='VolumeID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mounted = models.CharField(db_column='Mounted', max_length=20, blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(db_column='Path', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mountpoint = models.CharField(db_column='MountPoint', max_length=50, blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLinuxVolumes'


class Tblloginlog(models.Model):
    logid = models.AutoField(db_column='LogID', primary_key=True)  # Field name made lowercase.
    success = models.BooleanField(db_column='Success')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=500)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    cert = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblLoginLog'


class Tbllsagentasset(models.Model):
    lsagentassetid = models.CharField(db_column='LsAgentAssetID', primary_key=True, max_length=36)  # Field name made lowercase.
    status = models.ForeignKey('Tbllsagentassetstate', models.DO_NOTHING, db_column='Status')  # Field name made lowercase.
    computerunique = models.CharField(db_column='ComputerUnique', max_length=500, blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    lsagentgroupid = models.ForeignKey('Tbllsagentgroup', models.DO_NOTHING, db_column='LsAgentGroupID', blank=True, null=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID', blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=20, blank=True, null=True)  # Field name made lowercase.
    assettype = models.IntegerField(db_column='AssetType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLsAgentAsset'


class Tbllsagentassetstate(models.Model):
    id = models.IntegerField(primary_key=True)
    statename = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblLsAgentAssetState'


class Tbllsagentgroup(models.Model):
    lsagentgroupid = models.CharField(db_column='LsAgentGroupID', primary_key=True, max_length=36)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.
    default = models.BooleanField(db_column='Default')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    scheduleid = models.ForeignKey('Tsysschedule', models.DO_NOTHING, db_column='ScheduleID', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    autoupdate = models.BooleanField(db_column='AutoUpdate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLsAgentGroup'


class Tbllsagentgroupurl(models.Model):
    lsagentgroupurlid = models.CharField(db_column='LsAgentGroupUrlID', primary_key=True, max_length=36)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    lsagentgroupid = models.ForeignKey(Tbllsagentgroup, models.DO_NOTHING, db_column='LsAgentGroupID')  # Field name made lowercase.
    servername = models.ForeignKey('Tsysasservers', models.DO_NOTHING, db_column='ServerName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLsAgentGroupUrl'


class Tbllsagentrelayconfig(models.Model):
    lsagentrelayconfigid = models.CharField(db_column='LsAgentRelayConfigID', primary_key=True, max_length=36)  # Field name made lowercase.
    servername = models.ForeignKey('Tsysasservers', models.DO_NOTHING, db_column='Servername', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    retrysendattempts = models.IntegerField(db_column='RetrySendAttempts')  # Field name made lowercase.
    retrysendtime = models.IntegerField(db_column='RetrySendTime')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    relaykey = models.CharField(db_column='RelayKey', max_length=36, blank=True, null=True)  # Field name made lowercase.
    agentkey = models.CharField(db_column='AgentKey', max_length=36, blank=True, null=True)  # Field name made lowercase.
    lastdatasync = models.DateTimeField(db_column='LastDataSync', blank=True, null=True)  # Field name made lowercase.
    lastconfigsync = models.DateTimeField(db_column='LastConfigSync', blank=True, null=True)  # Field name made lowercase.
    requestvalidation = models.BooleanField(db_column='RequestValidation')  # Field name made lowercase.
    requestoverride = models.BooleanField(db_column='RequestOverride')  # Field name made lowercase.
    overrideavailable = models.BooleanField(db_column='OverrideAvailable')  # Field name made lowercase.
    requestdisable = models.BooleanField(db_column='RequestDisable')  # Field name made lowercase.
    relayerrormessage = models.CharField(db_column='RelayErrorMessage', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLsAgentRelayConfig'


class Tbllsagenturl(models.Model):
    lsagenturlid = models.CharField(db_column='LsAgentUrlID', primary_key=True, max_length=36)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLsAgentUrl'


class Tblmacapplications(models.Model):
    applicationid = models.AutoField(db_column='ApplicationID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    softid = models.IntegerField()
    version = models.CharField(db_column='Version', max_length=200, blank=True, null=True)  # Field name made lowercase.
    installdate = models.DateTimeField(db_column='InstallDate', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(db_column='Path', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    runtimeenvironment = models.CharField(db_column='RuntimeEnvironment', max_length=100, blank=True, null=True)  # Field name made lowercase.
    has64bitintelcode = models.BooleanField(db_column='Has64BitIntelCode', blank=True, null=True)  # Field name made lowercase.
    catalogsoftwareid = models.ForeignKey(Tblcatalogsoftware, models.DO_NOTHING, db_column='CatalogSoftwareId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMacApplications'


class Tblmacdiscburning(models.Model):
    discburningid = models.AutoField(db_column='DiscBurningID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    firmware = models.CharField(db_column='Firmware', max_length=20, blank=True, null=True)  # Field name made lowercase.
    interconnect = models.CharField(db_column='Interconnect', max_length=50, blank=True, null=True)  # Field name made lowercase.
    burnsupport = models.CharField(db_column='BurnSupport', max_length=50, blank=True, null=True)  # Field name made lowercase.
    burnunderrunprotection = models.BooleanField(db_column='BurnUnderrunProtection', blank=True, null=True)  # Field name made lowercase.
    cache = models.CharField(db_column='Cache', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cdwrite = models.CharField(db_column='CDWrite', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dvdwrite = models.CharField(db_column='DVDWrite', max_length=50, blank=True, null=True)  # Field name made lowercase.
    media = models.BooleanField(db_column='Media', blank=True, null=True)  # Field name made lowercase.
    readdvd = models.BooleanField(db_column='ReadDVD', blank=True, null=True)  # Field name made lowercase.
    writestrategies = models.CharField(db_column='WriteStrategies', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMacDiscBurning'


class Tblmacdisplays(models.Model):
    displayid = models.AutoField(db_column='DisplayID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    devicetype = models.CharField(db_column='DeviceType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    displaytype = models.CharField(db_column='DisplayType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    builtin = models.BooleanField(db_column='BuiltIn', blank=True, null=True)  # Field name made lowercase.
    depth = models.CharField(db_column='Depth', max_length=50, blank=True, null=True)  # Field name made lowercase.
    main = models.BooleanField(db_column='Main', blank=True, null=True)  # Field name made lowercase.
    mirror = models.CharField(db_column='Mirror', max_length=20, blank=True, null=True)  # Field name made lowercase.
    online = models.BooleanField(db_column='Online', blank=True, null=True)  # Field name made lowercase.
    resolution = models.CharField(db_column='Resolution', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coreimage = models.CharField(db_column='CoreImage', max_length=50, blank=True, null=True)  # Field name made lowercase.
    quartzextreme = models.CharField(db_column='QuartzExtreme', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMacDisplays'


class Tblmacfirewires(models.Model):
    firewireid = models.AutoField(db_column='FireWireID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maxspeed = models.CharField(db_column='MaxSpeed', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMacFireWires'


class Tblmachwoverview(models.Model):
    hwoverviewid = models.AutoField(db_column='HwOverviewID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    machinename = models.CharField(db_column='MachineName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    machinemodel = models.CharField(db_column='MachineModel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cputype = models.CharField(db_column='CPUType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nrofcpus = models.IntegerField(db_column='NrOfCPUs', blank=True, null=True)  # Field name made lowercase.
    cpuspeed = models.CharField(db_column='CPUSpeed', max_length=50, blank=True, null=True)  # Field name made lowercase.
    l2cachepercpu = models.CharField(db_column='L2CachePerCPU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    memory = models.CharField(db_column='Memory', max_length=50, blank=True, null=True)  # Field name made lowercase.
    busspeed = models.CharField(db_column='BusSpeed', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bootromversion = models.CharField(db_column='BootROMVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    packages = models.IntegerField(db_column='Packages', blank=True, null=True)  # Field name made lowercase.
    platformuuid = models.CharField(db_column='PlatformUUID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smcversionsystem = models.CharField(db_column='SMCVersionSystem', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMacHwOverview'


class Tblmacmemory(models.Model):
    memoryid = models.AutoField(db_column='MemoryID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=20, blank=True, null=True)  # Field name made lowercase.
    speed = models.CharField(db_column='Speed', max_length=20, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMacMemory'


class Tblmacmodems(models.Model):
    modemid = models.AutoField(db_column='ModemID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=50, blank=True, null=True)  # Field name made lowercase.
    interfacetype = models.CharField(db_column='InterfaceType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    modulation = models.CharField(db_column='Modulation', max_length=20, blank=True, null=True)  # Field name made lowercase.
    hwversion = models.CharField(db_column='HwVersion', max_length=20, blank=True, null=True)  # Field name made lowercase.
    driverinfo = models.CharField(db_column='DriverInfo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    countryinfo = models.CharField(db_column='CountryInfo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMacModems'


class Tblmacnetwork(models.Model):
    networkid = models.AutoField(db_column='NetworkID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    serviceorder = models.IntegerField(db_column='ServiceOrder', blank=True, null=True)  # Field name made lowercase.
    hardware = models.CharField(db_column='Hardware', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bsddevicename = models.CharField(db_column='BSDDeviceName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    mac = models.CharField(db_column='Mac', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ipv4 = models.CharField(db_column='Ipv4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ipv4mask = models.CharField(db_column='Ipv4Mask', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ipv6 = models.CharField(db_column='IPv6', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ipv6prefix = models.CharField(db_column='IPv6Prefix', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gateway = models.CharField(db_column='Gateway', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMacNetwork'


class Tblmacnetworkvolumes(models.Model):
    networkvolumeid = models.AutoField(db_column='NetworkVolumeID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    automounted = models.BooleanField(db_column='AutoMounted', blank=True, null=True)  # Field name made lowercase.
    mountedfrom = models.CharField(db_column='MountedFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mountpoint = models.CharField(db_column='MountPoint', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMacNetworkVolumes'


class Tblmacosinfo(models.Model):
    macosinfoid = models.AutoField(db_column='MacOSInfoId', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    systemversion = models.CharField(db_column='SystemVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kernelversion = models.CharField(db_column='KernelVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bootvolume = models.CharField(db_column='BootVolume', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bootmode = models.CharField(db_column='BootMode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    computername = models.CharField(db_column='ComputerName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    securevirtualmemory = models.CharField(db_column='SecureVirtualMemory', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sixtyfourbitkernelandexts = models.CharField(db_column='SixtyFourBitKernelAndExts', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMacOSInfo'


class Tblmacpartitions(models.Model):
    harddiskid = models.AutoField(db_column='HardDiskID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    filesystem = models.CharField(db_column='Filesystem', max_length=300, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=20, blank=True, null=True)  # Field name made lowercase.
    used = models.CharField(db_column='Used', max_length=20, blank=True, null=True)  # Field name made lowercase.
    available = models.CharField(db_column='Available', max_length=20, blank=True, null=True)  # Field name made lowercase.
    percentage = models.CharField(db_column='Percentage', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mountedon = models.CharField(db_column='MountedOn', max_length=300, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMacPartitions'


class Tblmappeddrives(models.Model):
    driveid = models.AutoField(db_column='DriveID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=300, blank=True, null=True)  # Field name made lowercase.
    driveletter = models.CharField(db_column='Driveletter', max_length=3, blank=True, null=True)  # Field name made lowercase.
    remotepath = models.CharField(db_column='RemotePath', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMappedDrives'


class Tblmetricsquerydefinition(models.Model):
    metricsquerydefinitionid = models.CharField(db_column='MetricsQueryDefinitionId', primary_key=True, max_length=36)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    prerequisitesql = models.CharField(db_column='PrerequisiteSql', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    sql = models.CharField(db_column='Sql', max_length=4000)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255)  # Field name made lowercase.
    lastupdatedate = models.DateTimeField(db_column='LastUpdateDate')  # Field name made lowercase.
    data = models.TextField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMetricsQueryDefinition'


class Tblmonitor(models.Model):
    monitorid = models.AutoField(db_column='MonitorID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    monitormodel = models.CharField(db_column='MonitorModel', max_length=300, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    monitormanufacturer = models.CharField(db_column='MonitorManufacturer', max_length=400, blank=True, null=True)  # Field name made lowercase.
    manufactureddate = models.DateTimeField(db_column='ManufacturedDate', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    pnpdeviceid = models.CharField(db_column='PNPDeviceID', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMonitor'


class Tblmonitorhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    monitormodel = models.CharField(db_column='MonitorModel', max_length=300, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    monitormanufacturer = models.CharField(db_column='MonitorManufacturer', max_length=300, blank=True, null=True)  # Field name made lowercase.
    manufactureddate = models.DateTimeField(db_column='ManufacturedDate', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.
    pnpdeviceid = models.CharField(db_column='PNPDeviceID', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMonitorHist'


class Tblnetwork(models.Model):
    networkid = models.AutoField(db_column='NetworkID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    databasepath = models.CharField(db_column='Databasepath', max_length=500, blank=True, null=True)  # Field name made lowercase.
    defaultipgateway = models.CharField(db_column='DefaultIPGateway', max_length=500, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=450, blank=True, null=True)  # Field name made lowercase.
    dhcpenabled = models.BooleanField(db_column='DHCPenabled', blank=True, null=True)  # Field name made lowercase.
    dhcpserver = models.CharField(db_column='DHCPserver', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dnsdomain = models.CharField(db_column='DNSDomain', max_length=450, blank=True, null=True)  # Field name made lowercase.
    dnsdomainsuffixsearchorder = models.CharField(db_column='DNSDomainSuffixSearchOrder', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    dnsenabledforwinsresolution = models.BooleanField(db_column='DNSEnabledForWinsResolution', blank=True, null=True)  # Field name made lowercase.
    dnshostname = models.CharField(db_column='DNSHostname', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dnsserversearchorder = models.CharField(db_column='DNSServerSearchOrder', max_length=500, blank=True, null=True)  # Field name made lowercase.
    domaindnsregistrationenabled = models.BooleanField(db_column='DomainDNSRegistrationEnabled', blank=True, null=True)  # Field name made lowercase.
    fulldnsregistrationenabled = models.BooleanField(db_column='FullDNSRegistrationEnabled', blank=True, null=True)  # Field name made lowercase.
    gatewaycostmetric = models.CharField(db_column='GatewayCostMetric', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    ipconnectionmetric = models.DecimalField(db_column='IPConnectionMetric', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ipenabled = models.BooleanField(db_column='IPEnabled', blank=True, null=True)  # Field name made lowercase.
    ipfiltersecurityenabled = models.BooleanField(db_column='IPFiltersecurityEnabled', blank=True, null=True)  # Field name made lowercase.
    ipportsecurityenabled = models.BooleanField(db_column='IPPortSecurityEnabled', blank=True, null=True)  # Field name made lowercase.
    ipsecpermitipprotocols = models.CharField(db_column='IPSecPermitIPProtocols', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ipsecpermittcpports = models.CharField(db_column='IPSecPermitTCPPorts', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ipsubnet = models.CharField(db_column='IPSubnet', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACaddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    servicename = models.CharField(db_column='ServiceName', max_length=900, blank=True, null=True)  # Field name made lowercase.
    tcpipnetbiosoptions = models.DecimalField(db_column='TcpipNetbiosOptions', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    winsenablelmhostslookup = models.BooleanField(db_column='WINSEnableLMHostsLookup', blank=True, null=True)  # Field name made lowercase.
    winsprimaryserver = models.CharField(db_column='WINSPrimaryserver', max_length=50, blank=True, null=True)  # Field name made lowercase.
    winsscopeid = models.CharField(db_column='WINSScopeID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    winssecondaryserver = models.CharField(db_column='WINSSecondaryserver', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    index = models.IntegerField(db_column='Index', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblNetwork'


class Tblnetworkadapter(models.Model):
    networkadapterid = models.BigAutoField(primary_key=True)
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=300, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=300, blank=True, null=True)  # Field name made lowercase.
    netconnectionid = models.CharField(db_column='NetConnectionID', max_length=300, blank=True, null=True)  # Field name made lowercase.
    netenabled = models.BooleanField(db_column='NetEnabled', blank=True, null=True)  # Field name made lowercase.
    speed = models.BigIntegerField(db_column='Speed', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblNetworkAdapter'


class Tblnetworkclient(models.Model):
    win32_networkclientid = models.AutoField(db_column='Win32_NetworkClientid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblNetworkClient'


class Tblnetworkclienthist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblNetworkClientHist'


class Tblnetworkhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    databasepath = models.CharField(db_column='Databasepath', max_length=500, blank=True, null=True)  # Field name made lowercase.
    defaultipgateway = models.CharField(db_column='DefaultIPGateway', max_length=500, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=450, blank=True, null=True)  # Field name made lowercase.
    dhcpenabled = models.BooleanField(db_column='DHCPenabled', blank=True, null=True)  # Field name made lowercase.
    dhcpserver = models.CharField(db_column='DHCPserver', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dnsdomain = models.CharField(db_column='DNSDomain', max_length=450, blank=True, null=True)  # Field name made lowercase.
    dnsdomainsuffixsearchorder = models.CharField(db_column='DNSDomainSuffixSearchOrder', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    dnsenabledforwinsresolution = models.BooleanField(db_column='DNSEnabledForWinsResolution', blank=True, null=True)  # Field name made lowercase.
    dnshostname = models.CharField(db_column='DNSHostname', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dnsserversearchorder = models.CharField(db_column='DNSServerSearchOrder', max_length=500, blank=True, null=True)  # Field name made lowercase.
    domaindnsregistrationenabled = models.BooleanField(db_column='DomainDNSRegistrationEnabled', blank=True, null=True)  # Field name made lowercase.
    fulldnsregistrationenabled = models.BooleanField(db_column='FullDNSRegistrationEnabled', blank=True, null=True)  # Field name made lowercase.
    gatewaycostmetric = models.CharField(db_column='GatewayCostMetric', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ipconnectionmetric = models.DecimalField(db_column='IPConnectionMetric', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ipenabled = models.BooleanField(db_column='IPEnabled', blank=True, null=True)  # Field name made lowercase.
    ipfiltersecurityenabled = models.BooleanField(db_column='IPFiltersecurityEnabled', blank=True, null=True)  # Field name made lowercase.
    ipportsecurityenabled = models.BooleanField(db_column='IPPortSecurityEnabled', blank=True, null=True)  # Field name made lowercase.
    ipsecpermitipprotocols = models.CharField(db_column='IPSecPermitIPProtocols', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ipsecpermittcpports = models.CharField(db_column='IPSecPermitTCPPorts', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ipsubnet = models.CharField(db_column='IPSubnet', max_length=500, blank=True, null=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACaddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    servicename = models.CharField(db_column='ServiceName', max_length=900, blank=True, null=True)  # Field name made lowercase.
    tcpipnetbiosoptions = models.DecimalField(db_column='TcpipNetbiosOptions', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    winsenablelmhostslookup = models.BooleanField(db_column='WINSEnableLMHostsLookup', blank=True, null=True)  # Field name made lowercase.
    winsprimaryserver = models.CharField(db_column='WINSPrimaryserver', max_length=50, blank=True, null=True)  # Field name made lowercase.
    winsscopeid = models.CharField(db_column='WINSScopeID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    winssecondaryserver = models.CharField(db_column='WINSSecondaryserver', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    index = models.IntegerField(db_column='Index', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblNetworkHist'


class Tblnotification(models.Model):
    notificationid = models.CharField(db_column='NotificationId', primary_key=True, max_length=36)  # Field name made lowercase.
    notificationcategoryid = models.ForeignKey('Tblnotificationcategory', models.DO_NOTHING, db_column='NotificationCategoryId')  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=4000)  # Field name made lowercase.
    expirationdate = models.DateTimeField(db_column='ExpirationDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblNotification'


class Tblnotificationcategory(models.Model):
    notificationcategoryid = models.IntegerField(db_column='NotificationCategoryId', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=100)  # Field name made lowercase.
    isselected = models.BooleanField(db_column='IsSelected')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=4000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblNotificationCategory'


class Tblnotificationuser(models.Model):
    notificationuserid = models.AutoField(db_column='NotificationUserId', primary_key=True)  # Field name made lowercase.
    notificationid = models.ForeignKey(Tblnotification, models.DO_NOTHING, db_column='NotificationId')  # Field name made lowercase.
    userid = models.ForeignKey(Htblusers, models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblNotificationUser'


class Tblntlog(models.Model):
    eventlogid = models.BigAutoField(db_column='EventlogID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    eventcode = models.IntegerField(db_column='Eventcode', blank=True, null=True)  # Field name made lowercase.
    eventtype = models.SmallIntegerField(db_column='Eventtype', blank=True, null=True)  # Field name made lowercase.
    logfileid = models.ForeignKey('Tblntlogfile', models.DO_NOTHING, db_column='LogfileID', blank=True, null=True)  # Field name made lowercase.
    messageid = models.ForeignKey('Tblntlogmessage', models.DO_NOTHING, db_column='MessageID', blank=True, null=True)  # Field name made lowercase.
    sourcenameid = models.ForeignKey('Tblntlogsource', models.DO_NOTHING, db_column='SourcenameID', blank=True, null=True)  # Field name made lowercase.
    loguserid = models.ForeignKey('Tblntloguser', models.DO_NOTHING, db_column='LoguserID', blank=True, null=True)  # Field name made lowercase.
    timegenerated = models.DateTimeField(db_column='TimeGenerated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblNtlog'


class Tblntlogfile(models.Model):
    logfileid = models.AutoField(db_column='LogfileID', primary_key=True)  # Field name made lowercase.
    logfile = models.CharField(db_column='Logfile', unique=True, max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblNtlogFile'


class Tblntlogmessage(models.Model):
    messageid = models.AutoField(db_column='MessageID', primary_key=True)  # Field name made lowercase.
    hash = models.CharField(db_column='Hash', unique=True, max_length=40)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=3900)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblNtlogMessage'


class Tblntlogsource(models.Model):
    sourcenameid = models.AutoField(db_column='SourcenameID', primary_key=True)  # Field name made lowercase.
    sourcename = models.CharField(db_column='Sourcename', unique=True, max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblNtlogSource'


class Tblntloguser(models.Model):
    loguserid = models.AutoField(db_column='LoguserID', primary_key=True)  # Field name made lowercase.
    loguser = models.CharField(db_column='Loguser', unique=True, max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblNtlogUser'


class Tblo365Activesyncdevice(models.Model):
    activesyncdeviceid = models.AutoField(db_column='ActiveSyncDeviceId', primary_key=True)  # Field name made lowercase.
    organizationid = models.ForeignKey('Tblo365Organization', models.DO_NOTHING, db_column='OrganizationId')  # Field name made lowercase.
    clienttype = models.CharField(db_column='ClientType', max_length=150, blank=True, null=True)  # Field name made lowercase.
    deviceaccesscontrolrule = models.CharField(db_column='DeviceAccessControlRule', max_length=150, blank=True, null=True)  # Field name made lowercase.
    deviceaccessstate = models.CharField(db_column='DeviceAccessState', max_length=150, blank=True, null=True)  # Field name made lowercase.
    deviceaccessstatereason = models.CharField(db_column='DeviceAccessStateReason', max_length=256, blank=True, null=True)  # Field name made lowercase.
    deviceactivesyncversion = models.CharField(db_column='DeviceActiveSyncVersion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    devicefriendlyname = models.CharField(db_column='DeviceFriendlyName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    devicemodel = models.CharField(db_column='DeviceModel', max_length=256, blank=True, null=True)  # Field name made lowercase.
    deviceos = models.CharField(db_column='DeviceOs', max_length=256, blank=True, null=True)  # Field name made lowercase.
    devicepolicyapplicationstatus = models.CharField(db_column='DevicePolicyApplicationStatus', max_length=150, blank=True, null=True)  # Field name made lowercase.
    devicetype = models.CharField(db_column='DeviceType', max_length=256, blank=True, null=True)  # Field name made lowercase.
    deviceuseragent = models.CharField(db_column='DeviceUserAgent', max_length=500, blank=True, null=True)  # Field name made lowercase.
    devicewiperequesttime = models.DateTimeField(db_column='DeviceWipeRequestTime', blank=True, null=True)  # Field name made lowercase.
    devicewipesenttime = models.DateTimeField(db_column='DeviceWipeSentTime', blank=True, null=True)  # Field name made lowercase.
    devicewipeacktime = models.DateTimeField(db_column='DeviceWipeAckTime', blank=True, null=True)  # Field name made lowercase.
    firstsynctime = models.DateTimeField(db_column='FirstSyncTime', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36, blank=True, null=True)  # Field name made lowercase.
    identity = models.CharField(db_column='Identity', max_length=256, blank=True, null=True)  # Field name made lowercase.
    lastpolicyupdatetime = models.DateTimeField(db_column='LastPolicyUpdateTime', blank=True, null=True)  # Field name made lowercase.
    lastsyncattempttime = models.DateTimeField(db_column='LastSyncAttemptTime', blank=True, null=True)  # Field name made lowercase.
    lastsuccesssync = models.DateTimeField(db_column='LastSuccessSync', blank=True, null=True)  # Field name made lowercase.
    lastdevicewiperequestor = models.CharField(db_column='LastDeviceWipeRequestor', max_length=256, blank=True, null=True)  # Field name made lowercase.
    mailbox = models.CharField(db_column='Mailbox', max_length=256, blank=True, null=True)  # Field name made lowercase.
    deviceimei = models.CharField(db_column='DeviceImei', max_length=100, blank=True, null=True)  # Field name made lowercase.
    deviceoslanguage = models.CharField(db_column='DeviceOSLanguage', max_length=50, blank=True, null=True)  # Field name made lowercase.
    devicephonenumber = models.CharField(db_column='DevicePhoneNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    devicemobileoperator = models.CharField(db_column='DeviceMobileOperator', max_length=100, blank=True, null=True)  # Field name made lowercase.
    numberoffolderssynced = models.IntegerField(db_column='NumberOfFoldersSynced', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblO365ActiveSyncDevice'


class Tblo365Assignedlicense(models.Model):
    assignedlicenseid = models.AutoField(db_column='AssignedLicenseId', primary_key=True)  # Field name made lowercase.
    licenseid = models.ForeignKey('Tblo365License', models.DO_NOTHING, db_column='LicenseId')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblO365AssignedLicense'


class Tblo365Assignedplan(models.Model):
    planid = models.AutoField(db_column='PlanId', primary_key=True)  # Field name made lowercase.
    organizationid = models.ForeignKey('Tblo365Organization', models.DO_NOTHING, db_column='OrganizationId')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    serviceplanid = models.CharField(db_column='ServicePlanId', max_length=36)  # Field name made lowercase.
    service = models.CharField(db_column='Service', max_length=256)  # Field name made lowercase.
    capabilitystatus = models.CharField(db_column='CapabilityStatus', max_length=32)  # Field name made lowercase.
    assignedtimestamp = models.DateTimeField(db_column='AssignedTimeStamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblO365AssignedPlan'


class Tblo365Contact(models.Model):
    contactid = models.AutoField(db_column='ContactId', primary_key=True)  # Field name made lowercase.
    organizationid = models.ForeignKey('Tblo365Organization', models.DO_NOTHING, db_column='OrganizationId')  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=256)  # Field name made lowercase.
    mail = models.CharField(db_column='Mail', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblO365Contact'


class Tblo365Domain(models.Model):
    domainid = models.AutoField(db_column='DomainId', primary_key=True)  # Field name made lowercase.
    domainname = models.CharField(db_column='DomainName', max_length=256)  # Field name made lowercase.
    organizationid = models.ForeignKey('Tblo365Organization', models.DO_NOTHING, db_column='OrganizationId')  # Field name made lowercase.
    authenticationtype = models.CharField(db_column='AuthenticationType', max_length=32, blank=True, null=True)  # Field name made lowercase.
    isadminmanaged = models.BooleanField(db_column='IsAdminManaged', blank=True, null=True)  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='IsDefault', blank=True, null=True)  # Field name made lowercase.
    isinitial = models.BooleanField(db_column='IsInitial', blank=True, null=True)  # Field name made lowercase.
    isroot = models.BooleanField(db_column='IsRoot', blank=True, null=True)  # Field name made lowercase.
    isverified = models.BooleanField(db_column='IsVerified', blank=True, null=True)  # Field name made lowercase.
    supportedservices = models.CharField(db_column='SupportedServices', max_length=512, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=256, blank=True, null=True)  # Field name made lowercase.
    availabilitystatus = models.CharField(db_column='AvailabilityStatus', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblO365Domain'


class Tblo365Group(models.Model):
    groupid = models.AutoField(db_column='GroupId', primary_key=True)  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectId', max_length=36)  # Field name made lowercase.
    organizationid = models.ForeignKey('Tblo365Organization', models.DO_NOTHING, db_column='OrganizationId')  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    mailenabled = models.BooleanField(db_column='MailEnabled')  # Field name made lowercase.
    securityenabled = models.BooleanField(db_column='SecurityEnabled')  # Field name made lowercase.
    mail = models.CharField(db_column='Mail', max_length=256, blank=True, null=True)  # Field name made lowercase.
    mailnickname = models.CharField(db_column='MailNickname', max_length=256, blank=True, null=True)  # Field name made lowercase.
    proxyaddresses = models.CharField(db_column='ProxyAddresses', max_length=4000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblO365Group'


class Tblo365Groupmember(models.Model):
    memberid = models.AutoField(db_column='MemberId', primary_key=True)  # Field name made lowercase.
    groupid = models.ForeignKey(Tblo365Group, models.DO_NOTHING, db_column='GroupId')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblO365GroupMember'


class Tblo365License(models.Model):
    licenseid = models.AutoField(db_column='LicenseId', primary_key=True)  # Field name made lowercase.
    organizationid = models.ForeignKey('Tblo365Organization', models.DO_NOTHING, db_column='OrganizationId')  # Field name made lowercase.
    skuid = models.CharField(db_column='SkuId', max_length=36)  # Field name made lowercase.
    capabilitystatus = models.CharField(db_column='CapabilityStatus', max_length=128)  # Field name made lowercase.
    consumedunits = models.IntegerField(db_column='ConsumedUnits')  # Field name made lowercase.
    prepaidunitsenabled = models.IntegerField(db_column='PrepaidUnitsEnabled')  # Field name made lowercase.
    prepaidunitssuspended = models.IntegerField(db_column='PrepaidUnitsSuspended')  # Field name made lowercase.
    prepaidunitswarning = models.IntegerField(db_column='PrepaidUnitsWarning')  # Field name made lowercase.
    skupartnumber = models.CharField(db_column='SkuPartNumber', max_length=150)  # Field name made lowercase.
    appliesto = models.CharField(db_column='AppliesTo', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblO365License'


class Tblo365Mailbox(models.Model):
    mailboxid = models.AutoField(db_column='MailboxId', primary_key=True)  # Field name made lowercase.
    organizationid = models.ForeignKey('Tblo365Organization', models.DO_NOTHING, db_column='OrganizationId')  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    primaryemail = models.CharField(db_column='PrimaryEmail', max_length=256, blank=True, null=True)  # Field name made lowercase.
    emailaddresses = models.CharField(db_column='EmailAddresses', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    alias = models.CharField(db_column='Alias', max_length=256, blank=True, null=True)  # Field name made lowercase.
    recipienttype = models.CharField(db_column='RecipientType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recipienttypedetails = models.CharField(db_column='RecipientTypeDetails', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userprincipalname = models.CharField(db_column='UserPrincipalName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    identity = models.CharField(db_column='Identity', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblO365Mailbox'


class Tblo365Organization(models.Model):
    organizationid = models.AutoField(db_column='OrganizationId', primary_key=True)  # Field name made lowercase.
    tenantid = models.CharField(db_column='TenantId', max_length=36)  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=16, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=500, blank=True, null=True)  # Field name made lowercase.
    countryname = models.CharField(db_column='CountryName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=16, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=300, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=500, blank=True, null=True)  # Field name made lowercase.
    telephonenumber = models.CharField(db_column='TelephoneNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    companylastdirsynctime = models.DateTimeField(db_column='CompanyLastDirSyncTime', blank=True, null=True)  # Field name made lowercase.
    dirsyncenabled = models.BooleanField(db_column='DirSyncEnabled', blank=True, null=True)  # Field name made lowercase.
    lastscan = models.DateTimeField(db_column='LastScan')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblO365Organization'


class Tblo365Serviceplan(models.Model):
    planid = models.AutoField(db_column='PlanId', primary_key=True)  # Field name made lowercase.
    licenseid = models.ForeignKey(Tblo365License, models.DO_NOTHING, db_column='LicenseId')  # Field name made lowercase.
    serviceplanid = models.CharField(db_column='ServicePlanId', max_length=36)  # Field name made lowercase.
    serviceplanname = models.CharField(db_column='ServicePlanName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    provisioningstatus = models.CharField(db_column='ProvisioningStatus', max_length=32, blank=True, null=True)  # Field name made lowercase.
    appliesto = models.CharField(db_column='AppliesTo', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblO365ServicePlan'


class Tblo365Sku(models.Model):
    skuid = models.AutoField(db_column='SkuId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblO365Sku'


class Tblo365User(models.Model):
    userid = models.AutoField(db_column='UserId', primary_key=True)  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectId', max_length=36)  # Field name made lowercase.
    organizationid = models.ForeignKey(Tblo365Organization, models.DO_NOTHING, db_column='OrganizationId')  # Field name made lowercase.
    userprincipalname = models.CharField(db_column='UserPrincipalName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(db_column='Mail', max_length=256, blank=True, null=True)  # Field name made lowercase.
    accountenabled = models.BooleanField(db_column='AccountEnabled')  # Field name made lowercase.
    agegroup = models.CharField(db_column='AgeGroup', max_length=50, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=500, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=500, blank=True, null=True)  # Field name made lowercase.
    consentprovidedforminor = models.CharField(db_column='ConsentProvidedForMinor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    creationtype = models.CharField(db_column='CreationType', max_length=150, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=500, blank=True, null=True)  # Field name made lowercase.
    dirsyncenabled = models.BooleanField(db_column='DirSyncEnabled', blank=True, null=True)  # Field name made lowercase.
    facsimiletelephonenumber = models.CharField(db_column='FacsimileTelephoneNumber', max_length=256, blank=True, null=True)  # Field name made lowercase.
    givenname = models.CharField(db_column='GivenName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    iscompromised = models.BooleanField(db_column='IsCompromised', blank=True, null=True)  # Field name made lowercase.
    immutableid = models.CharField(db_column='ImmutableId', max_length=256, blank=True, null=True)  # Field name made lowercase.
    isglobaladministrator = models.BooleanField(db_column='IsGlobalAdministrator', blank=True, null=True)  # Field name made lowercase.
    islicensed = models.BooleanField(db_column='IsLicensed', blank=True, null=True)  # Field name made lowercase.
    jobtitle = models.CharField(db_column='JobTitle', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lastdirsynctime = models.DateTimeField(db_column='LastDirSyncTime', blank=True, null=True)  # Field name made lowercase.
    legalagegroupclassification = models.CharField(db_column='LegalAgeGroupClassification', max_length=256, blank=True, null=True)  # Field name made lowercase.
    mailnickname = models.CharField(db_column='MailNickName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    onpremisessecurityidentifier = models.CharField(db_column='OnPremisesSecurityIdentifier', max_length=256, blank=True, null=True)  # Field name made lowercase.
    othermails = models.CharField(db_column='OtherMails', max_length=500, blank=True, null=True)  # Field name made lowercase.
    passwordpolicies = models.CharField(db_column='PasswordPolicies', max_length=256, blank=True, null=True)  # Field name made lowercase.
    passwordprofile = models.CharField(db_column='PasswordProfile', max_length=256, blank=True, null=True)  # Field name made lowercase.
    physicaldeliveryofficename = models.CharField(db_column='PhysicalDeliveryOfficeName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=16, blank=True, null=True)  # Field name made lowercase.
    preferredlanguage = models.CharField(db_column='PreferredLanguage', max_length=150, blank=True, null=True)  # Field name made lowercase.
    refreshtokensvalidfromdatetime = models.DateTimeField(db_column='RefreshTokensValidFromDateTime', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=300, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=500, blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=256, blank=True, null=True)  # Field name made lowercase.
    telephonenumber = models.CharField(db_column='TelephoneNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usagelocation = models.CharField(db_column='UsageLocation', max_length=256, blank=True, null=True)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=150, blank=True, null=True)  # Field name made lowercase.
    managerupn = models.CharField(db_column='ManagerUpn', max_length=256, blank=True, null=True)  # Field name made lowercase.
    distinguishedname = models.CharField(db_column='DistinguishedName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    resetpasswordonnextlogon = models.BooleanField(db_column='ResetPasswordOnNextLogon', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblO365User'


class Tbloiddata(models.Model):
    oiddataid = models.AutoField(db_column='OIDDataID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    targetid = models.IntegerField(db_column='TargetID')  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=150, blank=True, null=True)  # Field name made lowercase.
    key = models.CharField(db_column='Key', max_length=300)  # Field name made lowercase.
    data = models.TextField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOIDData'


class Tbloidkey(models.Model):
    oidkeyid = models.AutoField(db_column='OIDKeyID', primary_key=True)  # Field name made lowercase.
    targetid = models.ForeignKey('Tbloidtarget', models.DO_NOTHING, db_column='TargetID')  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=150, blank=True, null=True)  # Field name made lowercase.
    key = models.CharField(db_column='Key', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOIDKey'
        unique_together = (('targetid', 'key'),)


class Tbloidtarget(models.Model):
    targetid = models.AutoField(db_column='TargetID', primary_key=True)  # Field name made lowercase.
    targettypeid = models.ForeignKey('Tbloidtargettype', models.DO_NOTHING, db_column='TargetTypeID')  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=150, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=150, blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled', blank=True, null=True)  # Field name made lowercase.
    deleteonrescan = models.BooleanField(db_column='DeleteOnRescan', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250, blank=True, null=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID', blank=True, null=True)  # Field name made lowercase.
    assettype = models.ForeignKey('Tsysassettypes', models.DO_NOTHING, db_column='AssetType', blank=True, null=True)  # Field name made lowercase.
    assetgroupid = models.ForeignKey(Tblassetgroups, models.DO_NOTHING, db_column='AssetGroupID', blank=True, null=True)  # Field name made lowercase.
    iprangeid = models.ForeignKey('Tsysipscanranges', models.DO_NOTHING, db_column='IprangeID', blank=True, null=True)  # Field name made lowercase.
    reportquery = models.ForeignKey('Tsysreports', models.DO_NOTHING, db_column='Reportquery', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOIDTarget'


class Tbloidtargettype(models.Model):
    targettypeid = models.AutoField(db_column='TargetTypeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=50)  # Field name made lowercase.
    icon = models.CharField(db_column='Icon', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOIDTargetType'


class Tblosrecoveryconfiguration(models.Model):
    win32_osrecoveryconfigurationid = models.AutoField(db_column='Win32_OSRecoveryConfigurationid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    autoreboot = models.BooleanField(db_column='AutoReboot', blank=True, null=True)  # Field name made lowercase.
    debugfilepath = models.CharField(db_column='DebugFilePath', max_length=450, blank=True, null=True)  # Field name made lowercase.
    debuginfotype = models.DecimalField(db_column='DebugInfoType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    kerneldumponly = models.BooleanField(db_column='KernelDumpOnly', blank=True, null=True)  # Field name made lowercase.
    minidumpdirectory = models.CharField(db_column='MiniDumpDirectory', max_length=450, blank=True, null=True)  # Field name made lowercase.
    overwriteexistingdebugfile = models.BooleanField(db_column='OverwriteExistingDebugFile', blank=True, null=True)  # Field name made lowercase.
    sendadminalert = models.BooleanField(db_column='SendAdminAlert', blank=True, null=True)  # Field name made lowercase.
    writedebuginfo = models.BooleanField(db_column='WriteDebugInfo', blank=True, null=True)  # Field name made lowercase.
    writetosystemlog = models.BooleanField(db_column='WriteToSystemLog', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOSRecoveryConfiguration'


class Tblosrecoveryconfigurationhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    autoreboot = models.BooleanField(db_column='AutoReboot', blank=True, null=True)  # Field name made lowercase.
    debugfilepath = models.CharField(db_column='DebugFilePath', max_length=450, blank=True, null=True)  # Field name made lowercase.
    debuginfotype = models.DecimalField(db_column='DebugInfoType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    kerneldumponly = models.BooleanField(db_column='KernelDumpOnly', blank=True, null=True)  # Field name made lowercase.
    minidumpdirectory = models.CharField(db_column='MiniDumpDirectory', max_length=450, blank=True, null=True)  # Field name made lowercase.
    overwriteexistingdebugfile = models.BooleanField(db_column='OverwriteExistingDebugFile', blank=True, null=True)  # Field name made lowercase.
    sendadminalert = models.BooleanField(db_column='SendAdminAlert', blank=True, null=True)  # Field name made lowercase.
    writedebuginfo = models.BooleanField(db_column='WriteDebugInfo', blank=True, null=True)  # Field name made lowercase.
    writetosystemlog = models.BooleanField(db_column='WriteToSystemLog', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOSRecoveryConfigurationHist'


class Tblonboarddevice(models.Model):
    win32_onboarddeviceid = models.AutoField(db_column='Win32_OnBoardDeviceid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=450, blank=True, null=True)  # Field name made lowercase.
    devicetype = models.DecimalField(db_column='DeviceType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled', blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='Tag', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOnBoardDevice'


class Tblonboarddevicehist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=450, blank=True, null=True)  # Field name made lowercase.
    devicetype = models.DecimalField(db_column='DeviceType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled', blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='Tag', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOnBoardDeviceHist'


class Tbloperatingsystem(models.Model):
    osid = models.AutoField(db_column='OSID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    buildtype = models.CharField(db_column='BuildType', max_length=450, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    codeset = models.CharField(db_column='Codeset', max_length=50, blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='Countrycode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    currenttimezone = models.DecimalField(db_column='Currenttimezone', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dataexecutionprevention_32bitapplications = models.BooleanField(db_column='DataExecutionPrevention_32BitApplications', blank=True, null=True)  # Field name made lowercase.
    dataexecutionprevention_available = models.BooleanField(db_column='DataExecutionPrevention_Available', blank=True, null=True)  # Field name made lowercase.
    dataexecutionprevention_drivers = models.BooleanField(db_column='DataExecutionPrevention_Drivers', blank=True, null=True)  # Field name made lowercase.
    dataexecutionprevention_supportpolicy = models.DecimalField(db_column='DataExecutionPrevention_Supportpolicy', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    debug = models.BooleanField(db_column='Debug', blank=True, null=True)  # Field name made lowercase.
    encryptionlevel = models.DecimalField(db_column='EncryptionLevel', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    foregroundapplicationboost = models.IntegerField(db_column='ForegroundApplicationBoost', blank=True, null=True)  # Field name made lowercase.
    installdate = models.DateTimeField(db_column='InstallDate', blank=True, null=True)  # Field name made lowercase.
    largesystemcache = models.BooleanField(db_column='LargeSystemCache', blank=True, null=True)  # Field name made lowercase.
    maxprocessmemorysize = models.DecimalField(db_column='MaxProcessMemorySize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    numberoflicensedusers = models.DecimalField(db_column='NumberOfLicensedUsers', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    organization = models.CharField(db_column='Organization', max_length=450, blank=True, null=True)  # Field name made lowercase.
    oslanguage = models.DecimalField(db_column='OSLanguage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    osproductsuite = models.DecimalField(db_column='OSProductSuite', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ostype = models.DecimalField(db_column='OSType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    othertypedescription = models.CharField(db_column='OtherTypeDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    plusproductid = models.CharField(db_column='PlusProductID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    plusversionnumber = models.CharField(db_column='PlusVersionNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    producttype = models.DecimalField(db_column='ProductType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    registereduser = models.CharField(db_column='RegisteredUser', max_length=450, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    servicepackmajorversion = models.DecimalField(db_column='ServicePackMajorVersion', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    servicepackminorversion = models.DecimalField(db_column='ServicePackMinorVersion', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    sizestoredinpagingfiles = models.DecimalField(db_column='SizeStoredInPagingFiles', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    suitemask = models.DecimalField(db_column='Suitemask', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    systemdevice = models.CharField(db_column='SystemDevice', max_length=450, blank=True, null=True)  # Field name made lowercase.
    systemdrive = models.CharField(db_column='SystemDrive', max_length=50, blank=True, null=True)  # Field name made lowercase.
    totalvirtualmemorysize = models.DecimalField(db_column='TotalVirtualMemorysize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    totalvisiblememorysize = models.DecimalField(db_column='TotalVisibleMemorySize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=50, blank=True, null=True)  # Field name made lowercase.
    windowsdirectory = models.CharField(db_column='WindowsDirectory', max_length=300, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOperatingsystem'


class Tbloperatingsystemhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    buildtype = models.CharField(db_column='BuildType', max_length=450, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    codeset = models.CharField(db_column='Codeset', max_length=50, blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='Countrycode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    currenttimezone = models.DecimalField(db_column='Currenttimezone', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dataexecutionprevention_32bitapplications = models.BooleanField(db_column='DataExecutionPrevention_32BitApplications', blank=True, null=True)  # Field name made lowercase.
    dataexecutionprevention_available = models.BooleanField(db_column='DataExecutionPrevention_Available', blank=True, null=True)  # Field name made lowercase.
    dataexecutionprevention_drivers = models.BooleanField(db_column='DataExecutionPrevention_Drivers', blank=True, null=True)  # Field name made lowercase.
    dataexecutionprevention_supportpolicy = models.DecimalField(db_column='DataExecutionPrevention_Supportpolicy', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    debug = models.BooleanField(db_column='Debug', blank=True, null=True)  # Field name made lowercase.
    encryptionlevel = models.DecimalField(db_column='EncryptionLevel', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    foregroundapplicationboost = models.IntegerField(db_column='ForegroundApplicationBoost', blank=True, null=True)  # Field name made lowercase.
    installdate = models.DateTimeField(db_column='InstallDate', blank=True, null=True)  # Field name made lowercase.
    largesystemcache = models.BooleanField(db_column='LargeSystemCache', blank=True, null=True)  # Field name made lowercase.
    maxprocessmemorysize = models.DecimalField(db_column='MaxProcessMemorySize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    numberoflicensedusers = models.DecimalField(db_column='NumberOfLicensedUsers', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    organization = models.CharField(db_column='Organization', max_length=450, blank=True, null=True)  # Field name made lowercase.
    oslanguage = models.DecimalField(db_column='OSLanguage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    osproductsuite = models.DecimalField(db_column='OSProductSuite', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ostype = models.DecimalField(db_column='OSType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    othertypedescription = models.CharField(db_column='OtherTypeDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    plusproductid = models.CharField(db_column='PlusProductID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    plusversionnumber = models.CharField(db_column='PlusVersionNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    producttype = models.DecimalField(db_column='ProductType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    registereduser = models.CharField(db_column='RegisteredUser', max_length=450, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    servicepackmajorversion = models.DecimalField(db_column='ServicePackMajorVersion', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    servicepackminorversion = models.DecimalField(db_column='ServicePackMinorVersion', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    sizestoredinpagingfiles = models.DecimalField(db_column='SizeStoredInPagingFiles', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    suitemask = models.DecimalField(db_column='Suitemask', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    systemdevice = models.CharField(db_column='SystemDevice', max_length=450, blank=True, null=True)  # Field name made lowercase.
    systemdrive = models.CharField(db_column='SystemDrive', max_length=50, blank=True, null=True)  # Field name made lowercase.
    totalvirtualmemorysize = models.DecimalField(db_column='TotalVirtualMemorysize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    totalvisiblememorysize = models.DecimalField(db_column='TotalVisibleMemorySize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=50, blank=True, null=True)  # Field name made lowercase.
    windowsdirectory = models.CharField(db_column='WindowsDirectory', max_length=300, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOperatingsystemHist'


class Tbloslicenses(models.Model):
    oslicenseidid = models.AutoField(db_column='OSLicenseidID', primary_key=True)  # Field name made lowercase.
    os = models.CharField(db_column='OS', unique=True, max_length=450)  # Field name made lowercase.
    priceperlicense = models.DecimalField(db_column='Priceperlicense', max_digits=19, decimal_places=4)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    licensecontact = models.CharField(db_column='LicenseContact', max_length=500, blank=True, null=True)  # Field name made lowercase.
    licenseowner = models.CharField(db_column='LicenseOwner', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOsLicenses'


class Tblossublicensedocs(models.Model):
    oslicensesubdocid = models.AutoField(db_column='OSLicensesubdocid', primary_key=True)  # Field name made lowercase.
    oslicenseidid = models.ForeignKey(Tbloslicenses, models.DO_NOTHING, db_column='OSLicenseidID')  # Field name made lowercase.
    doclink = models.CharField(db_column='Doclink', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    docname = models.CharField(db_column='Docname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOssubLicenseDocs'


class Tblossublicenses(models.Model):
    oslicensesubid = models.AutoField(db_column='OSLicensesubid', primary_key=True)  # Field name made lowercase.
    oslicenseidid = models.ForeignKey(Tbloslicenses, models.DO_NOTHING, db_column='OSLicenseidID')  # Field name made lowercase.
    os = models.CharField(db_column='OS', max_length=450)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOssubLicenses'


class Tblossublicensesorders(models.Model):
    oslicensesuborderid = models.AutoField(db_column='OSLicensesuborderid', primary_key=True)  # Field name made lowercase.
    oslicenseidid = models.ForeignKey(Tbloslicenses, models.DO_NOTHING, db_column='OSLicenseidID')  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='Orderdate', blank=True, null=True)  # Field name made lowercase.
    nrlicenses = models.IntegerField(db_column='Nrlicenses', blank=True, null=True)  # Field name made lowercase.
    priceperlicense = models.DecimalField(db_column='Priceperlicense', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ordernumber = models.CharField(db_column='Ordernumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    licensekey = models.TextField(db_column='Licensekey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOssubLicensesOrders'


class Tblpcmciacontroller(models.Model):
    win32_pcmciacontrollerid = models.AutoField(db_column='Win32_PCMCIAControllerid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    configmanagererrorcode = models.DecimalField(db_column='ConfigManagerErrorCode', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    configmanageruserconfig = models.BooleanField(db_column='ConfigManagerUserConfig', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    protocolsupported = models.DecimalField(db_column='ProtocolSupported', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPCMCIAController'


class Tblpcmciacontrollerhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    configmanagererrorcode = models.DecimalField(db_column='ConfigManagerErrorCode', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    configmanageruserconfig = models.BooleanField(db_column='ConfigManagerUserConfig', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    protocolsupported = models.DecimalField(db_column='ProtocolSupported', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPCMCIAControllerHist'


class Tblpotsmodem(models.Model):
    win32_potsmodemid = models.AutoField(db_column='Win32_POTSModemid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    attachedto = models.CharField(db_column='AttachedTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    countryselected = models.CharField(db_column='CountrySelected', max_length=500, blank=True, null=True)  # Field name made lowercase.
    devicetype = models.CharField(db_column='DeviceType', max_length=500, blank=True, null=True)  # Field name made lowercase.
    maxbaudratetophone = models.DecimalField(db_column='MaxBaudRateToPhone', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    maxbaudratetoserialport = models.DecimalField(db_column='MaxBaudRateToSerialPort', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    providername = models.CharField(db_column='ProviderName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPOTSModem'


class Tblpotsmodemhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    attachedto = models.CharField(db_column='AttachedTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    countryselected = models.CharField(db_column='CountrySelected', max_length=500, blank=True, null=True)  # Field name made lowercase.
    devicetype = models.CharField(db_column='DeviceType', max_length=500, blank=True, null=True)  # Field name made lowercase.
    maxbaudratetophone = models.DecimalField(db_column='MaxBaudRateToPhone', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    maxbaudratetoserialport = models.DecimalField(db_column='MaxBaudRateToSerialPort', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    providername = models.CharField(db_column='ProviderName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPOTSModemHist'


class Tblpagefile(models.Model):
    win32_pagefileid = models.AutoField(db_column='Win32_PageFileid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    archive = models.BooleanField(db_column='Archive', blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    filesize = models.DecimalField(db_column='FileSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    initialsize = models.DecimalField(db_column='InitialSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    installdate = models.DateTimeField(db_column='InstallDate', blank=True, null=True)  # Field name made lowercase.
    maximumsize = models.DecimalField(db_column='MaximumSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(db_column='Path', max_length=450, blank=True, null=True)  # Field name made lowercase.
    readable = models.BooleanField(db_column='Readable', blank=True, null=True)  # Field name made lowercase.
    system = models.BooleanField(db_column='System', blank=True, null=True)  # Field name made lowercase.
    writeable = models.BooleanField(db_column='Writeable', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPageFile'


class Tblpagefilehist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    archive = models.BooleanField(db_column='Archive', blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    filesize = models.DecimalField(db_column='FileSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    initialsize = models.DecimalField(db_column='InitialSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    installdate = models.DateTimeField(db_column='InstallDate', blank=True, null=True)  # Field name made lowercase.
    maximumsize = models.DecimalField(db_column='MaximumSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(db_column='Path', max_length=450, blank=True, null=True)  # Field name made lowercase.
    readable = models.BooleanField(db_column='Readable', blank=True, null=True)  # Field name made lowercase.
    system = models.BooleanField(db_column='System', blank=True, null=True)  # Field name made lowercase.
    writeable = models.BooleanField(db_column='Writeable', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPageFileHist'


class Tblparallelport(models.Model):
    win32_parallelportid = models.AutoField(db_column='Win32_ParallelPortid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    availability = models.DecimalField(db_column='Availability', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    configmanagererrorcode = models.DecimalField(db_column='ConfigManagerErrorCode', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    configmanageruserconfig = models.BooleanField(db_column='ConfigManagerUserConfig', blank=True, null=True)  # Field name made lowercase.
    osautodiscovered = models.BooleanField(db_column='OSAutoDiscovered', blank=True, null=True)  # Field name made lowercase.
    powermanagementsupported = models.BooleanField(db_column='PowerManagementSupported', blank=True, null=True)  # Field name made lowercase.
    protocolsupported = models.DecimalField(db_column='ProtocolSupported', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblParallelPort'


class Tblparallelporthist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    availability = models.DecimalField(db_column='Availability', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    configmanagererrorcode = models.DecimalField(db_column='ConfigManagerErrorCode', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    configmanageruserconfig = models.BooleanField(db_column='ConfigManagerUserConfig', blank=True, null=True)  # Field name made lowercase.
    osautodiscovered = models.BooleanField(db_column='OSAutoDiscovered', blank=True, null=True)  # Field name made lowercase.
    powermanagementsupported = models.BooleanField(db_column='PowerManagementSupported', blank=True, null=True)  # Field name made lowercase.
    protocolsupported = models.DecimalField(db_column='ProtocolSupported', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblParallelPortHist'


class Tblperformancecountersscan(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    scandatetime = models.DateTimeField(db_column='ScanDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPerformanceCountersScan'


class Tblperformancecountersscanmetric(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    performancecountersscanid = models.ForeignKey(Tblperformancecountersscan, models.DO_NOTHING, db_column='PerformanceCountersScanId')  # Field name made lowercase.
    metric = models.BigIntegerField(db_column='Metric')  # Field name made lowercase.
    value = models.DecimalField(db_column='Value', max_digits=18, decimal_places=0)  # Field name made lowercase.
    performancecountersscanmetricidentifierid = models.ForeignKey('Tblperformancecountersscanmetricidentifier', models.DO_NOTHING, db_column='PerformanceCountersScanMetricIdentifierId', blank=True, null=True)  # Field name made lowercase.
    scandatetime = models.DateTimeField(db_column='ScanDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPerformanceCountersScanMetric'


class Tblperformancecountersscanmetricidentifier(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPerformanceCountersScanMetricIdentifier'


class Tblphysicalmemory(models.Model):
    win32_physicalmemoryid = models.AutoField(db_column='Win32_PhysicalMemoryid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    capacity = models.DecimalField(db_column='Capacity', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    datawidth = models.DecimalField(db_column='DataWidth', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    devicelocator = models.CharField(db_column='DeviceLocator', max_length=400, blank=True, null=True)  # Field name made lowercase.
    formfactor = models.DecimalField(db_column='FormFactor', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    interleavedatadepth = models.DecimalField(db_column='InterleaveDataDepth', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    interleaveposition = models.DecimalField(db_column='InterleavePosition', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    memorytype = models.IntegerField(db_column='MemoryType', blank=True, null=True)  # Field name made lowercase.
    positioninrow = models.DecimalField(db_column='PositionInRow', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    speed = models.DecimalField(db_column='Speed', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    totalwidth = models.DecimalField(db_column='TotalWidth', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    typedetail = models.DecimalField(db_column='TypeDetail', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=200, blank=True, null=True)  # Field name made lowercase.
    partnumber = models.CharField(db_column='PartNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sku = models.CharField(db_column='SKU', max_length=200, blank=True, null=True)  # Field name made lowercase.
    configuredclockspeed = models.IntegerField(db_column='ConfiguredClockSpeed', blank=True, null=True)  # Field name made lowercase.
    configuredvoltage = models.IntegerField(db_column='ConfiguredVoltage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPhysicalMemory'


class Tblphysicalmemoryarray(models.Model):
    win32_physicalmemoryarrayid = models.AutoField(db_column='Win32_PhysicalMemoryArrayid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    location = models.DecimalField(db_column='Location', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    maxcapacity = models.DecimalField(db_column='MaxCapacity', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    memorydevices = models.DecimalField(db_column='MemoryDevices', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    memoryerrorcorrection = models.DecimalField(db_column='MemoryErrorCorrection', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='Tag', max_length=450, blank=True, null=True)  # Field name made lowercase.
    use = models.DecimalField(db_column='Use', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPhysicalMemoryArray'


class Tblphysicalmemoryarrayhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    location = models.DecimalField(db_column='Location', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    maxcapacity = models.DecimalField(db_column='MaxCapacity', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    memorydevices = models.DecimalField(db_column='MemoryDevices', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    memoryerrorcorrection = models.DecimalField(db_column='MemoryErrorCorrection', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='Tag', max_length=450, blank=True, null=True)  # Field name made lowercase.
    use = models.DecimalField(db_column='Use', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPhysicalMemoryArrayHist'


class Tblphysicalmemoryhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    capacity = models.DecimalField(db_column='Capacity', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    datawidth = models.DecimalField(db_column='DataWidth', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    devicelocator = models.CharField(db_column='DeviceLocator', max_length=400, blank=True, null=True)  # Field name made lowercase.
    formfactor = models.DecimalField(db_column='FormFactor', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    interleavedatadepth = models.DecimalField(db_column='InterleaveDataDepth', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    interleaveposition = models.DecimalField(db_column='InterleavePosition', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    memorytype = models.DecimalField(db_column='MemoryType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    positioninrow = models.DecimalField(db_column='PositionInRow', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    speed = models.DecimalField(db_column='Speed', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    totalwidth = models.DecimalField(db_column='TotalWidth', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    typedetail = models.DecimalField(db_column='TypeDetail', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=200, blank=True, null=True)  # Field name made lowercase.
    partnumber = models.CharField(db_column='PartNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sku = models.CharField(db_column='SKU', max_length=200, blank=True, null=True)  # Field name made lowercase.
    configuredclockspeed = models.IntegerField(db_column='ConfiguredClockSpeed', blank=True, null=True)  # Field name made lowercase.
    configuredvoltage = models.IntegerField(db_column='ConfiguredVoltage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPhysicalMemoryHist'


class Tblpnpsigneddrivers(models.Model):
    pnpsigneddriverid = models.BigAutoField(db_column='PnPSignedDriverID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=200)  # Field name made lowercase.
    pnpsigneddriveruniid = models.ForeignKey('Tblpnpsigneddriversuni', models.DO_NOTHING, db_column='PnPSignedDriverUniID')  # Field name made lowercase.
    compatid = models.CharField(db_column='CompatID', max_length=150, blank=True, null=True)  # Field name made lowercase.
    devloader = models.CharField(db_column='DevLoader', max_length=20, blank=True, null=True)  # Field name made lowercase.
    drivername = models.CharField(db_column='DriverName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    friendlyname = models.CharField(db_column='FriendlyName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    driverdate = models.DateTimeField(db_column='DriverDate', blank=True, null=True)  # Field name made lowercase.
    driverversion = models.CharField(db_column='DriverVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hardwareid = models.CharField(db_column='HardwareID', max_length=150, blank=True, null=True)  # Field name made lowercase.
    infname = models.CharField(db_column='InfName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    issigned = models.BooleanField(db_column='IsSigned')  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pdo = models.CharField(db_column='PDO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPnPSignedDrivers'
        unique_together = (('assetid', 'pnpsigneddriveruniid', 'deviceid'),)


class Tblpnpsigneddriversuni(models.Model):
    pnpsigneddriveruniid = models.AutoField(db_column='PnPSignedDriverUniID', primary_key=True)  # Field name made lowercase.
    devicename = models.CharField(db_column='DeviceName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=400, blank=True, null=True)  # Field name made lowercase.
    deviceclass = models.CharField(db_column='DeviceClass', max_length=60, blank=True, null=True)  # Field name made lowercase.
    driverprovidername = models.CharField(db_column='DriverProviderName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    signer = models.CharField(db_column='Signer', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPnPSignedDriversUni'
        unique_together = (('devicename', 'deviceclass', 'driverprovidername', 'signer'),)


class Tblpointingdevice(models.Model):
    win32_pointingdeviceid = models.AutoField(db_column='Win32_PointingDeviceid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    deviceinterface = models.DecimalField(db_column='DeviceInterface', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    doublespeedthreshold = models.DecimalField(db_column='DoubleSpeedThreshold', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    handedness = models.DecimalField(db_column='Handedness', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    numberofbuttons = models.DecimalField(db_column='NumberOfButtons', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pointingtype = models.DecimalField(db_column='PointingType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    quadspeedthreshold = models.DecimalField(db_column='QuadSpeedThreshold', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPointingDevice'


class Tblpointingdevicehist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    deviceinterface = models.DecimalField(db_column='DeviceInterface', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    doublespeedthreshold = models.DecimalField(db_column='DoubleSpeedThreshold', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    handedness = models.DecimalField(db_column='Handedness', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    numberofbuttons = models.DecimalField(db_column='NumberOfButtons', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pointingtype = models.DecimalField(db_column='PointingType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    quadspeedthreshold = models.DecimalField(db_column='QuadSpeedThreshold', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPointingDeviceHist'


class Tblportconnector(models.Model):
    win32_portconnectorid = models.AutoField(db_column='Win32_PortConnectorid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    connectortype = models.CharField(db_column='ConnectorType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    externalreferencedesignator = models.CharField(db_column='ExternalReferenceDesignator', max_length=450, blank=True, null=True)  # Field name made lowercase.
    internalreferencedesignator = models.CharField(db_column='InternalReferenceDesignator', max_length=450, blank=True, null=True)  # Field name made lowercase.
    porttype = models.DecimalField(db_column='PortType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPortConnector'


class Tblportconnectorhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    connectortype = models.CharField(db_column='ConnectorType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    externalreferencedesignator = models.CharField(db_column='ExternalReferenceDesignator', max_length=450, blank=True, null=True)  # Field name made lowercase.
    internalreferencedesignator = models.CharField(db_column='InternalReferenceDesignator', max_length=450, blank=True, null=True)  # Field name made lowercase.
    porttype = models.DecimalField(db_column='PortType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPortConnectorHist'


class Tblportablebattery(models.Model):
    win32_portablebatteryid = models.AutoField(db_column='Win32_PortableBatteryid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    capacitymultiplier = models.DecimalField(db_column='CapacityMultiplier', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    chemistry = models.DecimalField(db_column='Chemistry', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    designcapacity = models.DecimalField(db_column='DesignCapacity', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    designvoltage = models.DecimalField(db_column='DesignVoltage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    manufacturedate = models.DateTimeField(db_column='ManufactureDate', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    maxbatteryerror = models.DecimalField(db_column='MaxBatteryError', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=450, blank=True, null=True)  # Field name made lowercase.
    smartbatteryversion = models.CharField(db_column='SmartBatteryVersion', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPortableBattery'


class Tblportablebatteryhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    capacitymultiplier = models.DecimalField(db_column='CapacityMultiplier', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    chemistry = models.DecimalField(db_column='Chemistry', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    designcapacity = models.DecimalField(db_column='DesignCapacity', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    designvoltage = models.DecimalField(db_column='DesignVoltage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    manufacturedate = models.DateTimeField(db_column='ManufactureDate', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    maxbatteryerror = models.DecimalField(db_column='MaxBatteryError', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=450, blank=True, null=True)  # Field name made lowercase.
    smartbatteryversion = models.CharField(db_column='SmartBatteryVersion', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPortableBatteryHist'


class Tblpowershellcategory(models.Model):
    categoryid = models.AutoField(db_column='CategoryId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    icon = models.CharField(db_column='Icon', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPowershellCategory'


class Tblpowershellcolumndefinition(models.Model):
    powershellcolumndefinitionid = models.AutoField(db_column='PowershellColumnDefinitionId', primary_key=True)  # Field name made lowercase.
    powershelldefinitionid = models.ForeignKey('Tblpowershelldefinition', models.DO_NOTHING, db_column='PowershellDefinitionId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPowershellColumnDefinition'


class Tblpowershelldefinition(models.Model):
    powershelldefinitionid = models.AutoField(db_column='PowershellDefinitionId', primary_key=True)  # Field name made lowercase.
    assettypeid = models.ForeignKey('Tsysassettypes', models.DO_NOTHING, db_column='AssetTypeId')  # Field name made lowercase.
    categoryid = models.ForeignKey(Tblpowershellcategory, models.DO_NOTHING, db_column='CategoryId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=4000)  # Field name made lowercase.
    systemdefault = models.BooleanField(db_column='SystemDefault')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    icon = models.CharField(db_column='Icon', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPowershellDefinition'


class Tblpowershellresult(models.Model):
    powershellresultid = models.AutoField(db_column='PowershellResultId', primary_key=True)  # Field name made lowercase.
    powershellcolumndefinitionid = models.ForeignKey(Tblpowershellcolumndefinition, models.DO_NOTHING, db_column='PowershellColumnDefinitionId')  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    rowindex = models.IntegerField(db_column='RowIndex')  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=4000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPowershellResult'


class Tblpowershellresultlastscan(models.Model):
    lastscanid = models.AutoField(db_column='LastscanId', primary_key=True)  # Field name made lowercase.
    powershelldefinitionid = models.ForeignKey(Tblpowershelldefinition, models.DO_NOTHING, db_column='PowershellDefinitionId')  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    lasttime = models.DateTimeField(db_column='Lasttime')  # Field name made lowercase.
    scantime = models.FloatField(db_column='Scantime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPowershellResultLastscan'


class Tblprinterdriverdevice(models.Model):
    printerdriverdeviceid = models.BigAutoField(db_column='PrinterDriverDeviceID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=200)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPrinterDriverDevice'


class Tblprinterdrivers(models.Model):
    printerdriverid = models.BigAutoField(db_column='PrinterDriverID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    printerdriveruniid = models.ForeignKey('Tblprinterdriversuni', models.DO_NOTHING, db_column='PrinterDriverUniID')  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    driverversion = models.CharField(db_column='DriverVersion', max_length=20, blank=True, null=True)  # Field name made lowercase.
    driverdate = models.DateTimeField(db_column='DriverDate', blank=True, null=True)  # Field name made lowercase.
    configfile = models.CharField(db_column='ConfigFile', max_length=250, blank=True, null=True)  # Field name made lowercase.
    datafile = models.CharField(db_column='DataFile', max_length=250, blank=True, null=True)  # Field name made lowercase.
    driverpath = models.CharField(db_column='DriverPath', max_length=250, blank=True, null=True)  # Field name made lowercase.
    filepath = models.CharField(db_column='FilePath', max_length=250, blank=True, null=True)  # Field name made lowercase.
    helpfile = models.CharField(db_column='HelpFile', max_length=250, blank=True, null=True)  # Field name made lowercase.
    infpath = models.CharField(db_column='InfPath', max_length=250, blank=True, null=True)  # Field name made lowercase.
    hardwareid = models.CharField(db_column='HardwareID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    printprocessor = models.CharField(db_column='PrintProcessor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    printerenvironment = models.CharField(db_column='PrinterEnvironment', max_length=50, blank=True, null=True)  # Field name made lowercase.
    defaultdatatype = models.CharField(db_column='DefaultDataType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    monitorname = models.CharField(db_column='MonitorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oemurl = models.CharField(db_column='OemUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPrinterDrivers'
        unique_together = (('assetid', 'printerdriveruniid', 'version'),)


class Tblprinterdriversuni(models.Model):
    printerdriveruniid = models.AutoField(db_column='PrinterDriverUniID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=200, blank=True, null=True)  # Field name made lowercase.
    provider = models.CharField(db_column='Provider', max_length=200, blank=True, null=True)  # Field name made lowercase.
    supportedplatform = models.CharField(db_column='SupportedPlatform', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPrinterDriversUni'
        unique_together = (('name', 'supportedplatform'),)


class Tblprinters(models.Model):
    printerid = models.AutoField(db_column='printerID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    capabilitydescriptions = models.CharField(db_column='Capabilitydescriptions', max_length=500, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=500, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    enablebidi = models.BooleanField(db_column='EnableBIDI', blank=True, null=True)  # Field name made lowercase.
    horizontalresolution = models.DecimalField(db_column='Horizontalresolution', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    local = models.BooleanField(db_column='Local', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=450, blank=True, null=True)  # Field name made lowercase.
    network = models.BooleanField(db_column='Network', blank=True, null=True)  # Field name made lowercase.
    portname = models.CharField(db_column='Portname', max_length=250, blank=True, null=True)  # Field name made lowercase.
    printjobdatatype = models.CharField(db_column='Printjobdatatype', max_length=50, blank=True, null=True)  # Field name made lowercase.
    printprocessor = models.CharField(db_column='Printprocessor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sharename = models.CharField(db_column='Sharename', max_length=500, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    verticalresolution = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPrinters'


class Tblprintershist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    capabilitydescriptions = models.CharField(db_column='Capabilitydescriptions', max_length=500, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=500, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    enablebidi = models.BooleanField(db_column='EnableBIDI', blank=True, null=True)  # Field name made lowercase.
    horizontalresolution = models.DecimalField(db_column='Horizontalresolution', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    local = models.BooleanField(db_column='Local', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=450, blank=True, null=True)  # Field name made lowercase.
    network = models.BooleanField(db_column='Network', blank=True, null=True)  # Field name made lowercase.
    portname = models.CharField(db_column='Portname', max_length=250, blank=True, null=True)  # Field name made lowercase.
    printjobdatatype = models.CharField(db_column='Printjobdatatype', max_length=50, blank=True, null=True)  # Field name made lowercase.
    printprocessor = models.CharField(db_column='Printprocessor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sharename = models.CharField(db_column='Sharename', max_length=500, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    verticalresolution = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPrintersHist'


class Tblprocesses(models.Model):
    processid = models.AutoField(db_column='ProcessID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    commandline = models.CharField(db_column='Commandline', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    executablepath = models.CharField(db_column='ExecutablePath', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    threadcount = models.DecimalField(db_column='Threadcount', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    priority = models.DecimalField(db_column='Priority', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblProcesses'


class Tblprocessor(models.Model):
    win32_processorid = models.AutoField(db_column='WIN32_PROCESSORid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    addresswidth = models.DecimalField(db_column='AddressWidth', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    architecture = models.DecimalField(db_column='Architecture', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    availability = models.DecimalField(db_column='Availability', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    cpustatus = models.DecimalField(db_column='CpuStatus', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    datawidth = models.DecimalField(db_column='DataWidth', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=450, blank=True, null=True)  # Field name made lowercase.
    extclock = models.DecimalField(db_column='ExtClock', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    family = models.DecimalField(db_column='Family', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    l2cachesize = models.DecimalField(db_column='L2CacheSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    l2cachespeed = models.DecimalField(db_column='L2CacheSpeed', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    level = models.DecimalField(db_column='Level', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    maxclockspeed = models.DecimalField(db_column='MaxClockSpeed', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=450, blank=True, null=True)  # Field name made lowercase.
    numberofcores = models.DecimalField(db_column='NumberOfCores', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    numberoflogicalprocessors = models.DecimalField(db_column='NumberOfLogicalProcessors', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    processorid = models.CharField(db_column='ProcessorId', max_length=300, blank=True, null=True)  # Field name made lowercase.
    processortype = models.DecimalField(db_column='ProcessorType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    revision = models.DecimalField(db_column='Revision', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    socketdesignation = models.CharField(db_column='SocketDesignation', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stepping = models.CharField(db_column='Stepping', max_length=50, blank=True, null=True)  # Field name made lowercase.
    uniqueid = models.CharField(db_column='UniqueId', max_length=300, blank=True, null=True)  # Field name made lowercase.
    upgrademethod = models.DecimalField(db_column='UpgradeMethod', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=500, blank=True, null=True)  # Field name made lowercase.
    voltagecaps = models.DecimalField(db_column='VoltageCaps', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblProcessor'


class Tblprocessorhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    addresswidth = models.DecimalField(db_column='AddressWidth', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    architecture = models.DecimalField(db_column='Architecture', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    availability = models.DecimalField(db_column='Availability', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    cpustatus = models.DecimalField(db_column='CpuStatus', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    datawidth = models.DecimalField(db_column='DataWidth', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=450, blank=True, null=True)  # Field name made lowercase.
    extclock = models.DecimalField(db_column='ExtClock', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    family = models.DecimalField(db_column='Family', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    l2cachesize = models.DecimalField(db_column='L2CacheSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    l2cachespeed = models.DecimalField(db_column='L2CacheSpeed', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    level = models.DecimalField(db_column='Level', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    maxclockspeed = models.DecimalField(db_column='MaxClockSpeed', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=450, blank=True, null=True)  # Field name made lowercase.
    numberofcores = models.DecimalField(db_column='NumberOfCores', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    numberoflogicalprocessors = models.DecimalField(db_column='NumberOfLogicalProcessors', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    processorid = models.CharField(db_column='ProcessorId', max_length=300, blank=True, null=True)  # Field name made lowercase.
    processortype = models.DecimalField(db_column='ProcessorType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    revision = models.DecimalField(db_column='Revision', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    socketdesignation = models.CharField(db_column='SocketDesignation', max_length=450, blank=True, null=True)  # Field name made lowercase.
    stepping = models.CharField(db_column='Stepping', max_length=50, blank=True, null=True)  # Field name made lowercase.
    uniqueid = models.CharField(db_column='UniqueId', max_length=300, blank=True, null=True)  # Field name made lowercase.
    upgrademethod = models.DecimalField(db_column='UpgradeMethod', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=500, blank=True, null=True)  # Field name made lowercase.
    voltagecaps = models.DecimalField(db_column='VoltageCaps', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblProcessorHist'


class Tblproxy(models.Model):
    proxyid = models.AutoField(db_column='ProxyID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    proxyportnumber = models.CharField(db_column='Proxyportnumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    proxyserver = models.CharField(db_column='Proxyserver', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblProxy'


class Tblquickfixengineering(models.Model):
    win32_quickfixengineeringid = models.AutoField(db_column='Win32_QuickFixEngineeringid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    qfeid = models.ForeignKey('Tblquickfixengineeringuni', models.DO_NOTHING, db_column='QFEID')  # Field name made lowercase.
    installedbyid = models.ForeignKey('Tblquickfixengineeringinstalledby', models.DO_NOTHING, db_column='InstalledByID')  # Field name made lowercase.
    installedon = models.CharField(db_column='InstalledOn', max_length=300, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblQuickFixEngineering'


class Tblquickfixengineeringhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    qfeid = models.IntegerField(db_column='QFEID', blank=True, null=True)  # Field name made lowercase.
    installedbyid = models.IntegerField(db_column='InstalledByID', blank=True, null=True)  # Field name made lowercase.
    installedon = models.CharField(db_column='InstalledOn', max_length=300, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblQuickFixEngineeringHist'


class Tblquickfixengineeringinstalledby(models.Model):
    installedbyid = models.AutoField(db_column='InstalledByID', primary_key=True)  # Field name made lowercase.
    installedby = models.CharField(db_column='InstalledBy', max_length=350, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblQuickFixEngineeringInstalledBy'


class Tblquickfixengineeringuni(models.Model):
    qfeid = models.AutoField(db_column='QFEID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=450, blank=True, null=True)  # Field name made lowercase.
    fixcomments = models.CharField(db_column='FixComments', max_length=450, blank=True, null=True)  # Field name made lowercase.
    hotfixid = models.CharField(db_column='HotFixID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    servicepackineffect = models.CharField(db_column='ServicePackInEffect', max_length=300, blank=True, null=True)  # Field name made lowercase.
    hash = models.CharField(db_column='Hash', unique=True, max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblQuickFixEngineeringUni'


class Tblregistry(models.Model):
    registryid = models.AutoField(db_column='RegistryID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    regkey = models.CharField(db_column='Regkey', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    valuename = models.CharField(db_column='Valuename', max_length=200, blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblRegistry'


class Tblsnmpassetmac(models.Model):
    snmpmacid = models.BigAutoField(db_column='SNMPMacID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    ifindex = models.IntegerField(db_column='IfIndex')  # Field name made lowercase.
    assetmacaddress = models.CharField(db_column='AssetMacAddress', max_length=50)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    online = models.BooleanField(db_column='Online')  # Field name made lowercase.
    lastseen = models.DateTimeField(db_column='LastSeen')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSNMPAssetMac'


class Tblsnmpiftypes(models.Model):
    iftype = models.IntegerField(db_column='IfType', primary_key=True)  # Field name made lowercase.
    iftypename = models.CharField(db_column='IfTypename', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSNMPIfTypes'


class Tblsnmpinfo(models.Model):
    snmpinfoid = models.BigAutoField(db_column='SnmpInfoID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    ifindex = models.IntegerField(db_column='IfIndex', blank=True, null=True)  # Field name made lowercase.
    ifdescription = models.CharField(db_column='IfDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    iftype = models.DecimalField(db_column='IfType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ifmtu = models.DecimalField(db_column='IfMTU', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ifspeed = models.DecimalField(db_column='IfSpeed', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ifipaddress = models.CharField(db_column='IfIPAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ifmask = models.CharField(db_column='IfMask', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ifmacaddress = models.CharField(db_column='IfMacaddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ifadminstatus = models.IntegerField(db_column='IfAdminstatus', blank=True, null=True)  # Field name made lowercase.
    ifoperstatus = models.IntegerField(db_column='IfOperstatus', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    uplink = models.BooleanField(db_column='Uplink')  # Field name made lowercase.
    portname = models.CharField(db_column='Portname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vlan = models.CharField(db_column='Vlan', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ifname = models.CharField(db_column='ifName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ifalias = models.CharField(db_column='ifAlias', max_length=255, blank=True, null=True)  # Field name made lowercase.
    defaultgateway = models.CharField(db_column='DefaultGateway', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSNMPInfo'


class Tblsafeguids(models.Model):
    guid = models.CharField(primary_key=True, max_length=50)
    remark = models.CharField(db_column='Remark', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSafeguids'


class Tblscanhistory(models.Model):
    scanhistoryid = models.AutoField(db_column='ScanHistoryId', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    scanserver = models.CharField(db_column='ScanServer', max_length=60)  # Field name made lowercase.
    scanningmethodid = models.ForeignKey('Tsysscanningmethods', models.DO_NOTHING, db_column='ScanningMethodId')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    scantime = models.DateTimeField(db_column='ScanTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblScanHistory'


class Tblsccmasset(models.Model):
    sccmassetid = models.AutoField(db_column='SccmAssetId', primary_key=True)  # Field name made lowercase.
    sccmsiteid = models.ForeignKey('Tblsccmsite', models.DO_NOTHING, db_column='SccmSiteId')  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId', blank=True, null=True)  # Field name made lowercase.
    lastscandate = models.DateTimeField(db_column='LastScanDate')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25)  # Field name made lowercase.
    resourceid = models.BigIntegerField(db_column='ResourceId')  # Field name made lowercase.
    operatingsystemnameandversion = models.CharField(db_column='OperatingSystemNameandVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    resourcedomainorworkgroup = models.CharField(db_column='ResourceDomainORWorkgroup', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fulldomainname = models.CharField(db_column='FullDomainName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pcmanufacturer = models.CharField(db_column='PcManufacturer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pcmodel = models.CharField(db_column='PcModel', max_length=100, blank=True, null=True)  # Field name made lowercase.
    numberofprocessors = models.IntegerField(db_column='NumberOfProcessors', blank=True, null=True)  # Field name made lowercase.
    totalphysicalmemory = models.BigIntegerField(db_column='TotalPhysicalMemory', blank=True, null=True)  # Field name made lowercase.
    biosserialnumber = models.CharField(db_column='BiosSerialNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oscaption = models.CharField(db_column='OsCaption', max_length=100, blank=True, null=True)  # Field name made lowercase.
    osname = models.CharField(db_column='OsName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    csdversion = models.CharField(db_column='CsdVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    osmanufacturer = models.CharField(db_column='OsManufacturer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    osserialnumber = models.CharField(db_column='OsSerialNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    osversion = models.CharField(db_column='OsVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    normspeed = models.IntegerField(db_column='NormSpeed', blank=True, null=True)  # Field name made lowercase.
    numberofcores = models.IntegerField(db_column='NumberOfCores', blank=True, null=True)  # Field name made lowercase.
    cpumanufacturer = models.CharField(db_column='CpuManufacturer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IpAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ipnumeric = models.DecimalField(db_column='IpNumeric', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    assettype = models.IntegerField(db_column='Assettype')  # Field name made lowercase.
    hasclient = models.BooleanField(db_column='HasClient')  # Field name made lowercase.
    clientedition = models.IntegerField(db_column='ClientEdition', blank=True, null=True)  # Field name made lowercase.
    clientversion = models.CharField(db_column='ClientVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    cputype = models.CharField(db_column='CpuType', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSccmAsset'


class Tblsccmnetworkadapter(models.Model):
    sccmnetworkadapterid = models.AutoField(db_column='SccmNetworkAdapterId', primary_key=True)  # Field name made lowercase.
    sccmassetid = models.ForeignKey(Tblsccmasset, models.DO_NOTHING, db_column='SccmAssetId')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IpAddress', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ipsubnet = models.CharField(db_column='IpSubnet', max_length=25, blank=True, null=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', max_length=25, blank=True, null=True)  # Field name made lowercase.
    servicename = models.CharField(db_column='ServiceName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    index = models.IntegerField(db_column='Index')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSccmNetworkAdapter'


class Tblsccmserver(models.Model):
    sccmserverid = models.AutoField(db_column='SccmServerId', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId', blank=True, null=True)  # Field name made lowercase.
    lastscandate = models.DateTimeField(db_column='LastScanDate', blank=True, null=True)  # Field name made lowercase.
    servername = models.CharField(db_column='ServerName', max_length=60)  # Field name made lowercase.
    domain = models.CharField(db_column='Domain', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSccmServer'


class Tblsccmsite(models.Model):
    sccmsiteid = models.AutoField(db_column='SccmSiteId', primary_key=True)  # Field name made lowercase.
    sccmserverid = models.ForeignKey(Tblsccmserver, models.DO_NOTHING, db_column='SccmServerId')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=25)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=25, blank=True, null=True)  # Field name made lowercase.
    buildnumber = models.IntegerField(db_column='BuildNumber', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSccmSite'


class Tblsccmsoftware(models.Model):
    sccmsoftwareid = models.AutoField(db_column='SccmSoftwareId', primary_key=True)  # Field name made lowercase.
    sccmassetid = models.ForeignKey(Tblsccmasset, models.DO_NOTHING, db_column='SccmAssetId')  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=500)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=100, blank=True, null=True)  # Field name made lowercase.
    publisher = models.CharField(db_column='Publisher', max_length=256, blank=True, null=True)  # Field name made lowercase.
    installdate = models.DateTimeField(db_column='InstallDate', blank=True, null=True)  # Field name made lowercase.
    is64bit = models.BooleanField(db_column='Is64Bit')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSccmSoftware'


class Tblscsicontroller(models.Model):
    win32_scsicontrollerid = models.AutoField(db_column='WIN32_SCSICONTROLLERid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    availability = models.DecimalField(db_column='Availability', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    protocolsupported = models.DecimalField(db_column='ProtocolSupported', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblScsiController'


class Tblscsicontrollerhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    availability = models.DecimalField(db_column='Availability', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    protocolsupported = models.DecimalField(db_column='ProtocolSupported', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblScsiControllerHist'


class Tblserialport(models.Model):
    win32_serialportid = models.AutoField(db_column='Win32_SerialPortid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    availability = models.DecimalField(db_column='Availability', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    binary = models.BooleanField(db_column='Binary', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    maxbaudrate = models.DecimalField(db_column='MaxBaudRate', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    maximuminputbuffersize = models.DecimalField(db_column='MaximumInputBufferSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    maximumoutputbuffersize = models.DecimalField(db_column='MaximumOutputBufferSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    osautodiscovered = models.BooleanField(db_column='OSAutoDiscovered', blank=True, null=True)  # Field name made lowercase.
    providertype = models.CharField(db_column='ProviderType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSerialPort'


class Tblserialporthist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    availability = models.DecimalField(db_column='Availability', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    binary = models.BooleanField(db_column='Binary', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    maxbaudrate = models.DecimalField(db_column='MaxBaudRate', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    maximuminputbuffersize = models.DecimalField(db_column='MaximumInputBufferSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    maximumoutputbuffersize = models.DecimalField(db_column='MaximumOutputBufferSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    osautodiscovered = models.BooleanField(db_column='OSAutoDiscovered', blank=True, null=True)  # Field name made lowercase.
    providertype = models.CharField(db_column='ProviderType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSerialPortHist'


class Tblserialnumber(models.Model):
    serialid = models.AutoField(db_column='SerialID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    product = models.CharField(db_column='Product', max_length=400, blank=True, null=True)  # Field name made lowercase.
    productid = models.CharField(db_column='ProductID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    productkey = models.CharField(db_column='ProductKey', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSerialnumber'


class Tblservicestartmode(models.Model):
    startid = models.IntegerField(db_column='StartID', primary_key=True)  # Field name made lowercase.
    startmode = models.CharField(db_column='StartMode', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblServiceStartMode'


class Tblservicestate(models.Model):
    stateid = models.IntegerField(db_column='StateID', primary_key=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblServiceState'


class Tblservices(models.Model):
    serviceid = models.AutoField(db_column='ServiceID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    serviceuniqueid = models.ForeignKey('Tblservicesuni', models.DO_NOTHING, db_column='ServiceuniqueID')  # Field name made lowercase.
    acceptpause = models.BooleanField(db_column='Acceptpause', blank=True, null=True)  # Field name made lowercase.
    acceptstop = models.BooleanField(db_column='Acceptstop', blank=True, null=True)  # Field name made lowercase.
    desktopinteract = models.BooleanField(db_column='Desktopinteract', blank=True, null=True)  # Field name made lowercase.
    started = models.BooleanField(db_column='Started')  # Field name made lowercase.
    startid = models.ForeignKey(Tblservicestartmode, models.DO_NOTHING, db_column='StartID', blank=True, null=True)  # Field name made lowercase.
    stateid = models.ForeignKey(Tblservicestate, models.DO_NOTHING, db_column='StateID', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblServices'


class Tblservicesuni(models.Model):
    serviceuniqueid = models.AutoField(db_column='ServiceuniqueID', primary_key=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=450, blank=True, null=True)  # Field name made lowercase.
    pathname = models.CharField(db_column='Pathname', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    startname = models.CharField(db_column='Startname', max_length=450, blank=True, null=True)  # Field name made lowercase.
    hash = models.CharField(db_column='Hash', unique=True, max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblServicesUni'


class Tblsharepermissions(models.Model):
    permissionid = models.AutoField(db_column='permissionId', primary_key=True)  # Field name made lowercase.
    shareid = models.ForeignKey('Tblshares', models.DO_NOTHING, db_column='ShareID')  # Field name made lowercase.
    trustee = models.CharField(max_length=64, blank=True, null=True)
    readaccess = models.BooleanField(db_column='readAccess', blank=True, null=True)  # Field name made lowercase.
    writeaccess = models.BooleanField(db_column='writeAccess', blank=True, null=True)  # Field name made lowercase.
    fullaccess = models.BooleanField(db_column='fullAccess', blank=True, null=True)  # Field name made lowercase.
    denyaccess = models.BooleanField(db_column='denyAccess', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='lastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSharePermissions'


class Tblshares(models.Model):
    shareid = models.AutoField(db_column='ShareID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    shareuniqueid = models.ForeignKey('Tblsharesuni', models.DO_NOTHING, db_column='ShareUniqueID')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblShares'


class Tblshareshist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    shareuniqueid = models.ForeignKey('Tblsharesuni', models.DO_NOTHING, db_column='ShareUniqueID')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSharesHist'


class Tblsharesuni(models.Model):
    shareuniqueid = models.AutoField(db_column='ShareUniqueID', primary_key=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=450, blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(db_column='Path', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    type = models.DecimalField(db_column='Type', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    hash = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'tblSharesUni'


class Tblsoftware(models.Model):
    softwareid = models.AutoField(db_column='SoftwareID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    softid = models.ForeignKey('Tblsoftwareuni', models.DO_NOTHING, db_column='softID')  # Field name made lowercase.
    softwareversion = models.CharField(db_column='softwareVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    installdate = models.DateTimeField(db_column='Installdate', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    currentuser = models.BooleanField(db_column='CurrentUser', blank=True, null=True)  # Field name made lowercase.
    msi = models.BooleanField(db_column='MSI', blank=True, null=True)  # Field name made lowercase.
    msstore = models.BooleanField(db_column='MsStore')  # Field name made lowercase.
    installlocation = models.CharField(db_column='InstallLocation', max_length=300, blank=True, null=True)  # Field name made lowercase.
    catalogsoftwareid = models.ForeignKey(Tblcatalogsoftware, models.DO_NOTHING, db_column='CatalogSoftwareId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSoftware'


class Tblsoftwarehist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    softid = models.IntegerField(blank=True, null=True)
    softwareversion = models.CharField(db_column='softwareVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    installdate = models.DateTimeField(db_column='Installdate', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    currentuser = models.BooleanField(db_column='CurrentUser', blank=True, null=True)  # Field name made lowercase.
    msi = models.BooleanField(db_column='MSI', blank=True, null=True)  # Field name made lowercase.
    msstore = models.BooleanField(db_column='MsStore')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSoftwareHist'


class Tblsoftwareuni(models.Model):
    softid = models.AutoField(db_column='SoftID', primary_key=True)  # Field name made lowercase.
    softwarename = models.CharField(db_column='softwareName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    softwarepublisher = models.CharField(db_column='SoftwarePublisher', max_length=256, blank=True, null=True)  # Field name made lowercase.
    approved = models.IntegerField(db_column='Approved')  # Field name made lowercase.
    ostype = models.IntegerField(db_column='OSType')  # Field name made lowercase.
    added = models.DateTimeField(db_column='Added')  # Field name made lowercase.
    applicationid = models.CharField(db_column='ApplicationId', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSoftwareUni'
        unique_together = (('softwarename', 'softwarepublisher', 'applicationid'),)


class Tblsounddevice(models.Model):
    win32_sounddeviceid = models.AutoField(db_column='Win32_SoundDeviceid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSoundDevice'


class Tblsounddevicehist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSoundDeviceHist'


class Tblsqldatabases(models.Model):
    sqldatabaseid = models.BigAutoField(db_column='sqlDatabaseId', primary_key=True)  # Field name made lowercase.
    datafilessizekb = models.BigIntegerField(db_column='dataFilesSizeKb', blank=True, null=True)  # Field name made lowercase.
    logfilessizekb = models.BigIntegerField(db_column='logFilesSizeKb', blank=True, null=True)  # Field name made lowercase.
    logfilesusedsizekb = models.BigIntegerField(db_column='logFilesUsedSizeKb', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    lastchanged = models.DateTimeField(db_column='Lastchanged', blank=True, null=True)  # Field name made lowercase.
    sqlserverid = models.ForeignKey('Tblsqlservers', models.DO_NOTHING, db_column='sqlServerId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSqlDatabases'


class Tblsqllicensedocs(models.Model):
    docid = models.AutoField(db_column='DocID', primary_key=True)  # Field name made lowercase.
    licenseid = models.ForeignKey('Tblsqllicenses', models.DO_NOTHING, db_column='LicenseID')  # Field name made lowercase.
    doclink = models.CharField(db_column='Doclink', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    docname = models.CharField(db_column='Docname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSqlLicenseDocs'


class Tblsqllicenses(models.Model):
    licenseid = models.AutoField(db_column='LicenseID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=300, blank=True, null=True)  # Field name made lowercase.
    priceperserver = models.DecimalField(db_column='PricePerServer', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    licensetype = models.ForeignKey('Tsyssqllicensetypes', models.DO_NOTHING, db_column='LicenseType', blank=True, null=True)  # Field name made lowercase.
    licensetypecomments = models.TextField(db_column='LicenseTypeComments', blank=True, null=True)  # Field name made lowercase.
    nrofterms = models.IntegerField(db_column='NrOfTerms', blank=True, null=True)  # Field name made lowercase.
    priceperterm = models.DecimalField(db_column='PricePerTerm', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    licensecontact = models.CharField(db_column='LicenseContact', max_length=500, blank=True, null=True)  # Field name made lowercase.
    licenseowner = models.CharField(db_column='LicenseOwner', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sharedcal = models.BooleanField(db_column='SharedCAL', blank=True, null=True)  # Field name made lowercase.
    licenseexpiration = models.DateTimeField(db_column='LicenseExpiration', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSqlLicenses'


class Tblsqllicensesorders(models.Model):
    licenseorderid = models.AutoField(db_column='Licenseorderid', primary_key=True)  # Field name made lowercase.
    licenseid = models.ForeignKey(Tblsqllicenses, models.DO_NOTHING, db_column='LicenseID')  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='Orderdate', blank=True, null=True)  # Field name made lowercase.
    nrlicenses = models.IntegerField(db_column='Nrlicenses', blank=True, null=True)  # Field name made lowercase.
    priceperlicense = models.DecimalField(db_column='Priceperlicense', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ordernumber = models.CharField(db_column='Ordernumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSqlLicensesOrders'


class Tblsqllicensesserverorders(models.Model):
    licenseorderid = models.AutoField(db_column='Licenseorderid', primary_key=True)  # Field name made lowercase.
    licenseid = models.ForeignKey(Tblsqllicenses, models.DO_NOTHING, db_column='LicenseID')  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='Orderdate', blank=True, null=True)  # Field name made lowercase.
    nrlicenses = models.IntegerField(db_column='Nrlicenses', blank=True, null=True)  # Field name made lowercase.
    priceperlicense = models.DecimalField(db_column='Priceperlicense', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ordernumber = models.CharField(db_column='Ordernumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSqlLicensesServerOrders'


class Tblsqlservercluster(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSqlServerCluster'


class Tblsqlserverclusternode(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    clusterid = models.ForeignKey(Tblsqlservercluster, models.DO_NOTHING, db_column='ClusterId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSqlServerClusterNode'


class Tblsqlserverservice(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sqlserverid = models.ForeignKey('Tblsqlservers', models.DO_NOTHING, db_column='SqlServerId')  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    startuptype = models.IntegerField(db_column='StartupType', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSqlServerService'


class Tblsqlservers(models.Model):
    sqlserverid = models.BigAutoField(db_column='sqlServerId', primary_key=True)  # Field name made lowercase.
    datapath = models.CharField(db_column='dataPath', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    fileversion = models.CharField(db_column='fileVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    installpath = models.CharField(db_column='installPath', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    iswow64 = models.IntegerField(db_column='isWow64', blank=True, null=True)  # Field name made lowercase.
    language = models.IntegerField(blank=True, null=True)
    skuname = models.CharField(db_column='skuName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    splevel = models.IntegerField(db_column='spLevel', blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=255, blank=True, null=True)
    displayversion = models.CharField(db_column='displayVersion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='lastChanged', blank=True, null=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    servicename = models.CharField(db_column='serviceName', max_length=255)  # Field name made lowercase.
    authentication = models.IntegerField(db_column='Authentication')  # Field name made lowercase.
    isclustered = models.BooleanField(db_column='IsClustered')  # Field name made lowercase.
    clusterid = models.ForeignKey(Tblsqlservercluster, models.DO_NOTHING, db_column='ClusterId', blank=True, null=True)  # Field name made lowercase.
    instanceid = models.CharField(db_column='InstanceId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    instancename = models.CharField(db_column='InstanceName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSqlServers'


class Tblsqlsubservers(models.Model):
    subserverid = models.AutoField(db_column='SubServerID', primary_key=True)  # Field name made lowercase.
    licenseid = models.ForeignKey(Tblsqllicenses, models.DO_NOTHING, db_column='LicenseID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=300, blank=True, null=True)  # Field name made lowercase.
    assetname = models.CharField(db_column='AssetName', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSqlSubServers'


class Tblstate(models.Model):
    state = models.IntegerField(db_column='State', primary_key=True)  # Field name made lowercase.
    statename = models.CharField(db_column='Statename', max_length=300)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblState'


class Tblsublicensedocs(models.Model):
    licensesubdocid = models.AutoField(db_column='LicensesubdocID', primary_key=True)  # Field name made lowercase.
    licenseidid = models.ForeignKey(Tbllicenses, models.DO_NOTHING, db_column='LicenseidID')  # Field name made lowercase.
    doclink = models.CharField(db_column='Doclink', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    docname = models.CharField(db_column='Docname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSublicenseDocs'


class Tblsublicenses(models.Model):
    licensesubid = models.AutoField(db_column='LicensesubID', primary_key=True)  # Field name made lowercase.
    licenseidid = models.ForeignKey(Tbllicenses, models.DO_NOTHING, db_column='LicenseidID')  # Field name made lowercase.
    softwarename = models.CharField(db_column='softwareName', max_length=300)  # Field name made lowercase.
    softwareversion = models.CharField(db_column='softwareVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSublicenses'
        unique_together = (('softwarename', 'softwareversion'),)


class Tblsublicensesorders(models.Model):
    licensesuborderid = models.AutoField(db_column='LicensesuborderID', primary_key=True)  # Field name made lowercase.
    licenseidid = models.ForeignKey(Tbllicenses, models.DO_NOTHING, db_column='LicenseidID')  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='Orderdate')  # Field name made lowercase.
    nrlicenses = models.IntegerField(db_column='Nrlicenses')  # Field name made lowercase.
    priceperlicense = models.DecimalField(db_column='Priceperlicense', max_digits=19, decimal_places=4)  # Field name made lowercase.
    ordernumber = models.CharField(db_column='Ordernumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    licensekey = models.TextField(db_column='Licensekey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSublicensesOrders'


class Tblsystemdriverpnpentity(models.Model):
    systemdriverpnpentityid = models.BigAutoField(db_column='SystemDriverPnpEntityID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=200)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSystemDriverPnpEntity'


class Tblsystemdrivers(models.Model):
    systemdriverid = models.BigAutoField(db_column='SystemDriverID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    systemdriveruniid = models.ForeignKey('Tblsystemdriversuni', models.DO_NOTHING, db_column='SystemDriverUniID')  # Field name made lowercase.
    acceptpause = models.BooleanField(db_column='AcceptPause')  # Field name made lowercase.
    acceptstop = models.BooleanField(db_column='AcceptStop')  # Field name made lowercase.
    desktopinteract = models.BooleanField(db_column='DesktopInteract')  # Field name made lowercase.
    started = models.BooleanField(db_column='Started')  # Field name made lowercase.
    startmode = models.CharField(db_column='StartMode', max_length=10)  # Field name made lowercase.
    startname = models.CharField(db_column='StartName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pathname = models.CharField(db_column='PathName', max_length=250, blank=True, null=True)  # Field name made lowercase.
    errorcontrol = models.CharField(db_column='ErrorControl', max_length=20, blank=True, null=True)  # Field name made lowercase.
    servicetype = models.CharField(db_column='ServiceType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    exitcode = models.BigIntegerField(db_column='ExitCode', blank=True, null=True)  # Field name made lowercase.
    servicespecificexitcode = models.BigIntegerField(db_column='ServiceSpecificExitCode', blank=True, null=True)  # Field name made lowercase.
    tagid = models.BigIntegerField(db_column='TagId', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSystemDrivers'
        unique_together = (('assetid', 'systemdriveruniid'),)


class Tblsystemdriversuni(models.Model):
    systemdriveruniid = models.AutoField(db_column='SystemDriverUniID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=100, blank=True, null=True)  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSystemDriversUni'


class Tblsystemenclosure(models.Model):
    win32_systemenclosureid = models.AutoField(db_column='Win32_SystemEnclosureid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    chassistypes = models.DecimalField(db_column='ChassisTypes', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lockpresent = models.BooleanField(db_column='LockPresent', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    securitystatus = models.DecimalField(db_column='SecurityStatus', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=300, blank=True, null=True)  # Field name made lowercase.
    smbiosassettag = models.CharField(db_column='SMBIOSAssetTag', max_length=300, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=300, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSystemEnclosure'


class Tblsystemenclosurehist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    chassistypes = models.DecimalField(db_column='ChassisTypes', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lockpresent = models.BooleanField(db_column='LockPresent', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    securitystatus = models.DecimalField(db_column='SecurityStatus', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=300, blank=True, null=True)  # Field name made lowercase.
    smbiosassettag = models.CharField(db_column='SMBIOSAssetTag', max_length=300, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=300, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSystemEnclosureHist'


class Tbltpm(models.Model):
    win32_tpmid = models.AutoField(db_column='Win32_TpmId', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    isactivated_initialvalue = models.BooleanField(db_column='IsActivated_InitialValue', blank=True, null=True)  # Field name made lowercase.
    isenabled_initialvalue = models.BooleanField(db_column='IsEnabled_InitialValue', blank=True, null=True)  # Field name made lowercase.
    isowned_initialvalue = models.BooleanField(db_column='IsOwned_InitialValue', blank=True, null=True)  # Field name made lowercase.
    specversion = models.CharField(db_column='SpecVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    manufacturerversion = models.CharField(db_column='ManufacturerVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    manufacturerversioninfo = models.CharField(db_column='ManufacturerVersionInfo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    manufacturerid = models.IntegerField(db_column='ManufacturerId', blank=True, null=True)  # Field name made lowercase.
    physicalpresenceversioninfo = models.CharField(db_column='PhysicalPresenceVersionInfo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTPM'


class Tbltapedrive(models.Model):
    win32_tapedriveid = models.AutoField(db_column='Win32_TapeDriveid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    availability = models.DecimalField(db_column='Availability', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    capabilities = models.CharField(db_column='Capabilities', max_length=500, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    compression = models.DecimalField(db_column='Compression', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    defaultblocksize = models.DecimalField(db_column='DefaultBlockSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    maxblocksize = models.DecimalField(db_column='MaxBlockSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    maxmediasize = models.DecimalField(db_column='MaxMediaSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    maxpartitioncount = models.DecimalField(db_column='MaxPartitionCount', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mediatype = models.CharField(db_column='MediaType', max_length=450, blank=True, null=True)  # Field name made lowercase.
    minblocksize = models.DecimalField(db_column='MinBlockSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    needscleaning = models.BooleanField(db_column='NeedsCleaning', blank=True, null=True)  # Field name made lowercase.
    numberofmediasupported = models.DecimalField(db_column='NumberOfMediaSupported', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    padding = models.DecimalField(db_column='Padding', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTapeDrive'


class Tbltapedrivehist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    availability = models.DecimalField(db_column='Availability', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    capabilities = models.CharField(db_column='Capabilities', max_length=500, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    compression = models.DecimalField(db_column='Compression', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    defaultblocksize = models.DecimalField(db_column='DefaultBlockSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    maxblocksize = models.DecimalField(db_column='MaxBlockSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    maxmediasize = models.DecimalField(db_column='MaxMediaSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    maxpartitioncount = models.DecimalField(db_column='MaxPartitionCount', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mediatype = models.CharField(db_column='MediaType', max_length=450, blank=True, null=True)  # Field name made lowercase.
    minblocksize = models.DecimalField(db_column='MinBlockSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    needscleaning = models.BooleanField(db_column='NeedsCleaning', blank=True, null=True)  # Field name made lowercase.
    numberofmediasupported = models.DecimalField(db_column='NumberOfMediaSupported', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    padding = models.DecimalField(db_column='Padding', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTapeDriveHist'


class Tblusbcontroller(models.Model):
    win32_usbcontrollerid = models.AutoField(db_column='Win32_USBControllerid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    protocolsupported = models.DecimalField(db_column='ProtocolSupported', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUSBController'


class Tblusbcontrollerhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    protocolsupported = models.DecimalField(db_column='ProtocolSupported', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUSBControllerHist'


class Tblusbdevices(models.Model):
    win32_usbdeviceid = models.AutoField(db_column='Win32_USBDeviceid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=450, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=450, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUSBDevices'


class Tblups(models.Model):
    upsid = models.AutoField(db_column='UpsId', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    upssoftwareversion = models.CharField(db_column='UpsSoftwareVersion', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    agentsoftwareversion = models.CharField(db_column='AgentSoftwareVersion', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    attacheddevices = models.CharField(db_column='AttachedDevices', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    batterystatus = models.IntegerField(db_column='BatteryStatus', blank=True, null=True)  # Field name made lowercase.
    secondsonbattery = models.IntegerField(db_column='SecondsOnBattery', blank=True, null=True)  # Field name made lowercase.
    estimatedminutesremaining = models.IntegerField(db_column='EstimatedMinutesRemaining', blank=True, null=True)  # Field name made lowercase.
    estimatedchargeremaining = models.IntegerField(db_column='EstimatedChargeRemaining', blank=True, null=True)  # Field name made lowercase.
    batteryvoltage = models.IntegerField(db_column='BatteryVoltage', blank=True, null=True)  # Field name made lowercase.
    batterycurrent = models.IntegerField(db_column='BatteryCurrent', blank=True, null=True)  # Field name made lowercase.
    batterytemperature = models.IntegerField(db_column='BatteryTemperature', blank=True, null=True)  # Field name made lowercase.
    alarmspresent = models.IntegerField(db_column='AlarmsPresent', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUps'


class Tbluptime(models.Model):
    uptimeid = models.AutoField(db_column='UptimeID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    eventtime = models.DateTimeField(db_column='EventTime')  # Field name made lowercase.
    eventtype = models.SmallIntegerField(db_column='EventType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUptime'


class Tblusers(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID', blank=True, null=True)  # Field name made lowercase.
    accounttype = models.DecimalField(db_column='Accounttype', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    disabled = models.BooleanField(db_column='Disabled', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='Fullname', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lockout = models.BooleanField(db_column='Lockout', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=300, blank=True, null=True)  # Field name made lowercase.
    passwordchangeable = models.BooleanField(db_column='PasswordChangeable', blank=True, null=True)  # Field name made lowercase.
    passwordexpires = models.BooleanField(db_column='PasswordExpires', blank=True, null=True)  # Field name made lowercase.
    passwordrequired = models.BooleanField(db_column='PasswordRequired', blank=True, null=True)  # Field name made lowercase.
    sid = models.CharField(db_column='SID', max_length=300, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    buildinadmin = models.BooleanField(db_column='BuildInAdmin')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUsers'


class Tblusershist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID', blank=True, null=True)  # Field name made lowercase.
    accounttype = models.DecimalField(db_column='Accounttype', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    disabled = models.BooleanField(db_column='Disabled', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='Fullname', max_length=450, blank=True, null=True)  # Field name made lowercase.
    lockout = models.BooleanField(db_column='Lockout', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=300, blank=True, null=True)  # Field name made lowercase.
    passwordchangeable = models.BooleanField(db_column='PasswordChangeable', blank=True, null=True)  # Field name made lowercase.
    passwordexpires = models.BooleanField(db_column='PasswordExpires', blank=True, null=True)  # Field name made lowercase.
    passwordrequired = models.BooleanField(db_column='PasswordRequired', blank=True, null=True)  # Field name made lowercase.
    sid = models.CharField(db_column='SID', max_length=300, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    buildinadmin = models.BooleanField(db_column='BuildInAdmin')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUsersHist'


class Tblusersingroup(models.Model):
    useringroupid = models.AutoField(db_column='UserInGroupID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    groupname = models.CharField(db_column='Groupname', max_length=300, blank=True, null=True)  # Field name made lowercase.
    domainname = models.CharField(db_column='Domainname', max_length=300, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=300, blank=True, null=True)  # Field name made lowercase.
    accounttype = models.DecimalField(db_column='Accounttype', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    admingroup = models.BooleanField(db_column='Admingroup')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUsersInGroup'


class Tblusersingrouphist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    groupname = models.CharField(db_column='Groupname', max_length=300, blank=True, null=True)  # Field name made lowercase.
    domainname = models.CharField(db_column='Domainname', max_length=200, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accounttype = models.DecimalField(db_column='Accounttype', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    admingroup = models.BooleanField(db_column='Admingroup')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUsersInGroupHist'


class Tblvideocontroller(models.Model):
    win32_videocontrollerid = models.AutoField(db_column='Win32_VideoControllerid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    adaptercompatibility = models.CharField(db_column='AdapterCompatibility', max_length=450, blank=True, null=True)  # Field name made lowercase.
    adapterram = models.DecimalField(db_column='AdapterRAM', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    availability = models.DecimalField(db_column='Availability', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    currentbitsperpixel = models.DecimalField(db_column='CurrentBitsPerPixel', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    currenthorizontalresolution = models.DecimalField(db_column='CurrentHorizontalResolution', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    currentnumberofcolors = models.DecimalField(db_column='CurrentNumberOfColors', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    currentrefreshrate = models.DecimalField(db_column='CurrentRefreshRate', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    currentscanmode = models.DecimalField(db_column='CurrentScanMode', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    currentverticalresolution = models.DecimalField(db_column='CurrentVerticalResolution', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=500, blank=True, null=True)  # Field name made lowercase.
    devicespecificpens = models.DecimalField(db_column='DeviceSpecificPens', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    driverversion = models.CharField(db_column='DriverVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    maxrefreshrate = models.DecimalField(db_column='MaxRefreshRate', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    minrefreshrate = models.DecimalField(db_column='MinRefreshRate', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    monochrome = models.BooleanField(db_column='Monochrome', blank=True, null=True)  # Field name made lowercase.
    numberofcolorplanes = models.DecimalField(db_column='NumberOfColorPlanes', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    videoarchitecture = models.DecimalField(db_column='VideoArchitecture', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    videomemorytype = models.DecimalField(db_column='VideoMemoryType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    videomodedescription = models.CharField(db_column='VideoModeDescription', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblVideoController'


class Tblvideocontrollerhist(models.Model):
    trackercode = models.AutoField(db_column='Trackercode', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    adaptercompatibility = models.CharField(db_column='AdapterCompatibility', max_length=450, blank=True, null=True)  # Field name made lowercase.
    adapterram = models.DecimalField(db_column='AdapterRAM', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    availability = models.DecimalField(db_column='Availability', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=450, blank=True, null=True)  # Field name made lowercase.
    currentbitsperpixel = models.DecimalField(db_column='CurrentBitsPerPixel', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    currenthorizontalresolution = models.DecimalField(db_column='CurrentHorizontalResolution', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    currentnumberofcolors = models.DecimalField(db_column='CurrentNumberOfColors', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    currentrefreshrate = models.DecimalField(db_column='CurrentRefreshRate', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    currentscanmode = models.DecimalField(db_column='CurrentScanMode', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    currentverticalresolution = models.DecimalField(db_column='CurrentVerticalResolution', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=500, blank=True, null=True)  # Field name made lowercase.
    devicespecificpens = models.DecimalField(db_column='DeviceSpecificPens', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    driverversion = models.CharField(db_column='DriverVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    maxrefreshrate = models.DecimalField(db_column='MaxRefreshRate', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    minrefreshrate = models.DecimalField(db_column='MinRefreshRate', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    monochrome = models.BooleanField(db_column='Monochrome', blank=True, null=True)  # Field name made lowercase.
    numberofcolorplanes = models.DecimalField(db_column='NumberOfColorPlanes', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    videoarchitecture = models.DecimalField(db_column='VideoArchitecture', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    videomemorytype = models.DecimalField(db_column='VideoMemoryType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    videomodedescription = models.CharField(db_column='VideoModeDescription', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.
    action = models.DecimalField(db_column='Action', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblVideoControllerHist'


class Tblvmwaredatacenters(models.Model):
    datacenterid = models.AutoField(db_column='DatacenterID', primary_key=True)  # Field name made lowercase.
    internalkey = models.CharField(db_column='InternalKey', max_length=256, blank=True, null=True)  # Field name made lowercase.
    vcenterid = models.ForeignKey('Tblvmwarevcenters', models.DO_NOTHING, db_column='VcenterID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblVmwareDatacenters'


class Tblvmwaredatastoreclusterconfigrules(models.Model):
    configruleid = models.AutoField(db_column='ConfigRuleID', primary_key=True)  # Field name made lowercase.
    datastoreclusterid = models.IntegerField(db_column='DatastoreClusterID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblVmwareDatastoreClusterConfigRules'


class Tblvmwaredatastoreclustervmoverrides(models.Model):
    vmoverrideid = models.AutoField(db_column='VmOverrideID', primary_key=True)  # Field name made lowercase.
    datastoreclusterid = models.IntegerField(db_column='DatastoreClusterID')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled', blank=True, null=True)  # Field name made lowercase.
    behaviour = models.CharField(db_column='Behaviour', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intravmaffinity = models.BooleanField(db_column='IntraVmAffinity', blank=True, null=True)  # Field name made lowercase.
    intravmantiaffinity = models.CharField(db_column='IntraVmAntiAffinity', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblVmwareDatastoreClusterVmOverrides'


class Tblvmwaredatastoreclusters(models.Model):
    datastoreclusterid = models.AutoField(db_column='DatastoreClusterID', primary_key=True)  # Field name made lowercase.
    datacenterid = models.ForeignKey(Tblvmwaredatacenters, models.DO_NOTHING, db_column='DatacenterID')  # Field name made lowercase.
    internalkey = models.CharField(db_column='InternalKey', max_length=256, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    freespace = models.BigIntegerField(db_column='FreeSpace')  # Field name made lowercase.
    capacity = models.BigIntegerField(db_column='Capacity')  # Field name made lowercase.
    drsenabled = models.BooleanField(db_column='DrsEnabled', blank=True, null=True)  # Field name made lowercase.
    ioloadbalanceenabled = models.BooleanField(db_column='IoLoadBalanceEnabled', blank=True, null=True)  # Field name made lowercase.
    defaultintravmaffinity = models.BooleanField(db_column='DefaultIntraVmAffinity', blank=True, null=True)  # Field name made lowercase.
    defaultvmbehaviour = models.CharField(db_column='DefaultVmBehaviour', max_length=50, blank=True, null=True)  # Field name made lowercase.
    loadbalanceinterval = models.IntegerField(db_column='LoadBalanceInterval', blank=True, null=True)  # Field name made lowercase.
    spaceutilizationthreshold = models.IntegerField(db_column='SpaceUtilizationThreshold', blank=True, null=True)  # Field name made lowercase.
    minspaceutilizationdifference = models.IntegerField(db_column='MinSpaceUtilizationDifference', blank=True, null=True)  # Field name made lowercase.
    iolatencythreshold = models.IntegerField(db_column='IoLatencyThreshold', blank=True, null=True)  # Field name made lowercase.
    ioloadimbalancethreshold = models.IntegerField(db_column='IoLoadImbalanceThreshold', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblVmwareDatastoreClusters'


class Tblvmwaredatastores(models.Model):
    datastoreid = models.AutoField(db_column='DatastoreID', primary_key=True)  # Field name made lowercase.
    hostid = models.IntegerField(db_column='HostID', blank=True, null=True)  # Field name made lowercase.
    internalkey = models.CharField(db_column='InternalKey', max_length=256, blank=True, null=True)  # Field name made lowercase.
    datacenterid = models.IntegerField(db_column='DatacenterID', blank=True, null=True)  # Field name made lowercase.
    datastoreclusterid = models.IntegerField(db_column='DatastoreClusterID', blank=True, null=True)  # Field name made lowercase.
    uncommitted = models.BigIntegerField(db_column='Uncommitted', blank=True, null=True)  # Field name made lowercase.
    accessible = models.BooleanField(db_column='Accessible', blank=True, null=True)  # Field name made lowercase.
    multiplehostaccess = models.BooleanField(db_column='MultipleHostAccess', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maintenancemode = models.CharField(db_column='MaintenanceMode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maxphysicalrdmfilesize = models.BigIntegerField(db_column='MaxPhysicalRdmFileSize', blank=True, null=True)  # Field name made lowercase.
    maxvirtualrdmfilesize = models.BigIntegerField(db_column='MaxVirtualRdmFileSize', blank=True, null=True)  # Field name made lowercase.
    maxfilesize = models.BigIntegerField(db_column='MaxFileSize', blank=True, null=True)  # Field name made lowercase.
    maxvirtualdiskcapacity = models.BigIntegerField(db_column='MaxVirtualDiskCapacity', blank=True, null=True)  # Field name made lowercase.
    maxmemoryfilesize = models.BigIntegerField(db_column='MaxMemoryFileSize', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblVmwareDatastores'


class Tblvmwaredisk(models.Model):
    diskid = models.BigAutoField(db_column='DiskID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    totalspace = models.BigIntegerField(db_column='TotalSpace', blank=True, null=True)  # Field name made lowercase.
    freespace = models.BigIntegerField(db_column='FreeSpace', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(blank=True, null=True)
    datastoreid = models.ForeignKey(Tblvmwaredatastores, models.DO_NOTHING, db_column='DatastoreID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblVmwareDisk'


class Tblvmwareesxiclusters(models.Model):
    esxiclusterid = models.AutoField(db_column='EsxiClusterID', primary_key=True)  # Field name made lowercase.
    datacenterid = models.ForeignKey(Tblvmwaredatacenters, models.DO_NOTHING, db_column='DatacenterID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    totalcpu = models.IntegerField(db_column='TotalCpu', blank=True, null=True)  # Field name made lowercase.
    totalmemory = models.BigIntegerField(db_column='TotalMemory', blank=True, null=True)  # Field name made lowercase.
    numcpucores = models.IntegerField(db_column='NumCpuCores', blank=True, null=True)  # Field name made lowercase.
    numcputhreads = models.IntegerField(db_column='NumCpuThreads', blank=True, null=True)  # Field name made lowercase.
    effectivecpu = models.IntegerField(db_column='EffectiveCpu', blank=True, null=True)  # Field name made lowercase.
    effectivememory = models.BigIntegerField(db_column='EffectiveMemory', blank=True, null=True)  # Field name made lowercase.
    numhosts = models.IntegerField(db_column='NumHosts', blank=True, null=True)  # Field name made lowercase.
    numeffectivehosts = models.IntegerField(db_column='NumEffectiveHosts', blank=True, null=True)  # Field name made lowercase.
    overallstatus = models.CharField(db_column='OverallStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblVmwareEsxiClusters'


class Tblvmwareguest(models.Model):
    guestid = models.AutoField(db_column='GuestID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    memory = models.DecimalField(db_column='Memory', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    isrunning = models.CharField(db_column='IsRunning', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(blank=True, null=True)
    toolsrunningstatus = models.SmallIntegerField(db_column='ToolsRunningStatus', blank=True, null=True)  # Field name made lowercase.
    toolsversion = models.CharField(db_column='ToolsVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    toolsversionstatus = models.SmallIntegerField(db_column='ToolsVersionStatus', blank=True, null=True)  # Field name made lowercase.
    toolsstatus = models.SmallIntegerField(db_column='ToolsStatus', blank=True, null=True)  # Field name made lowercase.
    cpucount = models.IntegerField(db_column='CpuCount', blank=True, null=True)  # Field name made lowercase.
    hostid = models.IntegerField(db_column='HostID', blank=True, null=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    internalkey = models.CharField(db_column='InternalKey', max_length=256, blank=True, null=True)  # Field name made lowercase.
    esxikey = models.CharField(db_column='EsxiKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    boottime = models.DateTimeField(db_column='BootTime', blank=True, null=True)  # Field name made lowercase.
    guestkey = models.CharField(db_column='GuestKey', max_length=255, blank=True, null=True)  # Field name made lowercase.
    guestfullname = models.CharField(db_column='GuestFullName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hostname = models.CharField(db_column='HostName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ipv4address = models.CharField(db_column='Ipv4Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numethernetcards = models.IntegerField(db_column='NumEthernetCards', blank=True, null=True)  # Field name made lowercase.
    numvirtualdisks = models.IntegerField(db_column='NumVirtualDisks', blank=True, null=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='Uuid', max_length=36, blank=True, null=True)  # Field name made lowercase.
    instanceuuid = models.CharField(db_column='InstanceUuid', max_length=36, blank=True, null=True)  # Field name made lowercase.
    unsharedstorage = models.BigIntegerField(db_column='UnsharedStorage', blank=True, null=True)  # Field name made lowercase.
    datastoreclusterdrsvmoverrideid = models.ForeignKey(Tblvmwaredatastoreclustervmoverrides, models.DO_NOTHING, db_column='DatastoreClusterDrsVmOverrideID', blank=True, null=True)  # Field name made lowercase.
    assettype = models.IntegerField(db_column='AssetType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblVmwareGuest'


class Tblvmwareguestnetwork(models.Model):
    guestnetworkid = models.AutoField(db_column='GuestNetworkID', primary_key=True)  # Field name made lowercase.
    guestid = models.ForeignKey(Tblvmwareguest, models.DO_NOTHING, db_column='GuestID')  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dnsaddresses = models.CharField(db_column='DnsAddresses', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    domainname = models.CharField(db_column='DomainName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IpAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subnetmask = models.CharField(db_column='SubnetMask', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ipv4dhcpenabled = models.BooleanField(db_column='Ipv4DhcpEnabled', blank=True, null=True)  # Field name made lowercase.
    ipv6dhcpenabled = models.BooleanField(db_column='Ipv6DhcpEnabled', blank=True, null=True)  # Field name made lowercase.
    ipv6addresses = models.CharField(db_column='IPv6Addresses', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    isconnected = models.BooleanField(db_column='IsConnected', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblVmwareGuestNetwork'


class Tblvmwareguestsnapshots(models.Model):
    snapshotid = models.AutoField(db_column='SnapshotID', primary_key=True)  # Field name made lowercase.
    internalkey = models.CharField(db_column='InternalKey', max_length=256, blank=True, null=True)  # Field name made lowercase.
    guestid = models.ForeignKey(Tblvmwareguest, models.DO_NOTHING, db_column='GuestID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblVmwareGuestSnapShots'


class Tblvmwareinfo(models.Model):
    vmwareid = models.AutoField(db_column='VmwareID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=400, blank=True, null=True)  # Field name made lowercase.
    biosversion = models.CharField(db_column='BiosVersion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    biosdate = models.DateTimeField(db_column='BiosDate', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField()
    numcpucores = models.IntegerField(db_column='numCpuCores', blank=True, null=True)  # Field name made lowercase.
    numcpupkgs = models.IntegerField(db_column='numCpuPkgs', blank=True, null=True)  # Field name made lowercase.
    numcputhreads = models.IntegerField(db_column='numCpuThreads', blank=True, null=True)  # Field name made lowercase.
    hostname = models.CharField(db_column='HostName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    internalkey = models.CharField(db_column='InternalKey', max_length=256, blank=True, null=True)  # Field name made lowercase.
    datacenterid = models.IntegerField(db_column='DatacenterID', blank=True, null=True)  # Field name made lowercase.
    esxiclusterid = models.IntegerField(db_column='EsxiClusterID', blank=True, null=True)  # Field name made lowercase.
    admindisabled = models.BooleanField(db_column='AdminDisabled', blank=True, null=True)  # Field name made lowercase.
    dnsaddresses = models.CharField(db_column='DnsAddresses', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    defaultgateway = models.CharField(db_column='DefaultGateway', max_length=50, blank=True, null=True)  # Field name made lowercase.
    domainname = models.CharField(db_column='DomainName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dhcp = models.BooleanField(db_column='Dhcp', blank=True, null=True)  # Field name made lowercase.
    connectionstate = models.CharField(db_column='ConnectionState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    powerstate = models.CharField(db_column='PowerState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    boottime = models.DateTimeField(db_column='BootTime', blank=True, null=True)  # Field name made lowercase.
    uptime = models.BigIntegerField(db_column='UpTime', blank=True, null=True)  # Field name made lowercase.
    hostmaxvirtualdiskcapacity = models.BigIntegerField(db_column='HostMaxVirtualDiskCapacity', blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IpAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port', blank=True, null=True)  # Field name made lowercase.
    sslthumbprint = models.CharField(db_column='SslThumbprint', max_length=255, blank=True, null=True)  # Field name made lowercase.
    managementserverip = models.CharField(db_column='ManagementServerIp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='Uuid', max_length=36, blank=True, null=True)  # Field name made lowercase.
    memorysize = models.BigIntegerField(db_column='MemorySize', blank=True, null=True)  # Field name made lowercase.
    cpumodel = models.CharField(db_column='CpuModel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpumhz = models.IntegerField(db_column='CpuMhz', blank=True, null=True)  # Field name made lowercase.
    cpupackagesdescriptions = models.CharField(db_column='CpuPackagesDescriptions', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    numnics = models.IntegerField(db_column='NumNics', blank=True, null=True)  # Field name made lowercase.
    numhbas = models.IntegerField(db_column='NumHbas', blank=True, null=True)  # Field name made lowercase.
    serial = models.CharField(db_column='Serial', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblVmwareInfo'


class Tblvmwarenetwork(models.Model):
    networkid = models.AutoField(db_column='NetworkID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mac = models.CharField(db_column='MAC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subnet = models.CharField(db_column='Subnet', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(blank=True, null=True)
    hostid = models.IntegerField(db_column='HostID', blank=True, null=True)  # Field name made lowercase.
    internalkey = models.CharField(db_column='InternalKey', max_length=256, blank=True, null=True)  # Field name made lowercase.
    networktype = models.IntegerField(db_column='NetworkType', blank=True, null=True)  # Field name made lowercase.
    ipv6addresses = models.CharField(db_column='IPv6Addresses', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    speed = models.IntegerField(db_column='Speed', blank=True, null=True)  # Field name made lowercase.
    mtu = models.IntegerField(db_column='Mtu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblVmwareNetwork'


class Tblvmwarenetworktypes(models.Model):
    networktypeid = models.IntegerField(db_column='NetworkTypeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblVmwareNetworkTypes'


class Tblvmwareproductinfo(models.Model):
    productinfoid = models.AutoField(db_column='ProductInfoID', primary_key=True)  # Field name made lowercase.
    hostid = models.IntegerField(db_column='HostID', blank=True, null=True)  # Field name made lowercase.
    vcenterid = models.IntegerField(db_column='VCenterID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    apitype = models.CharField(db_column='ApiType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    apiversion = models.CharField(db_column='ApiVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    build = models.CharField(db_column='Build', max_length=50)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=255)  # Field name made lowercase.
    instanceuuid = models.CharField(db_column='InstanceUuid', max_length=36, blank=True, null=True)  # Field name made lowercase.
    licenseproductname = models.CharField(db_column='LicenseProductName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    licenseproductversion = models.CharField(db_column='LicenseProductVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    localebuild = models.CharField(db_column='LocaleBuild', max_length=50, blank=True, null=True)  # Field name made lowercase.
    localeversion = models.CharField(db_column='LocaleVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ostype = models.CharField(db_column='OsType', max_length=50)  # Field name made lowercase.
    productlineid = models.CharField(db_column='ProductLineID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=255)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblVmwareProductInfo'


class Tblvmwarevcenters(models.Model):
    vcenterid = models.AutoField(db_column='VcenterID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblVmwareVcenters'


class Tblvolume(models.Model):
    volumeid = models.AutoField(db_column='Volumeid', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    automount = models.BooleanField(db_column='Automount', blank=True, null=True)  # Field name made lowercase.
    blocksize = models.DecimalField(db_column='BlockSize', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    capacity = models.DecimalField(db_column='Capacity', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    compressed = models.BooleanField(db_column='Compressed', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    dirtybitset = models.BooleanField(db_column='DirtyBitSet', blank=True, null=True)  # Field name made lowercase.
    driveletter = models.CharField(db_column='DriveLetter', max_length=15, blank=True, null=True)  # Field name made lowercase.
    drivetype = models.DecimalField(db_column='DriveType', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    errorcleared = models.BooleanField(db_column='ErrorCleared', blank=True, null=True)  # Field name made lowercase.
    errordescription = models.CharField(db_column='ErrorDescription', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    errormethodology = models.CharField(db_column='ErrorMethodology', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    filesystem = models.CharField(db_column='FileSystem', max_length=50, blank=True, null=True)  # Field name made lowercase.
    freespace = models.DecimalField(db_column='FreeSpace', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    indexingenabled = models.BooleanField(db_column='IndexingEnabled', blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    pagefilepresent = models.BooleanField(db_column='PageFilePresent', blank=True, null=True)  # Field name made lowercase.
    supportsdiskquotas = models.BooleanField(db_column='SupportsDiskQuotas', blank=True, null=True)  # Field name made lowercase.
    supportsfilebasedcompression = models.BooleanField(db_column='SupportsFileBasedCompression', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblVolume'


class Tblvproamt(models.Model):
    vproamdid = models.AutoField(db_column='VproAmdID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.
    defaultttl = models.CharField(db_column='DefaultTTL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    https = models.BooleanField(db_column='HTTPS', blank=True, null=True)  # Field name made lowercase.
    httpversion = models.CharField(db_column='HTTPVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rmcppingversion = models.CharField(db_column='RMCPPingVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rmcppingstatus = models.CharField(db_column='RMCPPingStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblVproAMT'


class Tblwarranty(models.Model):
    warrantyid = models.AutoField(db_column='WarrantyId', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    lastwarrantytry = models.DateTimeField(db_column='LastWarrantyTry')  # Field name made lowercase.
    lastwarrantysuccess = models.DateTimeField(db_column='LastWarrantySuccess', blank=True, null=True)  # Field name made lowercase.
    purchasecountry = models.CharField(db_column='PurchaseCountry', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shipdate = models.DateTimeField(db_column='ShipDate', blank=True, null=True)  # Field name made lowercase.
    forceupdate = models.BooleanField(db_column='ForceUpdate')  # Field name made lowercase.
    error = models.CharField(db_column='Error', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblWarranty'


class Tblwarrantydetails(models.Model):
    warrantydetailsid = models.AutoField(db_column='WarrantyDetailsId', primary_key=True)  # Field name made lowercase.
    warrantyid = models.ForeignKey(Tblwarranty, models.DO_NOTHING, db_column='WarrantyId', blank=True, null=True)  # Field name made lowercase.
    warrantystartdate = models.DateTimeField(db_column='WarrantyStartDate', blank=True, null=True)  # Field name made lowercase.
    warrantyenddate = models.DateTimeField(db_column='WarrantyEndDate')  # Field name made lowercase.
    servicetype = models.CharField(db_column='ServiceType', max_length=1024)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblWarrantyDetails'


class Tblwinsat(models.Model):
    winsatid = models.AutoField(db_column='WinSatId', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.
    cpuscore = models.DecimalField(db_column='CPUScore', max_digits=4, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    d3dscore = models.DecimalField(db_column='D3DScore', max_digits=4, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    diskscore = models.DecimalField(db_column='DiskScore', max_digits=4, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    graphicsscore = models.DecimalField(db_column='GraphicsScore', max_digits=4, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    memoryscore = models.DecimalField(db_column='MemoryScore', max_digits=4, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    winsprlevel = models.DecimalField(db_column='WinSPRLevel', max_digits=4, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    winsatassessmentstate = models.SmallIntegerField(db_column='WinSATAssessmentState', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblWinSAT'


class Tblwindowscluster(models.Model):
    windowsclusterid = models.AutoField(db_column='WindowsClusterId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    fqdn = models.CharField(db_column='Fqdn', unique=True, max_length=255)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IpAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblWindowsCluster'


class Tblwindowsclusterlog(models.Model):
    windowsclusterlogid = models.AutoField(db_column='WindowsClusterLogId', primary_key=True)  # Field name made lowercase.
    windowsclusterid = models.ForeignKey(Tblwindowscluster, models.DO_NOTHING, db_column='WindowsClusterId')  # Field name made lowercase.
    windowsclusternodescannedid = models.ForeignKey('Tblwindowsclusternode', models.DO_NOTHING, db_column='WindowsClusterNodeScannedId', blank=True, null=True)  # Field name made lowercase.
    windowsclusternodesourceid = models.ForeignKey('Tblwindowsclusternode', models.DO_NOTHING, db_column='WindowsClusterNodeSourceId', blank=True, null=True)  # Field name made lowercase.
    windowsclusternodedestinationid = models.ForeignKey('Tblwindowsclusternode', models.DO_NOTHING, db_column='WindowsClusterNodeDestinationId', blank=True, null=True)  # Field name made lowercase.
    hypervguestid = models.ForeignKey(Tblhypervguest, models.DO_NOTHING, db_column='HyperVGuestId', blank=True, null=True)  # Field name made lowercase.
    action = models.IntegerField(db_column='Action', blank=True, null=True)  # Field name made lowercase.
    eventtimecreated = models.DateTimeField(db_column='EventTimeCreated')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EventId')  # Field name made lowercase.
    eventlevelid = models.IntegerField(db_column='EventLevelId')  # Field name made lowercase.
    eventmessageid = models.ForeignKey(Tblntlogmessage, models.DO_NOTHING, db_column='EventMessageId')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblWindowsClusterLog'


class Tblwindowsclusternode(models.Model):
    windowsclusternodeid = models.AutoField(db_column='WindowsClusterNodeId', primary_key=True)  # Field name made lowercase.
    windowsclusterid = models.ForeignKey(Tblwindowscluster, models.DO_NOTHING, db_column='WindowsClusterId')  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    assetname = models.CharField(db_column='AssetName', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblWindowsClusterNode'


class Tsysasdomains(models.Model):
    asdomainid = models.AutoField(db_column='AsDomainId', primary_key=True)  # Field name made lowercase.
    servername = models.ForeignKey('Tsysasservers', models.DO_NOTHING, db_column='Servername')  # Field name made lowercase.
    domainname = models.CharField(db_column='Domainname', max_length=380)  # Field name made lowercase.
    netbiosname = models.CharField(db_column='Netbiosname', max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    scannow = models.BooleanField(db_column='ScanNow')  # Field name made lowercase.
    lastscanned = models.DateTimeField(db_column='LastScanned', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    errortext = models.CharField(db_column='ErrorText', max_length=250, blank=True, null=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.
    intervalinseconds = models.IntegerField(db_column='IntervalInSeconds')  # Field name made lowercase.
    minrescantimeinseconds = models.IntegerField(db_column='MinRescanTimeInSeconds')  # Field name made lowercase.
    maxrescantimeinseconds = models.IntegerField(db_column='MaxRescanTimeInSeconds')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysASDomains'
        unique_together = (('servername', 'domainname'),)


class Tsysasou(models.Model):
    asouid = models.AutoField(db_column='AsOuId', primary_key=True)  # Field name made lowercase.
    asdomainid = models.ForeignKey(Tsysasdomains, models.DO_NOTHING, db_column='AsDomainId')  # Field name made lowercase.
    ou = models.CharField(db_column='OU', max_length=380)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysASOU'
        unique_together = (('asdomainid', 'ou'),)


class Tsysasservers(models.Model):
    servername = models.CharField(db_column='Servername', primary_key=True, max_length=60)  # Field name made lowercase.
    servicestarted = models.DateTimeField(db_column='Servicestarted', blank=True, null=True)  # Field name made lowercase.
    servicelastpolled = models.DateTimeField(db_column='Servicelastpolled', blank=True, null=True)  # Field name made lowercase.
    computerscanned = models.DecimalField(db_column='Computerscanned', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    activescanning = models.BooleanField()
    workgroupscanning = models.BooleanField(blank=True, null=True)
    version = models.CharField(db_column='Version', max_length=50, blank=True, null=True)  # Field name made lowercase.
    listenport = models.DecimalField(db_column='Listenport', max_digits=18, decimal_places=0)  # Field name made lowercase.
    concurrentthreads = models.DecimalField(db_column='ConcurrentThreads', max_digits=18, decimal_places=0)  # Field name made lowercase.
    ipscanthreads = models.DecimalField(db_column='IPscanThreads', max_digits=18, decimal_places=0)  # Field name made lowercase.
    rmadcomp = models.BooleanField(db_column='RMADCOMP')  # Field name made lowercase.
    naadcomp = models.BooleanField(db_column='NAADCOMP')  # Field name made lowercase.
    rmaduser = models.BooleanField(db_column='RMADUSER')  # Field name made lowercase.
    makeactive = models.BooleanField(db_column='MAKEACTIVE')  # Field name made lowercase.
    delhist = models.BooleanField(db_column='DELHIST')  # Field name made lowercase.
    delhistdays = models.DecimalField(db_column='DELHISTDAYS', max_digits=18, decimal_places=0)  # Field name made lowercase.
    delcomp = models.BooleanField(db_column='DELCOMP')  # Field name made lowercase.
    delcompdays = models.DecimalField(db_column='DELCOMPDAYS', max_digits=18, decimal_places=0)  # Field name made lowercase.
    nacomp = models.BooleanField(db_column='NACOMP')  # Field name made lowercase.
    nacompdays = models.DecimalField(db_column='NACOMPDAYS', max_digits=18, decimal_places=0)  # Field name made lowercase.
    deleventdays = models.DecimalField(db_column='DELEVENTDAYS', max_digits=18, decimal_places=0)  # Field name made lowercase.
    delsyslogdays = models.DecimalField(db_column='DELSYSLOGDAYS', max_digits=18, decimal_places=0)  # Field name made lowercase.
    refradcomp = models.BooleanField(db_column='REFRADCOMP')  # Field name made lowercase.
    refradusers = models.BooleanField(db_column='REFRADUSERS')  # Field name made lowercase.
    smtpserver = models.CharField(db_column='SMTPserver', max_length=250, blank=True, null=True)  # Field name made lowercase.
    smtpport = models.DecimalField(db_column='SMTPport', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    smtpfrom = models.CharField(db_column='SMTPFROM', max_length=250, blank=True, null=True)  # Field name made lowercase.
    smtpfromdisplay = models.CharField(db_column='SMTPFROMDISPLAY', max_length=250, blank=True, null=True)  # Field name made lowercase.
    smtpauthenticate = models.BooleanField(db_column='SMTPAuthenticate', blank=True, null=True)  # Field name made lowercase.
    smtpusername = models.CharField(db_column='SMTPUsername', max_length=255, blank=True, null=True)  # Field name made lowercase.
    smtppassword = models.CharField(db_column='SMTPPassword', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    sendalertreports = models.BooleanField(db_column='SendAlertreports')  # Field name made lowercase.
    sendeventalerts = models.BooleanField(db_column='SendEventAlerts')  # Field name made lowercase.
    mailnow = models.BooleanField(db_column='Mailnow')  # Field name made lowercase.
    ipscannow = models.BooleanField(db_column='IPscannow')  # Field name made lowercase.
    day1rep = models.BooleanField(db_column='Day1rep')  # Field name made lowercase.
    day2rep = models.BooleanField(db_column='Day2rep')  # Field name made lowercase.
    day3rep = models.BooleanField(db_column='Day3rep')  # Field name made lowercase.
    day4rep = models.BooleanField(db_column='Day4rep')  # Field name made lowercase.
    day5rep = models.BooleanField(db_column='Day5rep')  # Field name made lowercase.
    day6rep = models.BooleanField(db_column='Day6rep')  # Field name made lowercase.
    day7rep = models.BooleanField(db_column='Day7rep')  # Field name made lowercase.
    day1timerep = models.DateTimeField(db_column='Day1timerep')  # Field name made lowercase.
    day2timerep = models.DateTimeField(db_column='Day2timerep')  # Field name made lowercase.
    day3timerep = models.DateTimeField(db_column='Day3timerep')  # Field name made lowercase.
    day4timerep = models.DateTimeField(db_column='Day4timerep')  # Field name made lowercase.
    day5timerep = models.DateTimeField(db_column='Day5timerep')  # Field name made lowercase.
    day6timerep = models.DateTimeField(db_column='Day6timerep')  # Field name made lowercase.
    day7timerep = models.DateTimeField(db_column='Day7timerep')  # Field name made lowercase.
    lastmailed = models.DateTimeField(db_column='Lastmailed', blank=True, null=True)  # Field name made lowercase.
    rmdiuser = models.BooleanField(db_column='RMDIUSER')  # Field name made lowercase.
    rmdicomp = models.BooleanField(db_column='RMDICOMP')  # Field name made lowercase.
    nadicomp = models.BooleanField(db_column='NADICOMP')  # Field name made lowercase.
    scanuser = models.CharField(db_column='Scanuser', max_length=300, blank=True, null=True)  # Field name made lowercase.
    evinfo = models.BooleanField(db_column='EVinfo')  # Field name made lowercase.
    evsuccess = models.BooleanField(db_column='EVsuccess')  # Field name made lowercase.
    evuptime = models.BooleanField(db_column='EVUptime')  # Field name made lowercase.
    deluptimedays = models.IntegerField(db_column='DELUptimeDays')  # Field name made lowercase.
    evwarning = models.BooleanField(db_column='EVwarning')  # Field name made lowercase.
    evfailure = models.BooleanField(db_column='EVfailure')  # Field name made lowercase.
    dellogoninfo = models.IntegerField(db_column='DELLOGONINFO')  # Field name made lowercase.
    isdomain = models.BooleanField(db_column='IsDomain')  # Field name made lowercase.
    domainname = models.CharField(db_column='DomainName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dnsname = models.CharField(db_column='DNSName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    startip = models.CharField(db_column='StartIP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endip = models.CharField(db_column='EndIP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smtpusessl = models.BooleanField(db_column='SMTPUseSSL')  # Field name made lowercase.
    saddcomp = models.BooleanField(db_column='SADDCOMP')  # Field name made lowercase.
    sadduser = models.BooleanField(db_column='SADDUSER')  # Field name made lowercase.
    enableproxy = models.BooleanField(db_column='enableProxy')  # Field name made lowercase.
    proxyname = models.CharField(db_column='proxyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    proxyport = models.IntegerField(db_column='proxyPort', blank=True, null=True)  # Field name made lowercase.
    enableproxyauth = models.BooleanField(db_column='enableProxyAuth')  # Field name made lowercase.
    proxylogin = models.CharField(db_column='proxyLogin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    proxypassword = models.CharField(db_column='proxyPassword', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    proxydomain = models.CharField(db_column='proxyDomain', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enablewarrantyscanning = models.BooleanField(db_column='enableWarrantyScanning')  # Field name made lowercase.
    currentuser = models.CharField(db_column='CurrentUser', max_length=500)  # Field name made lowercase.
    assetgroupsscannow = models.BooleanField(db_column='AssetGroupsScannow', blank=True, null=True)  # Field name made lowercase.
    renamedcomputerdetection = models.BooleanField(db_column='renamedComputerDetection')  # Field name made lowercase.
    lastactivescan = models.DateTimeField(db_column='LastActiveScan')  # Field name made lowercase.
    maxdeploymentthreads = models.IntegerField(db_column='MaxDeploymentThreads', blank=True, null=True)  # Field name made lowercase.
    deldeploymentlogdays = models.DecimalField(db_column='DELDEPLOYMENTLOGDAYS', max_digits=18, decimal_places=0)  # Field name made lowercase.
    scanhistorydays = models.IntegerField(db_column='ScanHistoryDays')  # Field name made lowercase.
    activescanningmaxrescantime = models.IntegerField(db_column='ActiveScanningMaxRescanTime')  # Field name made lowercase.
    activescanningminrescantime = models.IntegerField(db_column='ActiveScanningMinRescanTime')  # Field name made lowercase.
    activescanninginterval = models.IntegerField(db_column='ActiveScanningInterval')  # Field name made lowercase.
    clearqueue = models.BooleanField(db_column='ClearQueue')  # Field name made lowercase.
    mailserver = models.BooleanField()
    proxypasswordkeyhash = models.IntegerField(db_column='ProxyPasswordKeyHash', blank=True, null=True)  # Field name made lowercase.
    encryptionkeyhash = models.IntegerField(db_column='EncryptionKeyHash', blank=True, null=True)  # Field name made lowercase.
    delconfigurationlogdays = models.IntegerField(db_column='Delconfigurationlogdays')  # Field name made lowercase.
    delloginlogdays = models.IntegerField(db_column='Delloginlogdays')  # Field name made lowercase.
    proxytimeout = models.IntegerField(db_column='ProxyTimeout')  # Field name made lowercase.
    dofallbackscanning = models.BooleanField(db_column='DoFallbackScanning')  # Field name made lowercase.
    delperformancecounterdays = models.IntegerField(db_column='DelPerformanceCounterDays')  # Field name made lowercase.
    is64bit = models.BooleanField(db_column='Is64bit', blank=True, null=True)  # Field name made lowercase.
    isperformancecountertargetcreated = models.BooleanField(db_column='IsPerformanceCounterTargetCreated')  # Field name made lowercase.
    delwindowsclusterlogsdays = models.IntegerField(db_column='DelWindowsClusterLogsDays')  # Field name made lowercase.
    delhypervlogsdays = models.IntegerField(db_column='DelHyperVLogsDays')  # Field name made lowercase.
    delsccmdatadays = models.IntegerField(db_column='DelSccmDataDays')  # Field name made lowercase.
    delsccmcomp = models.BooleanField(db_column='DELSCCMCOMP')  # Field name made lowercase.
    scanlastlogon = models.BooleanField(db_column='ScanLastLogon')  # Field name made lowercase.
    isassetradarcompatible = models.BooleanField(db_column='IsAssetRadarCompatible')  # Field name made lowercase.
    assetradarcompatiblelastscanned = models.DateTimeField(db_column='AssetRadarCompatibleLastScanned', blank=True, null=True)  # Field name made lowercase.
    checkassetradarcompatibilitynow = models.BooleanField(db_column='CheckAssetRadarCompatibilityNow')  # Field name made lowercase.
    installassetradardrivernow = models.BooleanField(db_column='InstallAssetRadarDriverNow')  # Field name made lowercase.
    delassetradarcomp = models.BooleanField(db_column='DelAssetRadarComp')  # Field name made lowercase.
    delassetradarcompunknownonly = models.BooleanField(db_column='DelAssetRadarCompUnknownOnly')  # Field name made lowercase.
    delassetradardays = models.IntegerField(db_column='DelAssetRadarDays')  # Field name made lowercase.
    delassetradarlogcomp = models.BooleanField(db_column='DelAssetRadarLogComp')  # Field name made lowercase.
    delassetradarlogdays = models.IntegerField(db_column='DelAssetRadarLogDays')  # Field name made lowercase.
    nonactiveassetradarcomp = models.BooleanField(db_column='NonActiveAssetRadarComp')  # Field name made lowercase.
    nonactiveassetradarcompdays = models.IntegerField(db_column='NonActiveAssetRadarCompDays')  # Field name made lowercase.
    nonactiveassetradarcompunknownonly = models.BooleanField(db_column='NonActiveAssetRadarCompUnknownOnly')  # Field name made lowercase.
    nonactiveassetradarcompunknownonlydays = models.IntegerField(db_column='NonActiveAssetRadarCompUnknownOnlyDays')  # Field name made lowercase.
    delassetradarcompunknownonlydays = models.IntegerField(db_column='DelAssetRadarCompUnknownOnlyDays')  # Field name made lowercase.
    isassetradarenabled = models.IntegerField(db_column='IsAssetRadarEnabled')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.
    enableassetrecognition = models.BooleanField(db_column='EnableAssetRecognition', blank=True, null=True)  # Field name made lowercase.
    availableupdateinstallationtimeframestart = models.DateTimeField(db_column='AvailableUpdateInstallationTimeFrameStart', blank=True, null=True)  # Field name made lowercase.
    availableupdateinstallationtimeframeend = models.DateTimeField(db_column='AvailableUpdateInstallationTimeFrameEnd', blank=True, null=True)  # Field name made lowercase.
    isautoupdatefetcher = models.BooleanField(db_column='IsAutoUpdateFetcher')  # Field name made lowercase.
    autoupdatetype = models.IntegerField(db_column='AutoUpdateType')  # Field name made lowercase.
    isautoupdatetriggeredbyuser = models.BooleanField(db_column='IsAutoUpdateTriggeredByUser')  # Field name made lowercase.
    isautoupdateinstalling = models.BooleanField(db_column='IsAutoUpdateInstalling')  # Field name made lowercase.
    lasttimecheckedforupdates = models.DateTimeField(db_column='LastTimeCheckedForUpdates', blank=True, null=True)  # Field name made lowercase.
    ischeckforupdatestriggeredbyuser = models.BooleanField(db_column='IsCheckForUpdatesTriggeredByUser')  # Field name made lowercase.
    triggerautoupdatejobs = models.BooleanField(db_column='TriggerAutoUpdateJobs')  # Field name made lowercase.
    isfetchercheckingforupdates = models.BooleanField(db_column='IsFetcherCheckingForUpdates')  # Field name made lowercase.
    autoupdatefeedbackmessage = models.CharField(db_column='AutoUpdateFeedbackMessage', max_length=500, blank=True, null=True)  # Field name made lowercase.
    renamedcomputerdetectionwithoutmac = models.BooleanField(db_column='RenamedComputerDetectionWithoutMac', blank=True, null=True)  # Field name made lowercase.
    numberofdevicestosetinterfaceasuplink = models.IntegerField(db_column='NumberOfDevicesToSetInterfaceAsUplink', blank=True, null=True)  # Field name made lowercase.
    scandisabledazureaddevices = models.BooleanField(db_column='ScanDisabledAzureAdDevices')  # Field name made lowercase.
    removedisabledazureaddevices = models.BooleanField(db_column='RemoveDisabledAzureAdDevices')  # Field name made lowercase.
    setdisabledazureaddevicestononactive = models.BooleanField(db_column='SetDisabledAzureAdDevicesToNonActive')  # Field name made lowercase.
    removenotfoundazureaddevices = models.BooleanField(db_column='RemoveNotFoundAzureAdDevices')  # Field name made lowercase.
    setnotfoundazureaddevicestononactive = models.BooleanField(db_column='SetNotFoundAzureAdDevicesToNonActive')  # Field name made lowercase.
    refreshazureaddevicedetails = models.BooleanField(db_column='RefreshAzureAdDeviceDetails')  # Field name made lowercase.
    refreshazureaduserdetails = models.BooleanField(db_column='RefreshAzureAdUserDetails')  # Field name made lowercase.
    removenotfoundazureadusers = models.BooleanField(db_column='RemoveNotFoundAzureAdUsers')  # Field name made lowercase.
    removedisabledazureadusers = models.BooleanField(db_column='RemoveDisabledAzureAdUsers')  # Field name made lowercase.
    scandisabledazureadusers = models.BooleanField(db_column='ScanDisabledAzureAdUsers')  # Field name made lowercase.
    mergeazureaddevice = models.BooleanField(db_column='MergeAzureAdDevice')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysASServers'


class Tsysassites(models.Model):
    assiteid = models.AutoField(db_column='AsSiteId', primary_key=True)  # Field name made lowercase.
    asdomainid = models.ForeignKey(Tsysasdomains, models.DO_NOTHING, db_column='AsDomainId')  # Field name made lowercase.
    sitename = models.CharField(db_column='SiteName', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysASSites'
        unique_together = (('asdomainid', 'sitename'),)


class Tsysasworkgroups(models.Model):
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='Servername')  # Field name made lowercase.
    workgroup = models.CharField(db_column='Workgroup', max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    scannow = models.BooleanField(db_column='ScanNow')  # Field name made lowercase.
    lastscanned = models.DateTimeField(db_column='LastScanned', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    errortext = models.CharField(db_column='ErrorText', max_length=250, blank=True, null=True)  # Field name made lowercase.
    asworkgroupsid = models.AutoField(db_column='ASWorkgroupsId', primary_key=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysASWorkgroups'


class Tsysawsregion(models.Model):
    regionid = models.AutoField(db_column='RegionId', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    icon = models.CharField(db_column='Icon', max_length=50)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAWSRegion'


class Tsysawsscanningregion(models.Model):
    scanningregionid = models.AutoField(db_column='ScanningRegionId', primary_key=True)  # Field name made lowercase.
    regionid = models.ForeignKey(Tsysawsregion, models.DO_NOTHING, db_column='RegionId')  # Field name made lowercase.
    scheduleid = models.ForeignKey('Tsysscanschedule', models.DO_NOTHING, db_column='ScheduleId')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    lastscanned = models.DateTimeField(db_column='Lastscanned', blank=True, null=True)  # Field name made lowercase.
    scannow = models.BooleanField(db_column='ScanNow')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    errortext = models.CharField(db_column='ErrorText', max_length=500, blank=True, null=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='Servername')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAWSScanningRegion'


class Tsysawsscanningregioncredential(models.Model):
    scanningregioncredentialid = models.AutoField(db_column='ScanningRegionCredentialId', primary_key=True)  # Field name made lowercase.
    scanningregionid = models.ForeignKey(Tsysawsscanningregion, models.DO_NOTHING, db_column='ScanningRegionId')  # Field name made lowercase.
    credid = models.ForeignKey('Tsyscredentials', models.DO_NOTHING, db_column='CredId')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAWSScanningRegionCredential'


class Tsysadgrouptype(models.Model):
    grouptype = models.IntegerField(db_column='GroupType', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAdGroupType'


class Tsysadpropertytype(models.Model):
    typeid = models.IntegerField(db_column='TypeId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    maxsize = models.IntegerField(db_column='MaxSize')  # Field name made lowercase.
    appliesto = models.CharField(db_column='AppliesTo', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAdPropertyType'


class Tsysadsischedule(models.Model):
    scheduleid = models.AutoField(db_column='ScheduleID', primary_key=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='Servername')  # Field name made lowercase.
    scantype = models.IntegerField(db_column='Scantype')  # Field name made lowercase.
    scantarget = models.CharField(db_column='Scantarget', max_length=1024)  # Field name made lowercase.
    netbiosdomain = models.CharField(db_column='Netbiosdomain', max_length=150)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    scannow = models.BooleanField(db_column='ScanNow')  # Field name made lowercase.
    day1 = models.BooleanField(db_column='Day1')  # Field name made lowercase.
    day2 = models.BooleanField(db_column='Day2')  # Field name made lowercase.
    day3 = models.BooleanField(db_column='Day3')  # Field name made lowercase.
    day4 = models.BooleanField(db_column='Day4')  # Field name made lowercase.
    day5 = models.BooleanField(db_column='Day5')  # Field name made lowercase.
    day6 = models.BooleanField(db_column='Day6')  # Field name made lowercase.
    day7 = models.BooleanField(db_column='Day7')  # Field name made lowercase.
    day1time = models.DateTimeField(db_column='Day1time')  # Field name made lowercase.
    day2time = models.DateTimeField(db_column='Day2time')  # Field name made lowercase.
    day3time = models.DateTimeField(db_column='Day3time')  # Field name made lowercase.
    day4time = models.DateTimeField(db_column='Day4time')  # Field name made lowercase.
    day5time = models.DateTimeField(db_column='Day5time')  # Field name made lowercase.
    day6time = models.DateTimeField(db_column='Day6time')  # Field name made lowercase.
    day7time = models.DateTimeField(db_column='Day7time')  # Field name made lowercase.
    lastscanned = models.DateTimeField(db_column='LastScanned', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    errortext = models.CharField(db_column='ErrorText', max_length=250, blank=True, null=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAdsischedule'


class Tsysairwatchscanningtarget(models.Model):
    scanningtargetid = models.AutoField(db_column='ScanningTargetId', primary_key=True)  # Field name made lowercase.
    scheduleid = models.ForeignKey('Tsysscanschedule', models.DO_NOTHING, db_column='ScheduleId')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    lastscanned = models.DateTimeField(db_column='Lastscanned', blank=True, null=True)  # Field name made lowercase.
    scannow = models.BooleanField(db_column='ScanNow')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    errortext = models.CharField(db_column='ErrorText', max_length=500, blank=True, null=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='Servername')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAirWatchScanningTarget'


class Tsysairwatchscanningtargetcredential(models.Model):
    scanningtargetcredentialid = models.AutoField(db_column='ScanningTargetCredentialId', primary_key=True)  # Field name made lowercase.
    scanningtargetid = models.ForeignKey(Tsysairwatchscanningtarget, models.DO_NOTHING, db_column='ScanningTargetId')  # Field name made lowercase.
    credid = models.ForeignKey('Tsyscredentials', models.DO_NOTHING, db_column='CredId')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAirWatchScanningTargetCredential'


class Tsysalertschedule(models.Model):
    alertscheduleid = models.AutoField(db_column='AlertScheduleId', primary_key=True)  # Field name made lowercase.
    alertid = models.CharField(db_column='AlertId', max_length=150)  # Field name made lowercase.
    scheduleid = models.ForeignKey('Tsysschedule', models.DO_NOTHING, db_column='ScheduleId')  # Field name made lowercase.
    lastrun = models.DateTimeField(db_column='LastRun', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAlertSchedule'


class Tsysandroidos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    linuxkernelversion = models.CharField(db_column='LinuxKernelVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAndroidOs'


class Tsysapikeys(models.Model):
    keyid = models.AutoField(primary_key=True)
    key = models.CharField(max_length=200)
    description = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tsysApiKeys'


class Tsysasserverautoupdate(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoupdateid = models.ForeignKey('Tsysautoupdate', models.DO_NOTHING, db_column='AutoUpdateId')  # Field name made lowercase.
    scanserver = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='ScanServer')  # Field name made lowercase.
    installationdate = models.DateTimeField(db_column='InstallationDate')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAsServerAutoUpdate'
        unique_together = (('autoupdateid', 'scanserver'),)


class Tsysassetchangesource(models.Model):
    sourceid = models.IntegerField(db_column='SourceId', primary_key=True)  # Field name made lowercase.
    sourcename = models.CharField(db_column='SourceName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAssetChangeSource'


class Tsysassetexclusionreason(models.Model):
    assetexclusionreasonid = models.AutoField(db_column='AssetExclusionReasonId', primary_key=True)  # Field name made lowercase.
    assetexclusionreasontext = models.CharField(db_column='AssetExclusionReasonText', max_length=4000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAssetExclusionReason'


class Tsysassetfield(models.Model):
    fieldid = models.IntegerField(db_column='FieldId', primary_key=True)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAssetField'


class Tsysassetgroupfilter(models.Model):
    filterid = models.AutoField(db_column='FilterID', primary_key=True)  # Field name made lowercase.
    assetgroupid = models.ForeignKey(Tblassetgroups, models.DO_NOTHING, db_column='AssetGroupID')  # Field name made lowercase.
    compare = models.IntegerField(db_column='Compare')  # Field name made lowercase.
    operator = models.IntegerField(db_column='Operator')  # Field name made lowercase.
    comparevalue = models.CharField(db_column='Comparevalue', max_length=2000)  # Field name made lowercase.
    versioncomparevalue = models.CharField(db_column='VersionCompareValue', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAssetGroupFilter'


class Tsysassetgroupscan(models.Model):
    assetgroupscanid = models.AutoField(db_column='AssetGroupScanID', primary_key=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='Servername')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    assetgroupid = models.ForeignKey(Tblassetgroups, models.DO_NOTHING, db_column='AssetGroupID', blank=True, null=True)  # Field name made lowercase.
    assettype = models.IntegerField(db_column='AssetType', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled', blank=True, null=True)  # Field name made lowercase.
    day1 = models.BooleanField(db_column='Day1', blank=True, null=True)  # Field name made lowercase.
    day2 = models.BooleanField(db_column='Day2', blank=True, null=True)  # Field name made lowercase.
    day3 = models.BooleanField(db_column='Day3', blank=True, null=True)  # Field name made lowercase.
    day4 = models.BooleanField(db_column='Day4', blank=True, null=True)  # Field name made lowercase.
    day5 = models.BooleanField(db_column='Day5', blank=True, null=True)  # Field name made lowercase.
    day6 = models.BooleanField(db_column='Day6', blank=True, null=True)  # Field name made lowercase.
    day7 = models.BooleanField(db_column='Day7', blank=True, null=True)  # Field name made lowercase.
    day1time = models.DateTimeField(db_column='Day1time', blank=True, null=True)  # Field name made lowercase.
    day2time = models.DateTimeField(db_column='Day2time', blank=True, null=True)  # Field name made lowercase.
    day3time = models.DateTimeField(db_column='Day3time', blank=True, null=True)  # Field name made lowercase.
    day4time = models.DateTimeField(db_column='Day4time', blank=True, null=True)  # Field name made lowercase.
    day5time = models.DateTimeField(db_column='Day5time', blank=True, null=True)  # Field name made lowercase.
    day6time = models.DateTimeField(db_column='Day6time', blank=True, null=True)  # Field name made lowercase.
    day7time = models.DateTimeField(db_column='Day7time', blank=True, null=True)  # Field name made lowercase.
    lastassettypescan = models.DateTimeField(db_column='LastAssetTypescan', blank=True, null=True)  # Field name made lowercase.
    dns = models.BooleanField(db_column='DNS', blank=True, null=True)  # Field name made lowercase.
    recurring = models.BooleanField(db_column='Recurring', blank=True, null=True)  # Field name made lowercase.
    minutes = models.BooleanField(db_column='Minutes', blank=True, null=True)  # Field name made lowercase.
    waittime = models.IntegerField(db_column='Waittime', blank=True, null=True)  # Field name made lowercase.
    scannow = models.BooleanField(db_column='ScanNow')  # Field name made lowercase.
    report = models.ForeignKey('Tsysreports', models.DO_NOTHING, db_column='Report', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAssetGroupScan'


class Tsysassetrelationtypes(models.Model):
    relationtypeid = models.IntegerField(db_column='RelationTypeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    standard = models.BooleanField(db_column='Standard', blank=True, null=True)  # Field name made lowercase.
    relationtypeicon10 = models.CharField(db_column='RelationTypeIcon10', max_length=250, blank=True, null=True)  # Field name made lowercase.
    relationtypeicon16 = models.CharField(db_column='RelationTypeIcon16', max_length=250, blank=True, null=True)  # Field name made lowercase.
    relationtypeicon48 = models.CharField(db_column='RelationTypeIcon48', max_length=250, blank=True, null=True)  # Field name made lowercase.
    reversename = models.CharField(db_column='ReverseName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAssetRelationTypes'


class Tsysassettypeexclude(models.Model):
    assettypeexclusionid = models.AutoField(db_column='AssetTypeExclusionID', primary_key=True)  # Field name made lowercase.
    assettype = models.ForeignKey('Tsysassettypes', models.DO_NOTHING, db_column='AssetType')  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='ServerName')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=150, blank=True, null=True)  # Field name made lowercase.
    assetexclusionreasonid = models.ForeignKey(Tsysassetexclusionreason, models.DO_NOTHING, db_column='AssetExclusionReasonId', blank=True, null=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAssetTypeExclude'


class Tsysassettypes(models.Model):
    assettype = models.IntegerField(db_column='AssetType', primary_key=True)  # Field name made lowercase.
    assettypename = models.CharField(db_column='AssetTypename', max_length=100)  # Field name made lowercase.
    assettypeicon10 = models.CharField(db_column='AssetTypeIcon10', max_length=250, blank=True, null=True)  # Field name made lowercase.
    assettypeicon16 = models.CharField(db_column='AssetTypeIcon16', max_length=250, blank=True, null=True)  # Field name made lowercase.
    assettypeicon48 = models.CharField(db_column='AssetTypeIcon48', max_length=250, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAssetTypes'


class Tsysautoupdate(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', unique=True, max_length=20)  # Field name made lowercase.
    severity = models.IntegerField(db_column='Severity')  # Field name made lowercase.
    zipfile = models.BinaryField(db_column='ZipFile', blank=True, null=True)  # Field name made lowercase.
    isvalid = models.BooleanField(db_column='IsValid')  # Field name made lowercase.
    spacerequiredmb = models.IntegerField(db_column='SpaceRequiredMb')  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    ismanualinstallationrequired = models.BooleanField(db_column='IsManualInstallationRequired')  # Field name made lowercase.
    filehash = models.CharField(db_column='FileHash', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAutoUpdate'


class Tsysautoupdateerrors(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=20)  # Field name made lowercase.
    previousversion = models.CharField(db_column='PreviousVersion', max_length=20)  # Field name made lowercase.
    errormessage = models.TextField(db_column='ErrorMessage')  # Field name made lowercase.
    issenttoapi = models.BooleanField(db_column='IsSentToApi')  # Field name made lowercase.
    dateoccurred = models.DateTimeField(db_column='DateOccurred')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAutoUpdateErrors'


class Tsysautoupdatehistory(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=20)  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    scanserver = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='ScanServer')  # Field name made lowercase.
    installationdate = models.DateTimeField(db_column='InstallationDate')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    previousversion = models.CharField(db_column='PreviousVersion', max_length=20, blank=True, null=True)  # Field name made lowercase.
    osbuildnumber = models.CharField(db_column='OsBuildNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    installationfeedbackmessage = models.TextField(db_column='InstallationFeedbackMessage', blank=True, null=True)  # Field name made lowercase.
    issenttoapi = models.BooleanField(db_column='IsSentToApi')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAutoUpdateHistory'


class Tsysazureadscanningtarget(models.Model):
    scanningtargetid = models.AutoField(db_column='ScanningTargetId', primary_key=True)  # Field name made lowercase.
    scheduleid = models.ForeignKey('Tsysscanschedule', models.DO_NOTHING, db_column='ScheduleId')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    lastscanned = models.DateTimeField(db_column='Lastscanned', blank=True, null=True)  # Field name made lowercase.
    scannow = models.BooleanField(db_column='ScanNow')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    errortext = models.CharField(db_column='ErrorText', max_length=500, blank=True, null=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='Servername')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAzureAdScanningTarget'


class Tsysazureadscanningtargetcredential(models.Model):
    scanningtargetcredentialid = models.AutoField(db_column='ScanningTargetCredentialId', primary_key=True)  # Field name made lowercase.
    scanningtargetid = models.ForeignKey(Tsysazureadscanningtarget, models.DO_NOTHING, db_column='ScanningTargetId')  # Field name made lowercase.
    credid = models.ForeignKey('Tsyscredentials', models.DO_NOTHING, db_column='CredId')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAzureAdScanningTargetCredential'
        unique_together = (('scanningtargetid', 'credid'),)


class Tsysazurefilter(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    scanningtargetid = models.ForeignKey('Tsysazurescanningtarget', models.DO_NOTHING, db_column='ScanningTargetId')  # Field name made lowercase.
    filter = models.CharField(db_column='Filter', max_length=255)  # Field name made lowercase.
    filtertype = models.IntegerField(db_column='FilterType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAzureFilter'


class Tsysazurescanningtarget(models.Model):
    scanningtargetid = models.AutoField(db_column='ScanningTargetId', primary_key=True)  # Field name made lowercase.
    scheduleid = models.ForeignKey('Tsysscanschedule', models.DO_NOTHING, db_column='ScheduleId')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    lastscanned = models.DateTimeField(db_column='Lastscanned', blank=True, null=True)  # Field name made lowercase.
    scannow = models.BooleanField(db_column='ScanNow')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    errortext = models.CharField(db_column='ErrorText', max_length=500, blank=True, null=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='Servername')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAzureScanningTarget'


class Tsysazurescanningtargetcredential(models.Model):
    scanningtargetcredentialid = models.AutoField(db_column='ScanningTargetCredentialId', primary_key=True)  # Field name made lowercase.
    scanningtargetid = models.ForeignKey(Tsysazurescanningtarget, models.DO_NOTHING, db_column='ScanningTargetId')  # Field name made lowercase.
    credid = models.ForeignKey('Tsyscredentials', models.DO_NOTHING, db_column='CredId')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysAzureScanningTargetCredential'


class Tsyscertificatekeyusagetypes(models.Model):
    keyusagetypeid = models.IntegerField(db_column='KeyUsageTypeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysCertificateKeyUsageTypes'


class Tsyschromeosscanningtarget(models.Model):
    scanningtargetid = models.AutoField(db_column='ScanningTargetId', primary_key=True)  # Field name made lowercase.
    scheduleid = models.ForeignKey('Tsysscanschedule', models.DO_NOTHING, db_column='ScheduleId')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    lastscanned = models.DateTimeField(db_column='LastScanned', blank=True, null=True)  # Field name made lowercase.
    scannow = models.BooleanField(db_column='ScanNow')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    errortext = models.CharField(db_column='ErrorText', max_length=500, blank=True, null=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='ServerName')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysChromeOsScanningTarget'


class Tsyschromeosscanningtargetcredential(models.Model):
    scanningtargetcredentialid = models.AutoField(db_column='ScanningTargetCredentialId', primary_key=True)  # Field name made lowercase.
    scanningtargetid = models.ForeignKey(Tsyschromeosscanningtarget, models.DO_NOTHING, db_column='ScanningTargetId')  # Field name made lowercase.
    credid = models.ForeignKey('Tsyscredentials', models.DO_NOTHING, db_column='CredId')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysChromeOsScanningTargetCredential'


class Tsyscloudprerequisitescheck(models.Model):
    cloudprerequisitescheckid = models.AutoField(db_column='CloudPrerequisitesCheckId', primary_key=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='ServerName')  # Field name made lowercase.
    haswebsitetls1dot2 = models.IntegerField(db_column='HasWebsiteTls1Dot2')  # Field name made lowercase.
    haswebsiteinternetaccess = models.IntegerField(db_column='HasWebsiteInternetAccess')  # Field name made lowercase.
    hasservicetls1dot2 = models.IntegerField(db_column='HasServiceTls1Dot2')  # Field name made lowercase.
    hasserviceinternetaccess = models.IntegerField(db_column='HasServiceInternetAccess')  # Field name made lowercase.
    isserviceup = models.IntegerField(db_column='IsServiceUp')  # Field name made lowercase.
    hasminimumlansweeperversion = models.IntegerField(db_column='HasMinimumLansweeperVersion')  # Field name made lowercase.
    hasvalidlansweeperlicense = models.IntegerField(db_column='HasValidLansweeperLicense')  # Field name made lowercase.
    hascorrectdatabaserights = models.IntegerField(db_column='HasCorrectDatabaseRights')  # Field name made lowercase.
    hasenoughdiskspace = models.IntegerField(db_column='HasEnoughDiskSpace')  # Field name made lowercase.
    hasitassetdataplatformenoughcapacity = models.IntegerField(db_column='HasItAssetDataPlatformEnoughCapacity')  # Field name made lowercase.
    checkstarted = models.DateTimeField(db_column='CheckStarted')  # Field name made lowercase.
    minimumlansweeperversion = models.CharField(db_column='MinimumLansweeperVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isdatabasehostedonwindows = models.IntegerField(db_column='IsDatabaseHostedOnWindows')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysCloudPrerequisitesCheck'


class Tsyscloudstatus(models.Model):
    cloudstatusid = models.IntegerField(db_column='CloudStatusId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysCloudStatus'


class Tsyscredentials(models.Model):
    credid = models.AutoField(db_column='CredID', primary_key=True)  # Field name made lowercase.
    credname = models.CharField(db_column='Credname', unique=True, max_length=100)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=510, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=1000)  # Field name made lowercase.
    credtype = models.IntegerField(db_column='Credtype')  # Field name made lowercase.
    blank = models.BooleanField(db_column='Blank')  # Field name made lowercase.
    flags = models.SmallIntegerField(db_column='Flags')  # Field name made lowercase.
    password2 = models.CharField(db_column='Password2', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    globalkey = models.BooleanField(db_column='GlobalKey')  # Field name made lowercase.
    sshkey = models.TextField(db_column='SSHKey', blank=True, null=True)  # Field name made lowercase.
    keyhash = models.IntegerField(db_column='KeyHash', blank=True, null=True)  # Field name made lowercase.
    apiurl = models.CharField(db_column='ApiURL', max_length=150, blank=True, null=True)  # Field name made lowercase.
    azureapplicationid = models.CharField(db_column='AzureApplicationID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    intuneapplicationid = models.CharField(db_column='IntuneApplicationID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    jsonkey = models.TextField(db_column='JsonKey', blank=True, null=True)  # Field name made lowercase.
    apikey = models.TextField(db_column='ApiKey', blank=True, null=True)  # Field name made lowercase.
    sccmserver = models.CharField(db_column='SccmServer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    context = models.CharField(db_column='Context', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.
    keyhashvalid = models.BooleanField(db_column='KeyHashValid')  # Field name made lowercase.
    certificatethumbprint = models.CharField(db_column='CertificateThumbprint', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    credcomplete = models.BooleanField(db_column='CredComplete')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    sshsubtype = models.IntegerField(db_column='SshSubType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysCredentials'


class Tsyscurrentscans(models.Model):
    scanid = models.BigAutoField(db_column='ScanID', primary_key=True)  # Field name made lowercase.
    target = models.CharField(max_length=150)
    scanserver = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='Scanserver')  # Field name made lowercase.
    priority = models.BooleanField(db_column='Priority')  # Field name made lowercase.
    scantype = models.IntegerField(db_column='ScanType')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPaddress', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysCurrentScans'


class Tsyscustomfieldtypes(models.Model):
    typeid = models.IntegerField(primary_key=True)
    typename = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tsysCustomFieldTypes'


class Tsyscustomnames(models.Model):
    customname = models.CharField(db_column='Customname', primary_key=True, max_length=50)  # Field name made lowercase.
    displayname = models.CharField(db_column='Displayname', max_length=100)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    values = models.CharField(db_column='Values', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    info = models.CharField(db_column='Info', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysCustomNames'


class Tsysdbobjects(models.Model):
    dbobjname = models.CharField(db_column='DBobjName', primary_key=True, max_length=75)  # Field name made lowercase.
    query = models.TextField(db_column='Query', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=300, blank=True, null=True)  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    hdoverseeronly = models.BooleanField(db_column='HDOverseerOnly', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysDBobjects'


class Tsysdomaincontrollers(models.Model):
    domaincontrollerid = models.AutoField(db_column='DomainControllerID', primary_key=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='Servername')  # Field name made lowercase.
    domainnetbios = models.CharField(db_column='DomainNetbios', max_length=256)  # Field name made lowercase.
    domaincontrollerdns = models.CharField(db_column='DomainControllerDns', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysDomainControllers'
        unique_together = (('servername', 'domainnetbios'),)


class Tsysdomaincredentials(models.Model):
    domainname = models.CharField(db_column='DomainName', max_length=150)  # Field name made lowercase.
    credid = models.ForeignKey(Tsyscredentials, models.DO_NOTHING, db_column='CredID')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    isworkgroup = models.BooleanField(db_column='IsWorkgroup')  # Field name made lowercase.
    domaincredentialsid = models.BigAutoField(db_column='DomainCredentialsID', primary_key=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysDomainCredentials'
        unique_together = (('domainname', 'credid'),)


class Tsysdomainexclude(models.Model):
    domainexcludeid = models.AutoField(db_column='DomainExcludeID', primary_key=True)  # Field name made lowercase.
    domainname = models.CharField(db_column='DomainName', max_length=200)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='ServerName')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=150, blank=True, null=True)  # Field name made lowercase.
    assetexclusionreasonid = models.ForeignKey(Tsysassetexclusionreason, models.DO_NOTHING, db_column='AssetExclusionReasonId', blank=True, null=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysDomainExclude'


class Tsyseventalerts(models.Model):
    alertid = models.AutoField(db_column='AlertID', primary_key=True)  # Field name made lowercase.
    alertname = models.CharField(db_column='Alertname', max_length=500)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    mailgroup = models.CharField(db_column='Mailgroup', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysEventAlerts'


class Tsyseventfilter(models.Model):
    filterid = models.AutoField(db_column='FilterID', primary_key=True)  # Field name made lowercase.
    alertid = models.ForeignKey(Tsyseventalerts, models.DO_NOTHING, db_column='AlertID')  # Field name made lowercase.
    compare = models.IntegerField(db_column='Compare')  # Field name made lowercase.
    operator = models.IntegerField(db_column='Operator')  # Field name made lowercase.
    comparevalue = models.CharField(db_column='Comparevalue', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysEventfilter'


class Tsysexternalresources(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', unique=True)  # Field name made lowercase.
    resourcefile = models.BinaryField(db_column='ResourceFile')  # Field name made lowercase.
    resourcefilehash = models.CharField(db_column='ResourceFileHash', max_length=256)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysExternalResources'


class Tsysgatedmigrations(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    featuretoggle = models.CharField(db_column='FeatureToggle', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysGatedMigrations'


class Tsyshosttype(models.Model):
    hosttypeid = models.IntegerField(db_column='HostTypeId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    hosttypeicon = models.CharField(db_column='HostTypeIcon', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysHostType'


class Tsysipexclude(models.Model):
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='Servername')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPaddress', max_length=50)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=150, blank=True, null=True)  # Field name made lowercase.
    assetexclusionreasonid = models.ForeignKey(Tsysassetexclusionreason, models.DO_NOTHING, db_column='AssetExclusionReasonId', blank=True, null=True)  # Field name made lowercase.
    ipexcludeid = models.AutoField(db_column='IPExcludeId', primary_key=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysIPExclude'
        unique_together = (('servername', 'ipaddress'),)


class Tsysiplocations(models.Model):
    startip = models.DecimalField(db_column='StartIP', max_digits=18, decimal_places=0)  # Field name made lowercase.
    endip = models.DecimalField(db_column='EndIP', max_digits=18, decimal_places=0)  # Field name made lowercase.
    iplocation = models.CharField(db_column='IPLocation', max_length=200)  # Field name made lowercase.
    realstart = models.CharField(db_column='Realstart', max_length=20)  # Field name made lowercase.
    realend = models.CharField(db_column='Realend', max_length=20)  # Field name made lowercase.
    packageshare = models.CharField(db_column='PackageShare', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    shareusername = models.CharField(db_column='ShareUsername', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sharepassword = models.CharField(db_column='SharePassword', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    sharekeyhash = models.IntegerField(db_column='ShareKeyHash', blank=True, null=True)  # Field name made lowercase.
    locationid = models.AutoField(db_column='LocationID', primary_key=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysIPLocations'


class Tsysiprangecredentials(models.Model):
    iprangeid = models.ForeignKey('Tsysipscanranges', models.DO_NOTHING, db_column='IPrangeID')  # Field name made lowercase.
    credid = models.ForeignKey(Tsyscredentials, models.DO_NOTHING, db_column='CredID')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    iprangecredentialsid = models.BigAutoField(db_column='ipRangeCredentialsId', primary_key=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysIPRangeCredentials'
        unique_together = (('iprangeid', 'credid'),)


class Tsysipscanranges(models.Model):
    iprangeid = models.AutoField(db_column='IprangeID', primary_key=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='Servername')  # Field name made lowercase.
    ipstart = models.CharField(db_column='Ipstart', max_length=50)  # Field name made lowercase.
    ipend = models.CharField(db_column='Ipend', max_length=50)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    pingtimeout = models.IntegerField(db_column='PingTimeout')  # Field name made lowercase.
    ipignorewindows = models.BooleanField(db_column='IPIgnoreWindows')  # Field name made lowercase.
    dontping = models.BooleanField(db_column='DontPing')  # Field name made lowercase.
    day1 = models.BooleanField(db_column='Day1')  # Field name made lowercase.
    day2 = models.BooleanField(db_column='Day2')  # Field name made lowercase.
    day3 = models.BooleanField(db_column='Day3')  # Field name made lowercase.
    day4 = models.BooleanField(db_column='Day4')  # Field name made lowercase.
    day5 = models.BooleanField(db_column='Day5')  # Field name made lowercase.
    day6 = models.BooleanField(db_column='Day6')  # Field name made lowercase.
    day7 = models.BooleanField(db_column='Day7')  # Field name made lowercase.
    day1time = models.DateTimeField(db_column='Day1time')  # Field name made lowercase.
    day2time = models.DateTimeField(db_column='Day2time')  # Field name made lowercase.
    day3time = models.DateTimeField(db_column='Day3time')  # Field name made lowercase.
    day4time = models.DateTimeField(db_column='Day4time')  # Field name made lowercase.
    day5time = models.DateTimeField(db_column='Day5time')  # Field name made lowercase.
    day6time = models.DateTimeField(db_column='Day6time')  # Field name made lowercase.
    day7time = models.DateTimeField(db_column='Day7time')  # Field name made lowercase.
    lastipscan = models.DateTimeField(db_column='LastIPscan', blank=True, null=True)  # Field name made lowercase.
    nossh = models.BooleanField(db_column='NoSSH')  # Field name made lowercase.
    recurring = models.BooleanField(db_column='Recurring')  # Field name made lowercase.
    minutes = models.BooleanField(db_column='Minutes')  # Field name made lowercase.
    waittime = models.IntegerField(db_column='Waittime')  # Field name made lowercase.
    sshport = models.IntegerField(db_column='SSHport', blank=True, null=True)  # Field name made lowercase.
    savepingedip = models.BooleanField(db_column='SavePingedIP')  # Field name made lowercase.
    ipignoreknownwindows = models.BooleanField(db_column='IPIgnoreKnownWindows')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    sipport = models.IntegerField(db_column='SIPport')  # Field name made lowercase.
    scannow = models.BooleanField(db_column='ScanNow')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysIPScanRanges'
        unique_together = (('servername', 'ipstart', 'ipend'),)


class Tsysinfoblock(models.Model):
    infoblockid = models.IntegerField(db_column='InfoBlockId', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=250)  # Field name made lowercase.
    link = models.CharField(db_column='Link', max_length=250)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=250)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=4000)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded')  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=7, blank=True, null=True)  # Field name made lowercase.
    icon = models.CharField(db_column='Icon', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isglobal = models.BooleanField(db_column='IsGlobal', blank=True, null=True)  # Field name made lowercase.
    isseen = models.BooleanField(db_column='IsSeen', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysInfoBlock'


class Tsysinfoblockwebuserseen(models.Model):
    seenid = models.AutoField(db_column='SeenId', primary_key=True)  # Field name made lowercase.
    infoblockid = models.ForeignKey(Tsysinfoblock, models.DO_NOTHING, db_column='InfoBlockId')  # Field name made lowercase.
    pageid = models.ForeignKey('Tsyswebusers', models.DO_NOTHING, db_column='PageId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysInfoBlockWebUserSeen'


class Tsysinitialnetworkinterfaces(models.Model):
    interfaceid = models.AutoField(db_column='InterfaceID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=300, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=450, blank=True, null=True)  # Field name made lowercase.
    ipstart = models.CharField(db_column='IPStart', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ipend = models.CharField(db_column='IPEnd', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ipsubnet = models.CharField(db_column='IPSubnet', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ipmachine = models.CharField(db_column='IPMachine', max_length=50, blank=True, null=True)  # Field name made lowercase.
    systeminterfaceid = models.CharField(db_column='SystemInterfaceId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', max_length=20, blank=True, null=True)  # Field name made lowercase.
    enabledforassetradar = models.BooleanField(db_column='EnabledForAssetRadar')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    scanserver = models.CharField(db_column='Scanserver', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysInitialNetworkInterfaces'


class Tsysintunescanningtarget(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    scheduleid = models.ForeignKey('Tsysscanschedule', models.DO_NOTHING, db_column='ScheduleId')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    lastscanned = models.DateTimeField(db_column='Lastscanned', blank=True, null=True)  # Field name made lowercase.
    scannow = models.BooleanField(db_column='ScanNow')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    errortext = models.CharField(db_column='ErrorText', max_length=500, blank=True, null=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='Servername')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysIntuneScanningTarget'


class Tsysintunescanningtargetcredential(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    scanningtargetid = models.ForeignKey(Tsysintunescanningtarget, models.DO_NOTHING, db_column='ScanningTargetId')  # Field name made lowercase.
    credid = models.ForeignKey(Tsyscredentials, models.DO_NOTHING, db_column='CredId')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysIntuneScanningTargetCredential'


class Tsysintunev2Scanningtarget(models.Model):
    scanningtargetid = models.AutoField(db_column='ScanningTargetId', primary_key=True)  # Field name made lowercase.
    scheduleid = models.ForeignKey('Tsysscanschedule', models.DO_NOTHING, db_column='ScheduleId')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    lastscanned = models.DateTimeField(db_column='Lastscanned', blank=True, null=True)  # Field name made lowercase.
    scannow = models.BooleanField(db_column='ScanNow')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    errortext = models.CharField(db_column='ErrorText', max_length=500, blank=True, null=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='Servername')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysIntuneV2ScanningTarget'


class Tsysintunev2Scanningtargetcredential(models.Model):
    scanningtargetcredentialid = models.AutoField(db_column='ScanningTargetCredentialId', primary_key=True)  # Field name made lowercase.
    scanningtargetid = models.ForeignKey(Tsysintunev2Scanningtarget, models.DO_NOTHING, db_column='ScanningTargetId')  # Field name made lowercase.
    credid = models.ForeignKey(Tsyscredentials, models.DO_NOTHING, db_column='CredId')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysIntuneV2ScanningTargetCredential'
        unique_together = (('scanningtargetid', 'credid'),)


class Tsysios(models.Model):
    iosid = models.AutoField(db_column='IosId', primary_key=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    kernel = models.CharField(db_column='Kernel', max_length=50)  # Field name made lowercase.
    codename = models.CharField(db_column='CodeName', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysIos'


class Tsyslabeldocs(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tsysLabelDocs'


class Tsyslanguages(models.Model):
    languageid = models.IntegerField(db_column='LanguageId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    englishname = models.CharField(db_column='EnglishName', max_length=50)  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=10)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    supported = models.BooleanField(db_column='Supported')  # Field name made lowercase.
    culturename = models.CharField(db_column='CultureName', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysLanguages'


class Tsyslastcloudsyncdates(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    lastscansyncdate = models.DateTimeField(db_column='LastScanSyncDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysLastCloudSyncDates'


class Tsysldapconfiguration(models.Model):
    ldapid = models.AutoField(db_column='LdapId', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    dns = models.CharField(db_column='Dns', max_length=150, blank=True, null=True)  # Field name made lowercase.
    netbios = models.CharField(db_column='Netbios', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ldapport = models.IntegerField(db_column='LdapPort', blank=True, null=True)  # Field name made lowercase.
    ldapsport = models.IntegerField(db_column='LdapsPort', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysLdapConfiguration'


class Tsysldapconfigurationserver(models.Model):
    ldapserverid = models.AutoField(db_column='LdapServerId', primary_key=True)  # Field name made lowercase.
    ldapid = models.ForeignKey(Tsysldapconfiguration, models.DO_NOTHING, db_column='LdapId')  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='ServerName')  # Field name made lowercase.
    ldapstatus = models.IntegerField(db_column='LdapStatus')  # Field name made lowercase.
    ldaperror = models.CharField(db_column='LdapError', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    ldapsstatus = models.IntegerField(db_column='LdapsStatus')  # Field name made lowercase.
    ldapserror = models.CharField(db_column='LdapsError', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    laststatuscheck = models.DateTimeField(db_column='LastStatusCheck', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysLdapConfigurationServer'


class Tsyslicensetokens(models.Model):
    licensetokenid = models.AutoField(db_column='LicenseTokenId', primary_key=True)  # Field name made lowercase.
    token = models.CharField(db_column='Token', max_length=4000)  # Field name made lowercase.
    environment = models.ForeignKey('Tsysremoteconfigurationenvironment', models.DO_NOTHING, db_column='Environment')  # Field name made lowercase.
    tokentype = models.IntegerField(db_column='TokenType')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysLicenseTokens'


class Tsyslinuxfilescanning(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    filepath = models.CharField(db_column='FilePath', max_length=1000)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysLinuxFileScanning'


class Tsyslinuxsoftwaretype(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysLinuxSoftwareType'


class Tsyslocalinstallationnotification(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    criticality = models.IntegerField(db_column='Criticality')  # Field name made lowercase.
    category = models.IntegerField(db_column='Category')  # Field name made lowercase.
    icon = models.CharField(db_column='Icon', max_length=50)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=250)  # Field name made lowercase.
    menuurl = models.CharField(db_column='MenuUrl', max_length=250, blank=True, null=True)  # Field name made lowercase.
    kburl = models.CharField(db_column='KbUrl', max_length=250, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    permissionid = models.IntegerField(db_column='PermissionId', blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded')  # Field name made lowercase.
    datevaliduntil = models.DateTimeField(db_column='DateValidUntil', blank=True, null=True)  # Field name made lowercase.
    isdismissable = models.BooleanField(db_column='IsDismissable')  # Field name made lowercase.
    eventdatetoshow = models.DateTimeField(db_column='EventDateToShow', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysLocalInstallationNotification'


class Tsyslocalinstallationnotificationwebuserseen(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    localinstallationnotificationid = models.ForeignKey(Tsyslocalinstallationnotification, models.DO_NOTHING, db_column='LocalInstallationNotificationId')  # Field name made lowercase.
    pageid = models.ForeignKey('Tsyswebusers', models.DO_NOTHING, db_column='PageId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysLocalInstallationNotificationWebUserSeen'


class Tsysmacblacklist(models.Model):
    macblacklistid = models.AutoField(db_column='MacBlacklistId', primary_key=True)  # Field name made lowercase.
    mac = models.CharField(db_column='Mac', unique=True, max_length=128)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=512, blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysMacBlacklist'


class Tsysmacvendor(models.Model):
    mac = models.CharField(db_column='MAC', primary_key=True, max_length=6)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysMacVendor'


class Tsysmailconfig(models.Model):
    configid = models.AutoField(db_column='ConfigID', primary_key=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='ServerName', blank=True, null=True)  # Field name made lowercase.
    smtpserver = models.CharField(db_column='SMTPserver', max_length=250, blank=True, null=True)  # Field name made lowercase.
    smtpport = models.IntegerField(db_column='SMTPport', blank=True, null=True)  # Field name made lowercase.
    smtpfrom = models.CharField(db_column='SMTPFrom', max_length=250, blank=True, null=True)  # Field name made lowercase.
    smtpfromdisplay = models.CharField(db_column='SMTPFromDisplay', max_length=250, blank=True, null=True)  # Field name made lowercase.
    smtpauthenticate = models.BooleanField(db_column='SMTPAuthenticate', blank=True, null=True)  # Field name made lowercase.
    smtpusername = models.CharField(db_column='SMTPUsername', max_length=255, blank=True, null=True)  # Field name made lowercase.
    smtppassword = models.CharField(db_column='SMTPPassword', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    sendalertreports = models.BooleanField(db_column='SendAlertReports', blank=True, null=True)  # Field name made lowercase.
    sendeventalerts = models.BooleanField(db_column='SendEventAlerts', blank=True, null=True)  # Field name made lowercase.
    smtpusessl = models.BooleanField(db_column='SMTPUseSSL', blank=True, null=True)  # Field name made lowercase.
    mailnow = models.BooleanField(db_column='Mailnow', blank=True, null=True)  # Field name made lowercase.
    lastmailed = models.DateTimeField(db_column='LastMailed', blank=True, null=True)  # Field name made lowercase.
    smtppasswordkeyhash = models.IntegerField(db_column='SMTPPasswordKeyHash', blank=True, null=True)  # Field name made lowercase.
    smtpssl = models.SmallIntegerField(db_column='SMTPSSL', blank=True, null=True)  # Field name made lowercase.
    error = models.IntegerField(db_column='Error', blank=True, null=True)  # Field name made lowercase.
    errortext = models.CharField(db_column='ErrorText', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    lasttried = models.DateTimeField(db_column='LastTried', blank=True, null=True)  # Field name made lowercase.
    protocol = models.IntegerField(db_column='Protocol', blank=True, null=True)  # Field name made lowercase.
    clientid = models.CharField(db_column='ClientId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tenantid = models.CharField(db_column='TenantId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    clientsecret = models.CharField(db_column='ClientSecret', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysMailConfig'


class Tsysmailgroups(models.Model):
    mailgroup = models.CharField(db_column='Mailgroup', max_length=250)  # Field name made lowercase.
    members = models.CharField(db_column='Members', max_length=1000)  # Field name made lowercase.
    mailgroupid = models.AutoField(db_column='MailgroupID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysMailgroups'


class Tsysmanufacturertranslation(models.Model):
    manufacturertranslationid = models.AutoField(db_column='ManufacturerTranslationId', primary_key=True)  # Field name made lowercase.
    regex = models.CharField(db_column='Regex', unique=True, max_length=256)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysManufacturerTranslation'


class Tsysmodeltranslation(models.Model):
    modeltranslationid = models.AutoField(db_column='ModelTranslationId', primary_key=True)  # Field name made lowercase.
    regex = models.CharField(db_column='Regex', unique=True, max_length=256)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysModelTranslation'


class Tsysnewfeature(models.Model):
    featureid = models.IntegerField(db_column='FeatureId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=250)  # Field name made lowercase.
    icon = models.CharField(db_column='Icon', max_length=50)  # Field name made lowercase.
    link = models.CharField(db_column='Link', max_length=250)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=50)  # Field name made lowercase.
    isgated = models.BooleanField(db_column='IsGated')  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded')  # Field name made lowercase.
    permissionid = models.ForeignKey('Tsyspermissions', models.DO_NOTHING, db_column='PermissionId', blank=True, null=True)  # Field name made lowercase.
    menulink = models.CharField(db_column='MenuLink', max_length=250, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysNewFeature'


class Tsysnewfeaturewebuserseen(models.Model):
    seenid = models.AutoField(db_column='SeenId', primary_key=True)  # Field name made lowercase.
    featureid = models.ForeignKey(Tsysnewfeature, models.DO_NOTHING, db_column='FeatureId')  # Field name made lowercase.
    pageid = models.ForeignKey('Tsyswebusers', models.DO_NOTHING, db_column='PageId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysNewFeatureWebUserSeen'


class Tsyso365Scanningtarget(models.Model):
    scanningtargetid = models.AutoField(db_column='ScanningTargetId', primary_key=True)  # Field name made lowercase.
    scheduleid = models.ForeignKey('Tsysscanschedule', models.DO_NOTHING, db_column='ScheduleId')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    lastscanned = models.DateTimeField(db_column='Lastscanned', blank=True, null=True)  # Field name made lowercase.
    scannow = models.BooleanField(db_column='ScanNow')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    errortext = models.CharField(db_column='ErrorText', max_length=500, blank=True, null=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='Servername')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysO365ScanningTarget'


class Tsyso365Scanningtargetcredential(models.Model):
    scanningtargetcredentialid = models.AutoField(db_column='ScanningTargetCredentialId', primary_key=True)  # Field name made lowercase.
    scanningtargetid = models.ForeignKey(Tsyso365Scanningtarget, models.DO_NOTHING, db_column='ScanningTargetId')  # Field name made lowercase.
    credid = models.ForeignKey(Tsyscredentials, models.DO_NOTHING, db_column='CredId')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysO365ScanningTargetCredential'


class Tsyso365V2Scanningtarget(models.Model):
    scanningtargetid = models.AutoField(db_column='ScanningTargetId', primary_key=True)  # Field name made lowercase.
    scheduleid = models.ForeignKey('Tsysscanschedule', models.DO_NOTHING, db_column='ScheduleId')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    lastscanned = models.DateTimeField(db_column='Lastscanned', blank=True, null=True)  # Field name made lowercase.
    scannow = models.BooleanField(db_column='ScanNow')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    errortext = models.CharField(db_column='ErrorText', max_length=500, blank=True, null=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='Servername')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysO365V2ScanningTarget'


class Tsyso365V2Scanningtargetcredential(models.Model):
    scanningtargetcredentialid = models.AutoField(db_column='ScanningTargetCredentialId', primary_key=True)  # Field name made lowercase.
    scanningtargetid = models.ForeignKey(Tsyso365V2Scanningtarget, models.DO_NOTHING, db_column='ScanningTargetId')  # Field name made lowercase.
    credid = models.ForeignKey(Tsyscredentials, models.DO_NOTHING, db_column='CredId')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysO365V2ScanningTargetCredential'
        unique_together = (('scanningtargetid', 'credid'),)


class Tsysoidlookup(models.Model):
    oid = models.CharField(db_column='OID', unique=True, max_length=300)  # Field name made lowercase.
    itemtype = models.ForeignKey(Tsysassettypes, models.DO_NOTHING, db_column='Itemtype')  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=255)  # Field name made lowercase.
    lookupid = models.AutoField(db_column='LookupID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysOIDlookup'


class Tsysos(models.Model):
    oscode = models.CharField(db_column='OScode', primary_key=True, max_length=50)  # Field name made lowercase.
    osname = models.CharField(db_column='OSname', max_length=200)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=50)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='Sortorder')  # Field name made lowercase.
    oscodenumeric = models.BigIntegerField(db_column='OSCodeNumeric', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysOS'


class Tsyspackageexecution(models.Model):
    executionid = models.AutoField(db_column='ExecutionID', primary_key=True)  # Field name made lowercase.
    packagescheduleid = models.ForeignKey('Tsyspackageschedule', models.DO_NOTHING, db_column='PackageScheduleID')  # Field name made lowercase.
    scanserver = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='ScanServer')  # Field name made lowercase.
    lastrun = models.DateTimeField(db_column='LastRun')  # Field name made lowercase.
    executed = models.BooleanField(db_column='Executed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysPackageExecution'


class Tsyspackagelogtype(models.Model):
    typeid = models.AutoField(db_column='TypeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysPackageLogType'


class Tsyspackagelogs(models.Model):
    packagelogid = models.AutoField(db_column='PackageLogID', primary_key=True)  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID', blank=True, null=True)  # Field name made lowercase.
    packageid = models.IntegerField(db_column='PackageID')  # Field name made lowercase.
    success = models.BooleanField(db_column='Success')  # Field name made lowercase.
    errorcode = models.CharField(db_column='Errorcode', max_length=300, blank=True, null=True)  # Field name made lowercase.
    destination = models.CharField(db_column='Destination', max_length=300, blank=True, null=True)  # Field name made lowercase.
    errormessage = models.CharField(db_column='Errormessage', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    laststepid = models.IntegerField(db_column='LastStepID', blank=True, null=True)  # Field name made lowercase.
    added = models.DateTimeField(db_column='Added')  # Field name made lowercase.
    typeid = models.ForeignKey(Tsyspackagelogtype, models.DO_NOTHING, db_column='TypeID')  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='ServerName', blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='Ipaddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=50, blank=True, null=True)  # Field name made lowercase.
    executor = models.CharField(db_column='Executor', max_length=100, blank=True, null=True)  # Field name made lowercase.
    packagescheduleid = models.IntegerField(db_column='PackageScheduleID', blank=True, null=True)  # Field name made lowercase.
    runmode = models.IntegerField(db_column='RunMode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysPackageLogs'


class Tsyspackageschedule(models.Model):
    packagescheduleid = models.AutoField(db_column='PackageScheduleID', primary_key=True)  # Field name made lowercase.
    linktype = models.IntegerField(db_column='LinkType', blank=True, null=True)  # Field name made lowercase.
    scheduleid = models.ForeignKey('Tsysschedule', models.DO_NOTHING, db_column='ScheduleID', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.
    executor = models.CharField(db_column='Executor', max_length=100, blank=True, null=True)  # Field name made lowercase.
    creator = models.CharField(db_column='Creator', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifier = models.CharField(db_column='Modifier', max_length=100, blank=True, null=True)  # Field name made lowercase.
    runnow = models.BooleanField(db_column='RunNow', blank=True, null=True)  # Field name made lowercase.
    packageid = models.ForeignKey('Tsyspackages', models.DO_NOTHING, db_column='PackageID', blank=True, null=True)  # Field name made lowercase.
    reportquery = models.CharField(db_column='Reportquery', max_length=200, blank=True, null=True)  # Field name made lowercase.
    assetgroupid = models.ForeignKey(Tblassetgroups, models.DO_NOTHING, db_column='AssetGroupID', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    visible = models.BooleanField(db_column='Visible')  # Field name made lowercase.
    wol = models.BooleanField(db_column='WOL', blank=True, null=True)  # Field name made lowercase.
    woltime = models.IntegerField(db_column='WOLTime', blank=True, null=True)  # Field name made lowercase.
    reportparams = models.CharField(db_column='ReportParams', max_length=200, blank=True, null=True)  # Field name made lowercase.
    retrydate = models.DateTimeField(db_column='RetryDate', blank=True, null=True)  # Field name made lowercase.
    retrytime = models.IntegerField(db_column='RetryTime', blank=True, null=True)  # Field name made lowercase.
    deployafterscan = models.BooleanField(db_column='DeployAfterScan', blank=True, null=True)  # Field name made lowercase.
    runmode = models.IntegerField(db_column='RunMode', blank=True, null=True)  # Field name made lowercase.
    packageschedulereference = models.IntegerField(db_column='PackageScheduleReference', blank=True, null=True)  # Field name made lowercase.
    filters = models.CharField(db_column='Filters', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    haschanged = models.BooleanField(db_column='HasChanged')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysPackageSchedule'


class Tsyspackagescheduleasset(models.Model):
    scheduleassetid = models.AutoField(db_column='ScheduleAssetID', primary_key=True)  # Field name made lowercase.
    scheduleid = models.ForeignKey(Tsyspackageschedule, models.DO_NOTHING, db_column='ScheduleID')  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysPackageScheduleAsset'


class Tsyspackagestepconditionlinks(models.Model):
    conditionlinkid = models.AutoField(db_column='ConditionLinkID', primary_key=True)  # Field name made lowercase.
    conditiontypeid = models.ForeignKey('Tsyspackagestepconditiontypes', models.DO_NOTHING, db_column='ConditionTypeID')  # Field name made lowercase.
    conditionnameid = models.ForeignKey('Tsyspackagestepconditionnames', models.DO_NOTHING, db_column='ConditionNameID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysPackageStepConditionLinks'


class Tsyspackagestepconditionnames(models.Model):
    conditionnameid = models.IntegerField(db_column='ConditionNameID', primary_key=True)  # Field name made lowercase.
    conditionname = models.CharField(db_column='ConditionName', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysPackageStepConditionNames'


class Tsyspackagestepconditiontypes(models.Model):
    conditiontypeid = models.IntegerField(db_column='ConditionTypeID', primary_key=True)  # Field name made lowercase.
    typename = models.CharField(db_column='TypeName', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysPackageStepConditionTypes'


class Tsyspackagestepconditions(models.Model):
    conditionid = models.AutoField(db_column='ConditionID', primary_key=True)  # Field name made lowercase.
    packagestepid = models.ForeignKey('Tsyspackagesteps', models.DO_NOTHING, db_column='PackageStepID', blank=True, null=True)  # Field name made lowercase.
    conditiontypeid = models.ForeignKey(Tsyspackagestepconditiontypes, models.DO_NOTHING, db_column='ConditionTypeID')  # Field name made lowercase.
    specificationone = models.CharField(db_column='SpecificationOne', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    specificationtwo = models.CharField(db_column='SpecificationTwo', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    conditionnameid = models.ForeignKey(Tsyspackagestepconditionnames, models.DO_NOTHING, db_column='ConditionNameID', blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysPackageStepConditions'


class Tsyspackagesteptypes(models.Model):
    steptype = models.IntegerField(db_column='StepType', primary_key=True)  # Field name made lowercase.
    steptypename = models.CharField(db_column='StepTypeName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysPackageStepTypes'


class Tsyspackagesteps(models.Model):
    packagestepid = models.AutoField(db_column='PackageStepID', primary_key=True)  # Field name made lowercase.
    packageid = models.ForeignKey('Tsyspackages', models.DO_NOTHING, db_column='PackageID')  # Field name made lowercase.
    stepnr = models.IntegerField(db_column='StepNr', blank=True, null=True)  # Field name made lowercase.
    steptype = models.ForeignKey(Tsyspackagesteptypes, models.DO_NOTHING, db_column='StepType', blank=True, null=True)  # Field name made lowercase.
    stepname = models.CharField(db_column='StepName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    onsuccess = models.IntegerField(db_column='OnSuccess', blank=True, null=True)  # Field name made lowercase.
    onfailure = models.IntegerField(db_column='OnFailure', blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(db_column='Path', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    parameters = models.CharField(db_column='Parameters', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    exitcodes = models.CharField(db_column='Exitcodes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    commandline = models.CharField(db_column='Commandline', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    msiparameters = models.CharField(db_column='MSIParameters', max_length=500, blank=True, null=True)  # Field name made lowercase.
    msiname = models.CharField(db_column='MSIName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    msiversion = models.CharField(db_column='MSIVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    editmode = models.BooleanField(db_column='EditMode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysPackageSteps'


class Tsyspackages(models.Model):
    packageid = models.AutoField(db_column='PackageID', primary_key=True)  # Field name made lowercase.
    packagename = models.CharField(db_column='PackageName', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='Lastchanged', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='Createdby', max_length=255, blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='Changedby', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    shutdownoption = models.IntegerField(db_column='ShutdownOption', blank=True, null=True)  # Field name made lowercase.
    shutdowntime = models.IntegerField(db_column='ShutdownTime', blank=True, null=True)  # Field name made lowercase.
    timeout = models.IntegerField(db_column='Timeout')  # Field name made lowercase.
    rescan = models.BooleanField(db_column='Rescan')  # Field name made lowercase.
    runmode = models.IntegerField(db_column='RunMode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysPackages'


class Tsysperformancechartsettings(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    performancecountermetricid = models.ForeignKey('Tsysperformancecountermetric', models.DO_NOTHING, db_column='PerformanceCounterMetricId')  # Field name made lowercase.
    chartinterval = models.IntegerField(db_column='ChartInterval')  # Field name made lowercase.
    factor = models.FloatField(db_column='Factor')  # Field name made lowercase.
    chartname = models.CharField(db_column='ChartName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysPerformanceChartSettings'


class Tsysperformancecountermetric(models.Model):
    id = models.BigIntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250, blank=True, null=True)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=50)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysPerformanceCounterMetric'


class Tsysperformancecountertarget(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    interval = models.IntegerField(db_column='Interval')  # Field name made lowercase.
    targetgrouptype = models.IntegerField(db_column='TargetGroupType')  # Field name made lowercase.
    reportquery = models.ForeignKey('Tsysreports', models.DO_NOTHING, db_column='ReportQuery', blank=True, null=True)  # Field name made lowercase.
    assetgroupid = models.ForeignKey(Tblassetgroups, models.DO_NOTHING, db_column='AssetGroupId', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    metrics = models.BigIntegerField(db_column='Metrics', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysPerformanceCounterTarget'


class Tsysperformancecountertargetasset(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    performancecountertargetid = models.ForeignKey(Tsysperformancecountertarget, models.DO_NOTHING, db_column='PerformanceCounterTargetId')  # Field name made lowercase.
    assetid = models.ForeignKey(Tblassets, models.DO_NOTHING, db_column='AssetId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysPerformanceCounterTargetAsset'


class Tsysperformancecountertargetscan(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    performancecountertargetid = models.ForeignKey(Tsysperformancecountertarget, models.DO_NOTHING, db_column='PerformanceCounterTargetId')  # Field name made lowercase.
    scanserver = models.CharField(db_column='Scanserver', max_length=150)  # Field name made lowercase.
    lastscanned = models.DateTimeField(db_column='Lastscanned', blank=True, null=True)  # Field name made lowercase.
    errortext = models.CharField(db_column='ErrorText', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysPerformanceCounterTargetScan'


class Tsyspermissions(models.Model):
    permissionid = models.AutoField(db_column='PermissionID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=300)  # Field name made lowercase.
    icon = models.CharField(db_column='Icon', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysPermissions'


class Tsysprivacyconfiguration(models.Model):
    privacyconfigurationid = models.AutoField(db_column='PrivacyConfigurationId', primary_key=True)  # Field name made lowercase.
    allowsmetrics = models.BooleanField(db_column='AllowsMetrics')  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='ServerName', blank=True, null=True)  # Field name made lowercase.
    webserver = models.IntegerField(db_column='WebServer')  # Field name made lowercase.
    lastsentdate = models.DateTimeField(db_column='LastSentDate', blank=True, null=True)  # Field name made lowercase.
    lasterror = models.CharField(db_column='LastError', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysPrivacyConfiguration'


class Tsysrecognitionconfiguration(models.Model):
    recognitionconfigurationid = models.AutoField(db_column='RecognitionConfigurationId', primary_key=True)  # Field name made lowercase.
    token = models.CharField(db_column='Token', max_length=4000)  # Field name made lowercase.
    environment = models.ForeignKey('Tsysremoteconfigurationenvironment', models.DO_NOTHING, db_column='Environment')  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged')  # Field name made lowercase.
    hasinternetaccess = models.BooleanField(db_column='HasInternetAccess')  # Field name made lowercase.
    lastinternetaccesscheck = models.DateTimeField(db_column='LastInternetAccessCheck')  # Field name made lowercase.
    lastcatalogbrandmodelosupdate = models.DateTimeField(db_column='LastCatalogBrandModelOsUpdate', blank=True, null=True)  # Field name made lowercase.
    lastcatalogsoftwareupdate = models.DateTimeField(db_column='LastCatalogSoftwareUpdate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysRecognitionConfiguration'


class Tsysrecognitionprerequisitescheck(models.Model):
    recognitionprerequisitescheckid = models.AutoField(db_column='RecognitionPrerequisitesCheckId', primary_key=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='ServerName')  # Field name made lowercase.
    isserviceup = models.IntegerField(db_column='IsServiceUp')  # Field name made lowercase.
    hasinternetaccess = models.IntegerField(db_column='HasInternetAccess')  # Field name made lowercase.
    hasvalidlansweeperlicense = models.IntegerField(db_column='HasValidLansweeperLicense')  # Field name made lowercase.
    checkstarted = models.DateTimeField(db_column='CheckStarted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysRecognitionPrerequisitesCheck'


class Tsysrecognitionqueue(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', max_length=20)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysRecognitionQueue'


class Tsysremoteconfiguration(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    category = models.ForeignKey('Tsysremoteconfigurationcategory', models.DO_NOTHING, db_column='Category')  # Field name made lowercase.
    environment = models.ForeignKey('Tsysremoteconfigurationenvironment', models.DO_NOTHING, db_column='Environment')  # Field name made lowercase.
    configurationkey = models.CharField(db_column='ConfigurationKey', max_length=50)  # Field name made lowercase.
    configurationvalue = models.CharField(db_column='ConfigurationValue', max_length=4000)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysRemoteConfiguration'
        unique_together = (('category', 'environment', 'configurationkey'),)


class Tsysremoteconfigurationcategory(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysRemoteConfigurationCategory'


class Tsysremoteconfigurationenvironment(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    environment = models.CharField(db_column='Environment', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysRemoteConfigurationEnvironment'


class Tsysremotedatabases(models.Model):
    remotedatabaseid = models.AutoField(db_column='RemoteDatabaseID', primary_key=True)  # Field name made lowercase.
    ip_dns = models.CharField(db_column='IP/DNS', max_length=150)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    port = models.IntegerField(db_column='Port')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=250)  # Field name made lowercase.
    runnow = models.BooleanField(db_column='RunNow')  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250, blank=True, null=True)  # Field name made lowercase.
    scheduleid = models.IntegerField(db_column='ScheduleID')  # Field name made lowercase.
    lastscan = models.DateTimeField(db_column='Lastscan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysRemoteDatabases'


class Tsysrolemembers(models.Model):
    memberid = models.AutoField(db_column='MemberID', primary_key=True)  # Field name made lowercase.
    roleid = models.ForeignKey('Tsysroles', models.DO_NOTHING, db_column='RoleID')  # Field name made lowercase.
    member = models.CharField(db_column='Member', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysRoleMembers'


class Tsysrolepermissions(models.Model):
    rolepermissionid = models.AutoField(db_column='RolePermissionID', primary_key=True)  # Field name made lowercase.
    roleid = models.ForeignKey('Tsysroles', models.DO_NOTHING, db_column='RoleID')  # Field name made lowercase.
    permissionid = models.ForeignKey(Tsyspermissions, models.DO_NOTHING, db_column='PermissionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysRolePermissions'


class Tsysroles(models.Model):
    roleid = models.AutoField(db_column='RoleID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=300)  # Field name made lowercase.
    default = models.BooleanField(db_column='Default')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysRoles'


class Tsysscanschedule(models.Model):
    scheduleid = models.AutoField(db_column='ScheduleId', primary_key=True)  # Field name made lowercase.
    day1 = models.BooleanField(db_column='Day1')  # Field name made lowercase.
    day2 = models.BooleanField(db_column='Day2')  # Field name made lowercase.
    day3 = models.BooleanField(db_column='Day3')  # Field name made lowercase.
    day4 = models.BooleanField(db_column='Day4')  # Field name made lowercase.
    day5 = models.BooleanField(db_column='Day5')  # Field name made lowercase.
    day6 = models.BooleanField(db_column='Day6')  # Field name made lowercase.
    day7 = models.BooleanField(db_column='Day7')  # Field name made lowercase.
    day1time = models.DateTimeField(db_column='Day1time')  # Field name made lowercase.
    day2time = models.DateTimeField(db_column='Day2time')  # Field name made lowercase.
    day3time = models.DateTimeField(db_column='Day3time')  # Field name made lowercase.
    day4time = models.DateTimeField(db_column='Day4time')  # Field name made lowercase.
    day5time = models.DateTimeField(db_column='Day5time')  # Field name made lowercase.
    day6time = models.DateTimeField(db_column='Day6time')  # Field name made lowercase.
    day7time = models.DateTimeField(db_column='Day7time')  # Field name made lowercase.
    recurring = models.BooleanField(db_column='Recurring')  # Field name made lowercase.
    minutes = models.BooleanField(db_column='Minutes')  # Field name made lowercase.
    waittime = models.IntegerField(db_column='Waittime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysScanSchedule'


class Tsysscannedby(models.Model):
    scannedbyid = models.IntegerField(db_column='ScannedById', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysScannedBy'


class Tsysscanningmethods(models.Model):
    scanningmethodid = models.IntegerField(db_column='ScanningMethodId', primary_key=True)  # Field name made lowercase.
    scanningmethod = models.CharField(db_column='ScanningMethod', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysScanningMethods'


class Tsyssccmscanningtarget(models.Model):
    scanningtargetid = models.AutoField(db_column='ScanningTargetId', primary_key=True)  # Field name made lowercase.
    scheduleid = models.ForeignKey(Tsysscanschedule, models.DO_NOTHING, db_column='ScheduleId')  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='ServerName')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    lastscanned = models.DateTimeField(db_column='LastScanned', blank=True, null=True)  # Field name made lowercase.
    scannow = models.BooleanField(db_column='ScanNow')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    errortext = models.CharField(db_column='ErrorText', max_length=500, blank=True, null=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysSccmScanningTarget'


class Tsyssccmscanningtargetcredential(models.Model):
    scanningtargetcredentialid = models.AutoField(db_column='ScanningTargetCredentialId', primary_key=True)  # Field name made lowercase.
    scanningtargetid = models.ForeignKey(Tsyssccmscanningtarget, models.DO_NOTHING, db_column='ScanningTargetId')  # Field name made lowercase.
    credid = models.ForeignKey(Tsyscredentials, models.DO_NOTHING, db_column='CredId')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysSccmScanningTargetCredential'


class Tsysschedule(models.Model):
    scheduleid = models.AutoField(db_column='ScheduleID', primary_key=True)  # Field name made lowercase.
    schedulename = models.CharField(db_column='ScheduleName', max_length=50)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime')  # Field name made lowercase.
    interval = models.BigIntegerField(db_column='Interval', blank=True, null=True)  # Field name made lowercase.
    weekdays = models.SmallIntegerField(db_column='WeekDays', blank=True, null=True)  # Field name made lowercase.
    monthdays = models.IntegerField(db_column='MonthDays', blank=True, null=True)  # Field name made lowercase.
    executionmode = models.CharField(db_column='ExecutionMode', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysSchedule'


class Tsysserialtranslation(models.Model):
    serialtranslationid = models.AutoField(db_column='SerialTranslationId', primary_key=True)  # Field name made lowercase.
    regex = models.CharField(db_column='Regex', unique=True, max_length=256)  # Field name made lowercase.
    serial = models.CharField(db_column='Serial', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysSerialTranslation'


class Tsyssqllicensetypes(models.Model):
    licensetype = models.IntegerField(db_column='LicenseType', primary_key=True)  # Field name made lowercase.
    licensetypename = models.CharField(db_column='LicenseTypeName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysSqlLicenseTypes'


class Tsyssystemskutranslation(models.Model):
    systemskutranslationid = models.AutoField(db_column='SystemSkuTranslationId', primary_key=True)  # Field name made lowercase.
    regex = models.CharField(db_column='Regex', unique=True, max_length=256)  # Field name made lowercase.
    systemsku = models.CharField(db_column='SystemSku', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysSystemSkuTranslation'


class Tsysuniqueipcredentials(models.Model):
    ipaddress = models.CharField(db_column='IPAddress', max_length=15)  # Field name made lowercase.
    credid = models.ForeignKey(Tsyscredentials, models.DO_NOTHING, db_column='CredID')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    uniqueipcredentialsid = models.AutoField(db_column='UniqueIPCredentialsId', primary_key=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysUniqueIPCredentials'
        unique_together = (('ipaddress', 'credid'),)


class Tsysuniquewindowscredentials(models.Model):
    assetunique = models.CharField(db_column='AssetUnique', unique=True, max_length=300)  # Field name made lowercase.
    credid = models.ForeignKey(Tsyscredentials, models.DO_NOTHING, db_column='CredID')  # Field name made lowercase.
    uniquewindowscredentialsid = models.AutoField(db_column='UniqueWindowsCredentialsId', primary_key=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysUniqueWindowsCredentials'
        unique_together = (('assetunique', 'credid'),)


class Tsysuserschedule(models.Model):
    scheduleid = models.AutoField(db_column='ScheduleID', primary_key=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='Servername')  # Field name made lowercase.
    scantarget = models.CharField(db_column='Scantarget', max_length=1024)  # Field name made lowercase.
    netbiosdomain = models.CharField(db_column='Netbiosdomain', max_length=150)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    scannow = models.BooleanField(db_column='ScanNow')  # Field name made lowercase.
    day1 = models.BooleanField(db_column='Day1')  # Field name made lowercase.
    day2 = models.BooleanField(db_column='Day2')  # Field name made lowercase.
    day3 = models.BooleanField(db_column='Day3')  # Field name made lowercase.
    day4 = models.BooleanField(db_column='Day4')  # Field name made lowercase.
    day5 = models.BooleanField(db_column='Day5')  # Field name made lowercase.
    day6 = models.BooleanField(db_column='Day6')  # Field name made lowercase.
    day7 = models.BooleanField(db_column='Day7')  # Field name made lowercase.
    day1time = models.DateTimeField(db_column='Day1time')  # Field name made lowercase.
    day2time = models.DateTimeField(db_column='Day2time')  # Field name made lowercase.
    day3time = models.DateTimeField(db_column='Day3time')  # Field name made lowercase.
    day4time = models.DateTimeField(db_column='Day4time')  # Field name made lowercase.
    day5time = models.DateTimeField(db_column='Day5time')  # Field name made lowercase.
    day6time = models.DateTimeField(db_column='Day6time')  # Field name made lowercase.
    day7time = models.DateTimeField(db_column='Day7time')  # Field name made lowercase.
    lastscanned = models.DateTimeField(db_column='LastScanned', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    errortext = models.CharField(db_column='ErrorText', max_length=250, blank=True, null=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysUserSchedule'


class Tsyswaitqueue(models.Model):
    scanid = models.BigAutoField(db_column='Scanid', primary_key=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='Servername')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysWaitQueue'


class Tsyswarrantyprerequisitescheck(models.Model):
    warrantyprerequisitescheckid = models.AutoField(db_column='WarrantyPrerequisitesCheckId', primary_key=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='ServerName')  # Field name made lowercase.
    hasinternetaccess = models.IntegerField(db_column='HasInternetAccess')  # Field name made lowercase.
    checkstarted = models.DateTimeField(db_column='CheckStarted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysWarrantyPrerequisitesCheck'


class Tsyswebcontrols(models.Model):
    controlid = models.IntegerField(db_column='ControlID', primary_key=True)  # Field name made lowercase.
    controlname = models.CharField(db_column='ControlName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(db_column='Path', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    icon = models.CharField(db_column='Icon', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    canedit = models.BooleanField(db_column='CanEdit')  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='IsDefault')  # Field name made lowercase.
    preload = models.BooleanField(db_column='Preload')  # Field name made lowercase.
    category = models.IntegerField(db_column='Category')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysWebControls'


class Tsyswebroles(models.Model):
    authid = models.IntegerField(db_column='AuthID', primary_key=True)  # Field name made lowercase.
    authdescription = models.CharField(db_column='AuthDescription', max_length=255)  # Field name made lowercase.
    authmembers = models.CharField(db_column='AuthMembers', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    info = models.CharField(db_column='Info', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysWebRoles'


class Tsyswebtabcontrols(models.Model):
    tabcontrolid = models.AutoField(db_column='TabControlID', primary_key=True)  # Field name made lowercase.
    tabid = models.ForeignKey('Tsyswebtabs', models.DO_NOTHING, db_column='TabID')  # Field name made lowercase.
    controlid = models.ForeignKey(Tsyswebcontrols, models.DO_NOTHING, db_column='ControlID')  # Field name made lowercase.
    rowid = models.IntegerField(db_column='RowID')  # Field name made lowercase.
    columnid = models.IntegerField(db_column='ColumnID')  # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysWebTabControls'


class Tsyswebtabs(models.Model):
    tabid = models.AutoField(db_column='TabID', primary_key=True)  # Field name made lowercase.
    tabname = models.CharField(db_column='TabName', max_length=255)  # Field name made lowercase.
    pageid = models.ForeignKey('Tsyswebusers', models.DO_NOTHING, db_column='PageID')  # Field name made lowercase.
    templateid = models.IntegerField(db_column='TemplateID')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='Sortorder', blank=True, null=True)  # Field name made lowercase.
    globaltabs = models.BooleanField(db_column='GlobalTabs')  # Field name made lowercase.
    helpdesk = models.BooleanField(db_column='Helpdesk', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysWebTabs'


class Tsyswebusers(models.Model):
    pageid = models.AutoField(db_column='PageID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=150)  # Field name made lowercase.
    dateformat = models.CharField(db_column='DateFormat', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sortascending = models.BooleanField(blank=True, null=True)
    language = models.IntegerField()
    searchnewtab = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tsysWebUsers'


class Tsyswebusersglobaltabs(models.Model):
    pageid = models.IntegerField(db_column='PageID', primary_key=True)  # Field name made lowercase.
    tabid = models.ForeignKey(Tsyswebtabs, models.DO_NOTHING, db_column='TabID')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='Sortorder')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysWebUsersGlobalTabs'
        unique_together = (('pageid', 'tabid'),)


class Tsysactions(models.Model):
    description = models.CharField(db_column='Description', max_length=300)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=1000)  # Field name made lowercase.
    icon = models.CharField(db_column='Icon', max_length=50)  # Field name made lowercase.
    sortorder = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    enabled = models.BooleanField()
    confirmation = models.BooleanField()
    advanced = models.BooleanField(db_column='Advanced', blank=True, null=True)  # Field name made lowercase.
    ishyperlink = models.BooleanField(blank=True, null=True)
    actionid = models.AutoField(db_column='ActionID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysactions'


class Tsysadmins(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    domain = models.CharField(db_column='Domain', max_length=150)  # Field name made lowercase.
    adminname = models.CharField(db_column='AdminName', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysadmins'


class Tsysantivirus(models.Model):
    software = models.CharField(db_column='Software', max_length=300)  # Field name made lowercase.
    antivirusid = models.AutoField(db_column='AntivirusId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysantivirus'


class Tsysasseterrortypes(models.Model):
    errortype = models.IntegerField(db_column='Errortype', primary_key=True)  # Field name made lowercase.
    errormsg = models.CharField(db_column='ErrorMsg', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysasseterrortypes'


class Tsysassetlinks(models.Model):
    vendor = models.CharField(db_column='Vendor', primary_key=True, max_length=300)  # Field name made lowercase.
    assetlink = models.CharField(db_column='Assetlink', max_length=1024)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysassetlinks'


class Tsyserrors(models.Model):
    errorid = models.AutoField(db_column='Errorid', primary_key=True)  # Field name made lowercase.
    errortype = models.ForeignKey('Tsyserrortype', models.DO_NOTHING, db_column='Errortype')  # Field name made lowercase.
    errormsg = models.CharField(db_column='Errormsg', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    scanserver = models.CharField(db_column='Scanserver', max_length=300, blank=True, null=True)  # Field name made lowercase.
    added = models.DateTimeField(db_column='Added')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsyserrors'


class Tsyserrortype(models.Model):
    errortype = models.IntegerField(db_column='ErrorType', primary_key=True)  # Field name made lowercase.
    errorname = models.CharField(db_column='Errorname', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsyserrortype'


class Tsyseventignore(models.Model):
    ignoreid = models.AutoField(db_column='IgnoreID', primary_key=True)  # Field name made lowercase.
    sourcename = models.CharField(db_column='Sourcename', max_length=100)  # Field name made lowercase.
    eventcode = models.IntegerField(db_column='Eventcode', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsyseventignore'


class Tsyshisttables(models.Model):
    display = models.CharField(db_column='Display', primary_key=True, max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsyshisttables'


class Tsyslicensetype(models.Model):
    licensetype = models.IntegerField(db_column='LicenseType', primary_key=True)  # Field name made lowercase.
    licensetypename = models.CharField(db_column='LicenseTypeName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsyslicensetype'


class Tsyslogschedule(models.Model):
    scheduleid = models.AutoField(db_column='ScheduleID', primary_key=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='Servername')  # Field name made lowercase.
    scantype = models.DecimalField(db_column='Scantype', max_digits=18, decimal_places=0)  # Field name made lowercase.
    scantarget = models.CharField(db_column='Scantarget', max_length=1024)  # Field name made lowercase.
    netbiosdomain = models.CharField(db_column='Netbiosdomain', max_length=150)  # Field name made lowercase.
    everyxvalue = models.DecimalField(db_column='EveryXvalue', max_digits=18, decimal_places=0)  # Field name made lowercase.
    everyx = models.CharField(db_column='EveryX', max_length=1)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled')  # Field name made lowercase.
    lastscanned = models.DateTimeField(db_column='LastScanned', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    scannow = models.BooleanField(db_column='ScanNow')  # Field name made lowercase.
    errortext = models.CharField(db_column='ErrorText', max_length=250, blank=True, null=True)  # Field name made lowercase.
    cloudid = models.CharField(db_column='CloudId', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsyslogschedule'


class Tsyspages(models.Model):
    pageid = models.IntegerField(db_column='PageID', primary_key=True)  # Field name made lowercase.
    pagename = models.CharField(db_column='Pagename', max_length=150)  # Field name made lowercase.
    sortorder = models.DecimalField(db_column='Sortorder', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tsyspages'


class Tsysreportpages(models.Model):
    homepageid = models.AutoField(db_column='HomepageID', primary_key=True)  # Field name made lowercase.
    homepagequery = models.ForeignKey('Tsysreports', models.DO_NOTHING, db_column='HomepageQuery')  # Field name made lowercase.
    sortorder = models.DecimalField(db_column='Sortorder', max_digits=18, decimal_places=0)  # Field name made lowercase.
    priority = models.DecimalField(db_column='Priority', max_digits=18, decimal_places=0)  # Field name made lowercase.
    showcolor = models.BooleanField(db_column='Showcolor')  # Field name made lowercase.
    pageid = models.ForeignKey(Tsyspages, models.DO_NOTHING, db_column='PageID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysreportpages'


class Tsysreports(models.Model):
    reportquery = models.CharField(db_column='Reportquery', primary_key=True, max_length=200)  # Field name made lowercase.
    reporttitle = models.CharField(db_column='Reporttitle', max_length=1000)  # Field name made lowercase.
    sendmail = models.BooleanField(db_column='Sendmail', blank=True, null=True)  # Field name made lowercase.
    mailgroup = models.CharField(db_column='Mailgroup', max_length=250, blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    lastchanged = models.DateTimeField(db_column='LastChanged', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=150, blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lastrun = models.DateTimeField(db_column='LastRun', blank=True, null=True)  # Field name made lowercase.
    permissions = models.CharField(db_column='Permissions', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    alerttype = models.BooleanField(db_column='AlertType', blank=True, null=True)  # Field name made lowercase.
    exporttype = models.IntegerField(db_column='ExportType', blank=True, null=True)  # Field name made lowercase.
    overwrite = models.BooleanField(db_column='Overwrite', blank=True, null=True)  # Field name made lowercase.
    lastalert = models.DateTimeField(db_column='LastAlert', blank=True, null=True)  # Field name made lowercase.
    exporterror = models.CharField(db_column='ExportError', max_length=250, blank=True, null=True)  # Field name made lowercase.
    sendnow = models.BooleanField(db_column='SendNow', blank=True, null=True)  # Field name made lowercase.
    errordate = models.DateTimeField(db_column='ErrorDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysreports'


class Tsysscanqueue(models.Model):
    scanid = models.BigAutoField(db_column='Scanid', primary_key=True)  # Field name made lowercase.
    servername = models.ForeignKey(Tsysasservers, models.DO_NOTHING, db_column='Servername')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    scantarget = models.CharField(db_column='Scantarget', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysscanqueue'


class Tsysupdate(models.Model):
    config = models.IntegerField(db_column='Config', primary_key=True)  # Field name made lowercase.
    credentials = models.DateTimeField(db_column='Credentials', blank=True, null=True)  # Field name made lowercase.
    license = models.DateTimeField(db_column='License', blank=True, null=True)  # Field name made lowercase.
    waittime = models.DateTimeField(db_column='Waittime', blank=True, null=True)  # Field name made lowercase.
    files = models.DateTimeField(db_column='Files', blank=True, null=True)  # Field name made lowercase.
    registry = models.DateTimeField(db_column='Registry', blank=True, null=True)  # Field name made lowercase.
    productkeys = models.DateTimeField(db_column='Productkeys', blank=True, null=True)  # Field name made lowercase.
    eventsignore = models.DateTimeField(db_column='EventsIgnore', blank=True, null=True)  # Field name made lowercase.
    eventalert = models.DateTimeField(db_column='EventAlert', blank=True, null=True)  # Field name made lowercase.
    mail = models.DateTimeField(db_column='Mail', blank=True, null=True)  # Field name made lowercase.
    eventscan = models.DateTimeField(db_column='Eventscan', blank=True, null=True)  # Field name made lowercase.
    proxy = models.DateTimeField(db_column='Proxy')  # Field name made lowercase.
    macblacklist = models.DateTimeField(db_column='MacBlacklist', blank=True, null=True)  # Field name made lowercase.
    manufacturertranslation = models.DateTimeField(db_column='ManufacturerTranslation', blank=True, null=True)  # Field name made lowercase.
    ipexcluxions = models.DateTimeField(db_column='IpExcluxions')  # Field name made lowercase.
    renamedcomputerdetection = models.DateTimeField(db_column='RenamedComputerDetection')  # Field name made lowercase.
    deployment = models.DateTimeField(db_column='Deployment')  # Field name made lowercase.
    assettypeexclusions = models.DateTimeField(db_column='AssetTypeExclusions')  # Field name made lowercase.
    domainexclusions = models.DateTimeField(db_column='DomainExclusions', blank=True, null=True)  # Field name made lowercase.
    scanhistory = models.DateTimeField(db_column='ScanHistory')  # Field name made lowercase.
    domainuserscanning = models.DateTimeField(db_column='DomainUserScanning')  # Field name made lowercase.
    scheduledcomputerscanning = models.DateTimeField(db_column='ScheduledComputerScanning')  # Field name made lowercase.
    assetgroups = models.DateTimeField(db_column='AssetGroups', blank=True, null=True)  # Field name made lowercase.
    asdomains = models.DateTimeField(db_column='AsDomains', blank=True, null=True)  # Field name made lowercase.
    asou = models.DateTimeField(db_column='AsOU', blank=True, null=True)  # Field name made lowercase.
    assetgroupscan = models.DateTimeField(db_column='AssetGroupScan', blank=True, null=True)  # Field name made lowercase.
    asworkgroups = models.DateTimeField(db_column='AsWorkgroups', blank=True, null=True)  # Field name made lowercase.
    donotscan = models.DateTimeField(db_column='DoNotScan', blank=True, null=True)  # Field name made lowercase.
    ipscanranges = models.DateTimeField(db_column='IpScanRanges', blank=True, null=True)  # Field name made lowercase.
    logschedule = models.DateTimeField(db_column='LogSchedule', blank=True, null=True)  # Field name made lowercase.
    macvendor = models.DateTimeField(db_column='MacVendor', blank=True, null=True)  # Field name made lowercase.
    oidlookup = models.DateTimeField(db_column='OidLookup', blank=True, null=True)  # Field name made lowercase.
    vendoroid = models.DateTimeField(db_column='VendorOid', blank=True, null=True)  # Field name made lowercase.
    asservers = models.DateTimeField(db_column='AsServers', blank=True, null=True)  # Field name made lowercase.
    tsysconfig = models.DateTimeField(db_column='TsysConfig', blank=True, null=True)  # Field name made lowercase.
    domaincontrollers = models.DateTimeField(db_column='DomainControllers', blank=True, null=True)  # Field name made lowercase.
    assites = models.DateTimeField(db_column='ASSites', blank=True, null=True)  # Field name made lowercase.
    modeltranslation = models.DateTimeField(db_column='ModelTranslation', blank=True, null=True)  # Field name made lowercase.
    serialtranslation = models.DateTimeField(db_column='SerialTranslation', blank=True, null=True)  # Field name made lowercase.
    systemskutranslation = models.DateTimeField(db_column='SystemSkuTranslation', blank=True, null=True)  # Field name made lowercase.
    helpdeskmailconfig = models.DateTimeField(db_column='HelpDeskMailConfig')  # Field name made lowercase.
    iplocations = models.DateTimeField(db_column='IPLocations', blank=True, null=True)  # Field name made lowercase.
    outgoingemailtemplates = models.DateTimeField(db_column='OutgoingEmailTemplates', blank=True, null=True)  # Field name made lowercase.
    agentoptions = models.DateTimeField(db_column='AgentOptions', blank=True, null=True)  # Field name made lowercase.
    helpdeskconfig = models.DateTimeField(db_column='HelpdeskConfig', blank=True, null=True)  # Field name made lowercase.
    helpdeskmailfilterconfig = models.DateTimeField(db_column='HelpDeskMailFilterConfig')  # Field name made lowercase.
    helpdeskfooterattachementsconfig = models.DateTimeField(db_column='HelpDeskFooterAttachementsConfig')  # Field name made lowercase.
    lsagentasset = models.DateTimeField(db_column='LsAgentAsset', blank=True, null=True)  # Field name made lowercase.
    lsagentgroup = models.DateTimeField(db_column='LsAgentGroup', blank=True, null=True)  # Field name made lowercase.
    lsagenturl = models.DateTimeField(db_column='LsAgentUrl', blank=True, null=True)  # Field name made lowercase.
    lsagentscanoption = models.DateTimeField(db_column='LsAgentScanOption', blank=True, null=True)  # Field name made lowercase.
    lsagentserverconfig = models.DateTimeField(db_column='LsAgentServerConfig', blank=True, null=True)  # Field name made lowercase.
    lsagentconfiguration = models.DateTimeField(db_column='LsAgentConfiguration', blank=True, null=True)  # Field name made lowercase.
    oidtargets = models.DateTimeField(db_column='OIDTargets', blank=True, null=True)  # Field name made lowercase.
    powershelldefinition = models.DateTimeField(db_column='PowershellDefinition', blank=True, null=True)  # Field name made lowercase.
    awsscanningregions = models.DateTimeField(db_column='AwsScanningRegions', blank=True, null=True)  # Field name made lowercase.
    office365scanningtargets = models.DateTimeField(db_column='Office365ScanningTargets', blank=True, null=True)  # Field name made lowercase.
    azurescanningtargets = models.DateTimeField(db_column='AzureScanningTargets', blank=True, null=True)  # Field name made lowercase.
    intunescanningtargets = models.DateTimeField(db_column='IntuneScanningTargets', blank=True, null=True)  # Field name made lowercase.
    performancecounterscanningtargets = models.DateTimeField(db_column='PerformanceCounterScanningTargets', blank=True, null=True)  # Field name made lowercase.
    cloudconfig = models.DateTimeField(db_column='CloudConfig', blank=True, null=True)  # Field name made lowercase.
    chromeosscanningtargets = models.DateTimeField(db_column='ChromeOsScanningTargets', blank=True, null=True)  # Field name made lowercase.
    airwatchscanningtargets = models.DateTimeField(db_column='AirWatchScanningTargets', blank=True, null=True)  # Field name made lowercase.
    sccmscanningtargets = models.DateTimeField(db_column='SccmScanningTargets', blank=True, null=True)  # Field name made lowercase.
    assetradarinterfaces = models.DateTimeField(db_column='AssetRadarInterfaces', blank=True, null=True)  # Field name made lowercase.
    remoteconfiguration = models.DateTimeField(db_column='RemoteConfiguration', blank=True, null=True)  # Field name made lowercase.
    office365v2scanningtargets = models.DateTimeField(db_column='Office365V2ScanningTargets', blank=True, null=True)  # Field name made lowercase.
    intunev2scanningtargets = models.DateTimeField(db_column='IntuneV2ScanningTargets', blank=True, null=True)  # Field name made lowercase.
    ldapconfiguration = models.DateTimeField(db_column='LdapConfiguration', blank=True, null=True)  # Field name made lowercase.
    azureadscanningtargets = models.DateTimeField(db_column='AzureAdScanningTargets', blank=True, null=True)  # Field name made lowercase.
    externalresources = models.DateTimeField(db_column='ExternalResources', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysupdate'


class Tsysuseractions(models.Model):
    description = models.CharField(db_column='Description', max_length=300)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=1000)  # Field name made lowercase.
    icon = models.CharField(db_column='Icon', max_length=50)  # Field name made lowercase.
    sortorder = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    enabled = models.BooleanField()
    confirmation = models.BooleanField()
    advanced = models.BooleanField(db_column='Advanced', blank=True, null=True)  # Field name made lowercase.
    actionid = models.AutoField(db_column='ActionID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysuseractions'


class Tsysvendoroid(models.Model):
    oid = models.DecimalField(db_column='OID', primary_key=True, max_digits=18, decimal_places=0)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsysvendorOID'


class Tsysvendorlogos(models.Model):
    vendor = models.CharField(db_column='Vendor', primary_key=True, max_length=200)  # Field name made lowercase.
    logo = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tsysvendorlogos'
