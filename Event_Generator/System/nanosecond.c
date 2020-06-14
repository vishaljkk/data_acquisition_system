#include<stdio.h>
#include<time.h>
#include <math.h>
#include<stdlib.h>
int c_sleep_nsec(long nanoseconds) {
    struct timespec req;
    //struct timespec rem;
    if (nanoseconds > 999999999) {
      req.tv_sec = (int)(nanoseconds / 1000000000);
      req.tv_nsec = (nanoseconds - ((long)req.tv_sec * 1000000000));
    }
    else {
      req.tv_sec = 0;
      req.tv_nsec = nanoseconds;
    }
    //rem = NULL;
    return nanosleep(&req , NULL);
}

int main(int argc, char* argv[]) 
{
  int t=atoi(argv[1]);
  c_sleep_nsec(t);
  return 0;
}