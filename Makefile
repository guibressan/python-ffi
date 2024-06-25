.PHONY: clean

build: libexample.so

libexample.so: libexample.c libexample.h
	cc -o $@ -shared -fPIC $<

clean:
	@rm libexample.so 1>/dev/null 2>&1 || true
