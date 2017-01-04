#!/usr/bin/env python


"""kcm.

Usage:
  kcm (-h | --help)
  kcm --version
  kcm init [--conf-dir=<dir>] [--num-dp-cores=<num>] [--num-cp-cores=<num>]
  kcm describe [--conf-dir=<dir>]
  kcm reconcile [--conf-dir=<dir>]
  kcm isolate [--conf-dir=<dir>] --pool=<pool> <command> [-- <args> ...]
  kcm install --install-dir=<dir>

Options:
  -h --help             Show this screen.
  --version             Show version.
  --conf-dir=<dir>      KCM configuration directory [default: /etc/kcm].
  --install-dir=<dir>   KCM install directory.
  --num-dp-cores=<num>  Number of data plane cores [default: 4].
  --num-cp-cores=<num>  Number of control plane cores [default: 1].
  --pool=<pool>         Pool name: either infra, controlplane or dataplane.
"""
from intel import describe, init, install, isolate, reconcile
from docopt import docopt
import logging


def main():
    logging.basicConfig(level=logging.INFO)
    args = docopt(__doc__, version="KCM 0.1.0")
    if args["init"]:
        init.init(args["--conf-dir"],
                  args["--num-dp-cores"],
                  args["--num-cp-cores"])
        return
    if args["describe"]:
        describe.describe(args["--conf-dir"])
        return
    if args["isolate"]:
        isolate.isolate(args["--conf-dir"], args["--pool"],
                        args["<command>"], args["<args>"])
        return
    if args["reconcile"]:
        reconcile.reconcile(args["--conf-dir"])
        return
    if args["install"]:
        install.install(args["--install-dir"])
        return


if __name__ == "__main__":
    main()