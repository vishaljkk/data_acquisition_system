#include <stdio.h>
#include <math.h>
#include<stdlib.h>
#define PI 3.14159265358979323846
float guassian(int mean,int std,int x){
  float a=(1/(pow((2*PI),0.5)*std))*(exp(-pow((x-mean),2)/(2*pow(std,2))));
  return a;
}
int main(int argc, char* argv[]) {
  int mean=atoi(argv[1]);
  int std=atoi(argv[2]);
  int x1=atoi(argv[3]);
  int x2=atoi(argv[4]);
  FILE *fptr;
  if ((fptr = fopen("guassian.txt","w")) == NULL){
    printf("Error! opening file");
    exit(1);
  }
  for(int i=x1;i<=x2;i++){
    fprintf(fptr,"%d",i);
    fprintf(fptr,"\n");
    //fwrite(&i, sizeof(int), 1, fptr);
    float k=guassian(mean,std,i);
    fprintf(fptr,"%f",k);
    fprintf(fptr,"\n");
    //fwrite(&k, sizeof(float), 1, fptr);
    //printf("%f",k);
    //printf("\n");
  }
  fclose(fptr);

  return 0;
}
