BIN_DIR=~/bin
SRC_SCRIPT=add_article.py
DST_SCRIPT=$(BIN_DIR)/add_article

all:
	@echo "If you want to install this script, run 'make install'."

${BIN_DIR}:
	mkdir -p $@

install: $(SRC_SCRIPT) ${BIN_DIR}

	cp $< $(DST_SCRIPT)
	chmod u+x $(DST_SCRIPT)

clean:
ifneq (, $(wildcard $(DST_SCRIPT)))
	rm $(DST_SCRIPT)
endif
