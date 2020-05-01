################################################################################
# The Pyretic Project                                                          #
# frenetic-lang.org/pyretic                                                    #
# author: Joshua Reich (jreich@cs.princeton.edu)                               #
################################################################################
# Licensed to the Pyretic Project by one or more contributors. See the         #
# NOTICES file distributed with this work for additional information           #
# regarding copyright and ownership. The Pyretic Project licenses this         #
# file to you under the following license.                                     #
#                                                                              #
# Redistribution and use in source and binary forms, with or without           #
# modification, are permitted provided the following conditions are met:       #
# - Redistributions of source code must retain the above copyright             #
#   notice, this list of conditions and the following disclaimer.              #
# - Redistributions in binary form must reproduce the above copyright          #
#   notice, this list of conditions and the following disclaimer in            #
#   the documentation or other materials provided with the distribution.       #
# - The names of the copyright holds and contributors may not be used to       #
#   endorse or promote products derived from this work without specific        #
#   prior written permission.                                                  #
#                                                                              #
# Unless required by applicable law or agreed to in writing, software          #
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT    #
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the     #
# LICENSE file distributed with this work for specific language governing      #
# permissions and limitations under the License.                               #
################################################################################

from pyretic.lib.corelib import *
from pyretic.lib.std import *
import csv
import os

# insert the name of the module and policy you want to import
from pyretic.examples.pyretic_switch import act_like_switch

policy_file = "%s/pyretic/pyretic/examples/firewall-policies.csv" % os.environ[ 'HOME' ]

def main():
    with open(policy_file,'r') as f:
        reader = csv.reader(f)
        # start with a policy that doesn't match any packets
        not_allowed = none
        # and add traffic that isn't allowed
        for i in reader:
            not_allowed = not_allowed + (match(srcmac=MAC(i[1]))&match(dstmac=MAC(i[2]))) + (match(srcmac=MAC(i[2]))&match(dstmac=MAC(i[1])))

        # express allowed traffic in terms of not_allowed - hint use '~'
        allowed = ~not_allowed

        # and only send allowed traffic to the mac learning (act_like_switch) logic
        return allowed >> act_like_switch()



