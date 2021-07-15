# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tests import tagged
from odoo.exceptions import AccessError, ValidationError
from odoo.addons.automated_test_demo.tests.test_common import TestProjectCustom


class TestProjectCustom(TestProjectCustom):
    # def setUp(self):
    #     super().setUp()

    def test_create_data(self):
        # Create a new project with the test
        test_project = self.env['project.project'].create({
            'name': 'TestProject'
        })

        # Add a test task to the project
        test_project_task = self.env['project.task'].create({
            'name': 'ExampleTask',
            'project_id': test_project.id
        })

        # Check if the project name and the task name match
        self.assertEqual(test_project.name, 'TestProject')
        self.assertEqual(test_project_task.name, 'ExampleTask')
        # Check if the project assigned to the task is in fact the correct id
        self.assertEqual(test_project_task.project_id.id, test_project.id)
        # Check if failed
        self.assertEqual(test_project.name, 'TestProject')
        # Do a little print to show it visually for this demo - in production you don't really need this.
        print('Your test was succesfull!')

    def test_001_create_data_from_internal_user(self):
        user = self.internal_user_id
        with self.assertRaises(AccessError, msg="%s should not be able to create a task" % user.name):
            self.env['project.project'].with_user(user).create({
                "name": "Internal User Project",
            })
        print('Your test_001_create_data_from_internal_user was succesfull!')
