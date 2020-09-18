struct factorization {
    int *factors;
    int allocated_size;
    int current_size;
};

struct factorization factorize(int number);
void dispose_factorization(struct factorization *list);