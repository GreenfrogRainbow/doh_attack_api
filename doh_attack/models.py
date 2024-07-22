from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    birth = models.CharField(max_length=255, null=False)
    profession = models.CharField(max_length=255, null=False)
    useravatar = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'user'


class flowData(models.Model):
    SourcePortPre = models.CharField(max_length=255, null=False)
    FlowBytesSentPre = models.CharField(max_length=255, null=False)
    FlowBytesReceivedPre = models.CharField(max_length=255, null=False)
    DurationPre = models.CharField(max_length=255, null=False)
    SourceIP = models.CharField(max_length=255, null=False)
    DestinationIP = models.CharField(max_length=255, null=False)
    SourcePort = models.CharField(max_length=255, null=False)
    DestinationPort = models.CharField(max_length=255, null=False)
    TimeStamp = models.CharField(max_length=255, null=False)
    Duration = models.CharField(max_length=255, null=False)
    FlowBytesSent = models.CharField(max_length=255, null=False)
    FlowSentRate = models.CharField(max_length=255, null=False)
    FlowBytesReceived = models.CharField(max_length=255, null=False)
    FlowReceivedRate = models.CharField(max_length=255, null=False)
    PacketLengthVariance = models.CharField(max_length=255, null=False)
    PacketLengthStandardDeviation = models.CharField(max_length=255, null=False)
    PacketLengthMean = models.CharField(max_length=255, null=False)
    PacketLengthMedian = models.CharField(max_length=255, null=False)
    PacketLengthMode = models.CharField(max_length=255, null=False)
    PacketLengthSkewFromMedian = models.CharField(max_length=255, null=False)
    PacketLengthSkewFromMode = models.CharField(max_length=255, null=False)
    PacketLengthCoefficientofVariation = models.CharField(max_length=255, null=False)
    PacketTimeVariance = models.CharField(max_length=255, null=False)
    PacketTimeStandardDeviation = models.CharField(max_length=255, null=False)
    PacketTimeMean = models.CharField(max_length=255, null=False)
    PacketTimeMedian = models.CharField(max_length=255, null=False)
    PacketTimeMode = models.CharField(max_length=255, null=False)
    PacketTimeSkewFromMedian = models.CharField(max_length=255, null=False)
    PacketTimeSkewFromMode = models.CharField(max_length=255, null=False)
    PacketTimeCoefficientofVariation = models.CharField(max_length=255, null=False)
    ResponseTimeTimeVariance = models.CharField(max_length=255, null=False)
    ResponseTimeTimeStandardDeviation = models.CharField(max_length=255, null=False)
    ResponseTimeTimeMean = models.CharField(max_length=255, null=False)
    ResponseTimeTimeMedian = models.CharField(max_length=255, null=False)
    ResponseTimeTimeMode = models.CharField(max_length=255, null=False)
    ResponseTimeTimeSkewFromMedian = models.CharField(max_length=255, null=False)
    ResponseTimeTimeSkewFromMode = models.CharField(max_length=255, null=False)
    ResponseTimeTimeCoefficientofVariation = models.CharField(max_length=255, null=False)
    Label = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'flowData'


class shapData(models.Model):
    flowID = models.IntegerField(null=False)
    SourcePort_score = models.CharField(max_length=255, null=False)
    Duration_score = models.CharField(max_length=255, null=False)
    FlowBytesSent_score = models.CharField(max_length=255, null=False)
    FlowSentRate_score = models.CharField(max_length=255, null=False)
    FlowBytesReceived_score = models.CharField(max_length=255, null=False)
    FlowReceivedRate_score = models.CharField(max_length=255, null=False)
    PacketLengthVariance_score = models.CharField(max_length=255, null=False)
    PacketLengthStandardDeviation_score = models.CharField(max_length=255, null=False)
    PacketLengthMean_score = models.CharField(max_length=255, null=False)
    PacketLengthMedian_score = models.CharField(max_length=255, null=False)
    PacketLengthMode_score = models.CharField(max_length=255, null=False)
    PacketLengthSkewFromMedian_score = models.CharField(max_length=255, null=False)
    PacketLengthSkewFromMode_score = models.CharField(max_length=255, null=False)
    PacketLengthCoefficientofVariation_score = models.CharField(max_length=255, null=False)
    PacketTimeVariance_score = models.CharField(max_length=255, null=False)
    PacketTimeStandardDeviation_score = models.CharField(max_length=255, null=False)
    PacketTimeMean_score = models.CharField(max_length=255, null=False)
    PacketTimeMedian_score = models.CharField(max_length=255, null=False)
    PacketTimeMode_score = models.CharField(max_length=255, null=False)
    PacketTimeSkewFromMedian_score = models.CharField(max_length=255, null=False)
    PacketTimeSkewFromMode_score = models.CharField(max_length=255, null=False)
    PacketTimeCoefficientofVariation_score = models.CharField(max_length=255, null=False)
    ResponseTimeTimeVariance_score = models.CharField(max_length=255, null=False)
    ResponseTimeTimeStandardDeviation_score = models.CharField(max_length=255, null=False)
    ResponseTimeTimeMean_score = models.CharField(max_length=255, null=False)
    ResponseTimeTimeMedian_score = models.CharField(max_length=255, null=False)
    ResponseTimeTimeMode_score = models.CharField(max_length=255, null=False)
    ResponseTimeTimeSkewFromMedian_score = models.CharField(max_length=255, null=False)
    ResponseTimeTimeSkewFromMode_score = models.CharField(max_length=255, null=False)
    ResponseTimeTimeCoefficientofVariation_score = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'shapData'


class attackSource(models.Model):
    host = models.CharField(max_length=255, null=False)
    ip = models.CharField(max_length=255, null=False)
    port = models.CharField(max_length=255, null=False)
    protocol = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    organization = models.CharField(max_length=255, null=True)
    banner = models.TextField(null=True)

    class Meta:
        db_table = 'attackSource'


class Files(models.Model):
    filename = models.CharField(max_length=255, null=False, unique=True)
    filesize = models.CharField(max_length=255, null=False)
    sourceIp = models.CharField(max_length=255, null=False)
    sourcePort = models.CharField(max_length=255, null=False)
    destinationIp = models.CharField(max_length=255, null=False)
    destinationPort = models.CharField(max_length=255, null=False)
    tlsVersion = models.CharField(max_length=255, null=False)
    clientCipherSuits = models.TextField(null=True)
    serverAcceptedSuit = models.CharField(max_length=255, null=False)
    clientExtensions = models.TextField(null=True)
    serverExtensions = models.CharField(max_length=255, null=False)
    domain = models.CharField(max_length=255, null=False)
    tlsSession = models.CharField(max_length=255, null=False)
    packetLen = models.IntegerField()
    fingerPrint = models.CharField(max_length=255, null=False)
    

    class Meta:
        db_table = 'files'


class IP2Location(models.Model):
    ipFrom = models.PositiveIntegerField()
    ipTo = models.PositiveIntegerField()
    countryCode = models.CharField(max_length=10)
    countryName = models.CharField(max_length=255)
    regionName = models.CharField(max_length=255)
    cityName = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        db_table = 'ip2location'
