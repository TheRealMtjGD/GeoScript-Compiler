#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void help() {
    FILE *rbuff = fopen("../README.md", "r");
    char data[600];
    fgets(data, 600, rbuff);
    printf("%s", data);

    usage();
}

void usage() {
    printf("usage: geoscript -c [FileName] [LevelName]\n");
    printf("       geoscript -c [FileName] -gso\n");
    printf("       geoscript -c [FileName] -lib\n");
    printf("       geoscript -c [FileName] -raw\n");
    printf("       geoscript --help\n");
    printf("       geoscript --version\n");
    printf("       geoscript --usage\n");
}

void version() {
    printf("GeoScript 1.0.0 | Windows-Python-x64 CRLF\n");
}


int main(int argc, const char *argv[]) {
    if (argc == 1) {
        usage();
    } else if (argc == 2) {
        if (strcmp(argv[1], "--help")) {
            help();
        } else if (strcmp(argv[1], "--usage")) {
            usage();
        } else if (strcmp(argv[1], "--version")) {
            version();
        } else {
            printf("Fatal Error: Unidentified argument %s\n", argv[2]);
            exit(1);
        }
    } else if (argc == 4) {
        if (strcmp(argv[2], "-c")) {
            if (strcmp(argv[4], "-gso")) {
                system("python ../geoscript.py [name] gso");
            } else if (strcmp(argv[4], "-lib")) {
                system("python ../geoscript.py [name] lib");
            } else if (strcmp(argv[4], "-raw")) {
                system("python ../geoscript.py [name] raw");
            } else {
                system("python ../geoscript.py [name] [level]");
            }
        }
    }
}