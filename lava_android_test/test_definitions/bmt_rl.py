# Copyright (c) 2015 Micron
#
# Author: Henry Jung <henryjung@micron.com>
#
# This file is part of LAVA Android Test.
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
**Default options:** None
"""

import lava_android_test.testdef
import os
import re

test_name = 'bmt_rl'

DEFAULT_OPTIONS='output all'

cur_dir = os.path.realpath(os.path.dirname(__file__))
asset_dir = 'micron/bmt/rl/'
target_dir = '/data/local/tmp/'

main_activity = 'com.redlicense.benchmark.sqlite/.Main'
uiauto_jar = 'RLTest.jar'
uiauto_class = 'com.micron.mbu.bmt.RLTest'

INSTALL_STEPS_ADB_PRE = [ 'push %s/%s %s' % (cur_dir, asset_dir, target_dir) ]
RUN_STEPS_ADB_PRE = [ 'logcat -c', 'shell am start -n %s' % main_activity ]
RUN_ADB_SHELL_STEPS = [ 'uiautomator runtest %s -c %s' % (uiauto_jar, uiauto_class) ]
RUN_STEPS_ADB_POST = [ 'logcat -d | grep \"RL Test\"' ]

#PATTERN = "^\s*(?P<test_case_id>.*?)\s*:\s*(?P<result>\w+)\s*$"
PATTERN = "^.*:\s(?P<test_case_id>\w+)\s*:\s*(?P<measurement>\w+\.\w+)"

inst = lava_android_test.testdef.AndroidTestInstaller(
                                steps_adb_pre=INSTALL_STEPS_ADB_PRE)
run = lava_android_test.testdef.AndroidTestRunner(
                                    steps_adb_pre=RUN_STEPS_ADB_PRE,
                                    adbshell_steps=RUN_ADB_SHELL_STEPS,
                                    steps_adb_post=RUN_STEPS_ADB_POST)
parser = lava_android_test.testdef.AndroidTestParser(PATTERN)
testobj = lava_android_test.testdef.AndroidTest(testname=test_name,
                                    installer=inst,
                                    runner=run,
                                    parser=parser,
                                    default_options=DEFAULT_OPTIONS)
