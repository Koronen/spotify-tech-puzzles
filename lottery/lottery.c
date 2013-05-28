#include <stdio.h>
#include <math.h>

double lottery(
    const unsigned int m,
    const unsigned int n,
    const unsigned int t,
    const unsigned int p)
{
    return 0;
}

int main()
{
    unsigned int m, n, t, p;
    if(!scanf("%d %d %d %d", &m, &n, &t, &p)) return 1;

    printf("%lf\n", lottery(n, m, t, p));

    return 0;
}
