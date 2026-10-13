CC ?= cc
CFLAGS ?= -std=c11 -Wall -Wextra -Werror -pedantic -O2
.PHONY: test clean
test:
	$(CC) $(CFLAGS) -Iinclude src/pp_management.c tests/test_management.c -o test_management
	./test_management
clean:
	rm -f test_management
