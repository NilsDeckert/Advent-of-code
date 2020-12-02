#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    char *file_name = "input.txt";
    int numOf;
    int counter = 0;
    int numbers[200];
    FILE *fp;

    fp = fopen(file_name, "r");
    if (fp==NULL){
        perror("Error opening the file\n");
        exit(-1);
    }

    while (counter < 200){
        fscanf(fp, "%d", &numOf);
        numbers[counter] = numOf;
        counter++;
    }
    for(int i=0; i<200; i++){
        for(int j = 0; j<(200-1); j++){
            //printf("%d + %d = %d\n", numbers[i], numbers[j], numbers[i]+numbers[j]);
            if(numbers[i] + numbers[j] == 2020){
                printf("%d + %d = 2020\n", numbers[i], numbers[j]);
                printf("%d * %d = %d\n", numbers[i], numbers[j], numbers[i]*numbers[j]);
                exit(0);
            }
        }
    }

    fclose(fp);
    return 0;
}
