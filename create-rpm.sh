#!/bin/sh
NAME=hello
VERSION=0.1

rm -rf rpmbuild
mkdir rpmbuild
mkdir rpmbuild/SOURCES
mkdir rpmbuild/SPEC
cp $NAME.spec rpmbuild/SPEC
mkdir rpmbuild/TMP
mkdir rpmbuild/TMP/$NAME-$VERSION
cp *.sh rpmbuild/TMP/$NAME-$VERSION/.
rm rpmbuild/TMP/$NAME-$VERSION/create-rpm.sh

cd rpmbuild/TMP
tar cvzf ../SOURCES/$NAME-$VERSION.tar.gz $NAME-$VERSION

cd ..
rpmbuild --define "_topdir ${PWD}" -ba SPEC/$NAME.spec
