DST_DIR=${HOME}/bin

install: add_article.py
	mkdir -p ${DST_DIR}
	cp $< ${DST_DIR}
	chmod u+x ${DST_DIR}/$<
