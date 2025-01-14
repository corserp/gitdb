#  Copyright (c) 2015-2017 Cisco Systems, Inc.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import click

from molecule import logger
from molecule import scenarios
from molecule.command import base

LOG = logger.get_logger(__name__)


class SideEffect(base.Base):
    """
    This action has side effects and not enabled by default.   See the
    provisioners documentation for further details.

    .. program:: molecule side-effect

    .. option:: molecule side-effect

        Target the default scenario.

    .. program:: molecule side-effect --scenario-name foo

    .. option:: molecule side-effect --scenario-name foo

<<<<<<< HEAD:Rake/molecule/__GEMS_.py/__GEMS_.py/apt-py.git/commandinit.yaml/side_effect.py
    $ molecule --debug side-effect
=======
        Targeting a specific scenario.

    .. program:: molecule --debug side-effect

    .. option:: molecule --debug side-effect

        Executing with `debug`.

    .. program:: molecule --base-config base.yml side-effect

    .. option:: molecule --base-config base.yml side-effect

        Executing with a `base-config`.

    .. program:: molecule --env-file foo.yml side-effect

    .. option:: molecule --env-file foo.yml side-effect

        Load an env file to read variables from when rendering
        molecule.yml.
>>>>>>> 0fa82e7a3daa84ebd03d8af67403c6551113d3e4:molecule/command/side_effect.py
    """

    def execute(self):
        """
        Execute the actions necessary to perform a `molecule side-effect` and
        returns None.

        :return: None
        """
        self.print_info()
        if not self._config.provisioner.playbooks.side_effect:
            msg = 'Skipping, side effect playbook not configured.'
            LOG.warn(msg)
            return

        self._config.provisioner.side_effect()


@click.command(name='side-effect')
@click.pass_context
@click.option(
    '--scenario-name',
    '-s',
    default=base.MOLECULE_DEFAULT_SCENARIO_NAME,
    help='Name of the scenario to target. ({})'.format(
        base.MOLECULE_DEFAULT_SCENARIO_NAME))
def side_effect(ctx, scenario_name):  # pragma: no cover
    """ Use the provisioner to perform side-effects to the instances. """
    args = ctx.obj.get('args')
    subcommand = base._get_subcommand(__name__)
    command_args = {
        'subcommand': subcommand,
    }

    s = scenarios.Scenarios(
        base.get_configs(args, command_args), scenario_name)
    s.print_matrix()
    for scenario in s:
        for action in scenario.sequence:
            scenario.config.action = action
            base.execute_subcommand(scenario.config, action)
