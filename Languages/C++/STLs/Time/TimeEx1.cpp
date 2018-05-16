#include <stdio.h>  
#include <time.h>       
int main ()
{
  struct tm start_date;
  struct tm end_date;
  time_t start_time, end_time;
  double seconds;

  start_date.tm_hour = 0;  start_date.tm_min = 0;  start_date.tm_sec = 0;
  start_date.tm_mon = 10; start_date.tm_mday = 15; start_date.tm_year = 113;

  end_date.tm_hour = 0;  end_date.tm_min = 0;  end_date.tm_sec = 0;
  end_date.tm_mon = 10; end_date.tm_mday = 20; end_date.tm_year = 113;

  start_time = mktime(&start_date);
  end_time = mktime(&end_date);

  seconds = difftime(end_time, start_time);

  printf ("%.f seconds difference\n", seconds);
  

  return 0;
}
