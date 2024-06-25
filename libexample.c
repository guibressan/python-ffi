#include "libexample.h"

long libexample_iter(long n) {
	long r = 0;
	for (;n;) {
		r += n;
		n--;
	}
	return r;
}

