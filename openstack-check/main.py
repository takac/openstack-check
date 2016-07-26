from __future__ import print_function

import argparse

from stevedore import extension

if __name__ == '__main__':
    # create the top-level parser
    parser = argparse.ArgumentParser(prog='openstack-check')
    parser.add_argument('--foo', action='store_true', help='foo help')
    subparsers = parser.add_subparsers(help='sub-command help')

    mgr = extension.ExtensionManager(
        namespace='openstack.check',
    )

    for i in mgr:
        # pass in subparser to plugin
        i.plugin(subparsers)

    parsed_args = parser.parse_args()
    parsed_args.func(parsed_args)
