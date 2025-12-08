FROM postgres:18

# Criar locale pt_BR.UTF-8
RUN localedef -i pt_BR -c -f UTF-8 -A /usr/share/locale/locale.alias pt_BR.UTF-8

ENV LANG=pt_BR.UTF-8
ENV LC_ALL=pt_BR.UTF-8
ENV POSTGRES_PASSWORD=MYPASSWORD123
ENV POSTGRES_USER=SYSPOSTGRES
ENV POSTGRES_DB=DATABASE_ANIME

COPY /docker_database/scripts_iniciais/ /docker-entrypoint-initdb.d/

VOLUME /animes/database/DB_VOLUME

EXPOSE 5433
