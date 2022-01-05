# ----------------------------------------------------------------------------
# Copyright (c) 2018-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import sys

# README:
# conda activate q2dev
#
# This script takes three positional arguments:
# argv[1]: a filepath to read package names from
# argv[2]: a filepath to write the badges to
# argv[3]: the branch name


def read_packages(names_fp):
    # this is a bit gross, but it works
    package_names, level = [], None
    with open(names_fp) as fh:
        for line in fh:
            val = line.strip()
            if val == '':
                if level is not None:
                    package_names.append(level)
                level = []
            else:
                level.append(val)
        if level:
            package_names.append(level)
    return package_names


def write_badges(fp_badges, package_names, branch):
    with open(fp_badges, 'w') as fh:
        for i, level in enumerate(package_names):
            fh.write('### level: %d\n\n' % i)
            for name in level:
                fh.write(
                    '[![ci](https://github.com/qiime2/%s/actions/workflows/'
                    'ci.yml/badge.svg?branch=%s&event=push) %s]'
                    '(https://github.com/qiime2/%s/actions/workflows/'
                    'ci.yml?query=branch%%3A%s)\n\n' % (name,
                                                        branch,
                                                        name,
                                                        name,
                                                        branch))


if __name__ == '__main__':
    fp_package_names = sys.argv[1]
    package_names = read_packages(fp_package_names)

    fp_badges = sys.argv[2]
    branch_name = sys.argv[3]
    write_badges(fp_badges, package_names, branch_name)
