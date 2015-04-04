prefix ?= /usr
datadir ?= $(prefix)/share
sysconfdir ?= /etc

ELM_PROFILE ?= mobile
PROFILE_DIR = $(DESTDIR)/$(sysconfdir)/profile.d/
CONFIG_DIR = $(DESTDIR)/$(datadir)/elementary/config/$(ELM_PROFILE)

INSTALL = install -c
EET_EET = eet

all:
	cd config && \
		$(EET_EET) -e base.cfg config base.src 1; \
	cd - ;

clean:
	cd config && \
		rm -rf *.cfg
	cd - ;

install:
	mkdir -p $(PROFILE_DIR) $(CONFIG_DIR) && \
	$(INSTALL) profile.d/*.sh $(PROFILE_DIR) && \
	$(INSTALL) config/*.cfg $(CONFIG_DIR) && \
	$(INSTALL) config/profile.desktop $(CONFIG_DIR) && \
	$(INSTALL) config/icon.png $(CONFIG_DIR) ; \
