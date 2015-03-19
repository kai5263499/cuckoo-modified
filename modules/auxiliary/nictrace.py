# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import os
import logging
import shutil

from lib.cuckoo.common.abstracts import Auxiliary
from lib.cuckoo.common.constants import CUCKOO_ROOT

log = logging.getLogger(__name__)

class NicTrace(Auxiliary):
    def start(self):
        return

    def stop(self):
        """Move nictrace file.
        @return: operation status.
        """

        file_path = os.path.join(CUCKOO_ROOT, "storage", "analyses", str(self.task.id), "dump.pcap")
        orig_pcap = "%s/%s.pcap" % (self.options.get("pcapdir"), self.machine.label)
        log.debug("nictrace moving %s -> %s" % (orig_pcap,file_path))
        shutil.move(orig_pcap,file_path)