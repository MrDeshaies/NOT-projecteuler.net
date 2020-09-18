
#include <stdlib.h>
#include <stdio.h>
#include "factorize.h"


/**
 * Initialize a factorization structure. Be sure to call
 * dispose_factorization() when you're done to de-allocate
 */
struct factorization initialize_factorization(int initial_size) {
    struct factorization result;
    result.allocated_size = initial_size;
    result.factors = (int*)malloc(initial_size * sizeof(int));
    result.current_size = 0;
    return result;
}

void add_factor(struct factorization *list, int value) {
    if (list->allocated_size <= list->current_size) {
        list->factors = (int*)realloc(list->factors, 2*list->allocated_size*sizeof(int));
        list->allocated_size *= 2;
    }

    list->factors[list->current_size] = value;
    list->current_size++;
}

void dispose_factorization(struct factorization *list) {
    free(list->factors);
}

/**
 * Comparator for integers to use with qsort()
 */
int int_comp (const void * elem1, const void * elem2) 
{
    int f = *((int*)elem1);
    int s = *((int*)elem2);
    if (f > s) return  1;
    if (f < s) return -1;
    return 0;
}

void sort_factors(struct factorization *x) {
    qsort(x->factors, x->current_size, sizeof(int), int_comp);
}

int min(int x, int y) {
    if (x<y)
        return x;
    return y;
}

struct factorization factorize(int number) {
    struct factorization result = initialize_factorization(100);
    int i = 1;

    // hardcode a new numbers as the math below only works for number > 4
    switch(number){
        case 1:
            add_factor(&result, 1);
            break;
        case 2:
            add_factor(&result, 1);
            add_factor(&result, 2);
            break;
        case 3:
            add_factor(&result, 1);
            add_factor(&result, 3);
            break;
        case 4:
            add_factor(&result, 1);
            add_factor(&result, 2);
            add_factor(&result, 4);
            break;
    }
    if (result.current_size != 0) {
        return result;
    }
    
    int maxPossibleFactor = number / 2;
    if (number % 2 == 1)
        maxPossibleFactor++;
    while (i < maxPossibleFactor) {
        if (number % i == 0) {
            add_factor(&result, i);
            int x = number / i;
            if (x != i)
                add_factor(&result, x);
            maxPossibleFactor = min(maxPossibleFactor,x);
        }
        i++;
    }

    sort_factors(&result);
    return result;
}



/*
int main(int argc, char const *argv[])
{
    struct factorization result = factorize(1);
    dispose_factorization(&result);
    result = factorize(2);
    dispose_factorization(&result);
    printf("Success\n\n\n\n");

    // struct int_array_list result = factorize(24);
    // printf("Factorization of 24 is [");
    // for (int i = 0; i < result.current_size; i++) {
    //     printf("%d ", result.values[i]);
    // }
    // printf("]\n");
    return 0;
}*/