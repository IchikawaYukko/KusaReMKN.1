CC=	cc
CFLAGS=	-O
RM=	rm -rf
RPMBUILD=rpmbuild

all: KusaReMKN data

KusaReMKN: kusaremkn.c
	$(CC) $(CFLAGS) -o KusaReMKN kusaremkn.c

data: mkdata.sh
	sh mkdata.sh

rpm: KusaReMKN kusaremkn.spec
	# To install dependenciesm run:
	#   dnf install install -y git make gcc ncurses-devel rpm-build
	export SRC_ROOT=$(shell pwd) && $(RPMBUILD) -D "_topdir $(shell pwd)/rpmbuild" -D "_commit_id $(shell git log -1 --oneline|cut -b -7)" -ba kusaremkn.spec

.PHONY: clean
clean:
	$(RM) KusaReMKN data temp rpmbuild
