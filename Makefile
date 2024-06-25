CC = cc
CFLAGS = -O2 -Wall -std=c99

.PHONY: clean

build: libexample.so

libexample.so: libexample.c libexample.h
	$(CC) $(CFLAGS) -o $@ -shared -fPIC $<

clean:
	@rm libexample.so 1>/dev/null 2>&1 || true
