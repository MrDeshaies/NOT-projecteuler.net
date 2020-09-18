#include "factorize.h"
#include <stdio.h>

int main(int argc, char const *argv[])
{
    int stopNumberDivisors = 500;
    int maxD=0;
    int maxT=0;

    int i = 1;
    int triangle = 0;
    while (1) {
        triangle += i;
        i++;

        struct factorization factors = factorize(triangle);
        int numDivisors = factors.current_size;
        dispose_factorization(&factors);
        if (numDivisors > maxD) {
            maxD = numDivisors;
            maxT = triangle;
            printf("%d : %d\n", triangle, numDivisors);
        }
        if (numDivisors >= stopNumberDivisors)
            break;
    }
    return 0;
}
