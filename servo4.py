


#define LIGHTSEN_OUT 2  //gpio27 - J13 connect
#define COLLISION 3

int get_light_sensor();
int get_neardetect_sensor();

#define DBHOST "localhost"
#define DBUSER "root"
#define DBPASS "root"
#define DBNAME "demofarmdb"

MYSQL *connector;
MYSQL_RES *result;
MYSQL_ROW row;

int main (void)
{
  int adcChannel  = 0;
  int adcValue[8] = {0};

  if(wiringPiSetupGpio() == -1)
  {
    fprintf (stdout, "Unable to start wiringPi: %s\n", strerror(errno));
    return 1 ;
  }

  if(wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED) == -1) //아날로그를 디지털로 변환하는 부분인데 실제로 이 코드에서는 사용하고 있지 않습니다
  {
    fprintf (stdout, "wiringPiSPISetup Failed: %s\n", strerror(errno));
    return 1 ;
  }

  pinMode(CS_MCP3208, OUTPUT);

  // MySQL connection				//db붙이는 기능은 이 밑에 두줄 복사
  connector = mysql_init(NULL);
  if (!mysql_real_connect(connector, DBHOST, DBUSER, DBPASS, DBNAME, 3306, NULL, 0))
  {
    fprintf(stderr, "%s\n", mysql_error(connector));
    return 0;
  }

  printf("MySQL(rpidb) opened.\n");

  while(1) //sensor값을 수집하는 부분
  {
    char query[1024];
    adcValue[0] = get_light_sensor(); // Illuminance Sensor
	adcValue[1] = get_neardetect_sensor(); // neardetect Sensor

    //adcValue[7] = 27*pow((double)(adcValue[7]*VCC/4095), -1.10);

    sprintf(query,"insert into lab10 values (now(),%d,%d)", adcValue[0],adcValue[1]);

    if(mysql_query(connector, query))
    {
      fprintf(stderr, "%s\n", mysql_error(connector));
      printf("Write DB error\n");
    }

    delay(3000);
  }

  mysql_close(connector);

  return 0;
}


int wiringPicheck(void)
{
	if (wiringPiSetup () == -1)
	{
		fprintf(stdout, "Unable to start wiringPi: %s\n", strerror(errno));
		return 1 ;
	}
}

int get_light_sensor(void)
{
	// sets up the wiringPi library
	if (wiringPiSetup () < 0) 
	{
		fprintf (stderr, "Unable to setup wiringPi: %s\n", strerror (errno));
		return 1;
	}
	
	if(digitalRead(LIGHTSEN_OUT))	//day
		return 1;
	else //night
		return 0;
}

int get_neardetect_sensor(void)
{
    if (wiringPiSetup() < 0)
    {
        fprintf(stderr, "Unable to setup wiringPi: %s\n", strerror(errno));
        return 1;
    }

    if (digitalRead(COLLISION))
        retun 1;
    else
        return 0;
}
B
C
D
D
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
}
