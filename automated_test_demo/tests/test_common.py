
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo.tests import common
from odoo.exceptions import AccessError, ValidationError, Warning
from odoo.tests.common import users

_logger = logging.getLogger(__name__)


class TestProjectCustom(common.TransactionCase):
    def setUp(self):
        super(TestProjectCustom, self).setUp()

        self.user_group_employee = self.env.ref('base.group_user')
        self.user_group_project_user = self.env.ref('project.group_project_user')
        self.user_group_project_manager = self.env.ref('project.group_project_manager')

        Users = self.env['res.users']
        self.internal_user_id = Users.with_context(no_reset_password=True).create({
            'name': 'Internal User Test',
            'login': 'internal_user_test',
            'email': 'innernal_user_test@gmail.com',
            # 'mobile': '081294224788',
            'groups_id': [(6, 0, [self.user_group_employee.id])]
        })

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
        self.assertEqual(test_project.name, 'TestProject11')
        # Do a little print to show it visually for this demo - in production you don't really need this.
        _logger.info('Your test_create_data was succesfull!')

    def test_001_check_username_equal(self):
        self.assertEqual(self.internal_user_id.name, 'Internal User Test')
        _logger.info('Your test_001_check_username_equal was succesfull!')

    def test_002_check_username_not_equal(self):
        self.assertNotEqual(self.internal_user_id.name, 'Arkana')
        _logger.info('Your test_002_check_username_not_equal was succesfull!')

    def test_003_check_login_is_set(self):
        self.assertIsNotNone(self.internal_user_id.login)
        _logger.info('Your test_003_check_login_is_set was succesfull!')

    def test_003_check_login_is_not_set(self):
        self.assertIsNotNone(self.internal_user_id.login)
        _logger.info('Your test_003_check_login_is_not_set was succesfull!')

    def test_004_check_mobile_is_set(self):
        self.assertIsNotNone(self.internal_user_id.mobile)
        _logger.info('Your test_004_check_mobile_is_set was succesfull!')

    def test_005_check_if_user_has_group(self):
        self.assertIn(
            self.user_group_employee.id, self.internal_user_id.groups_id.ids)
        _logger.info('Your test_005_check_if_user_has_group was succesfull!')

    def test_006_check_if_login_only_contain_character(self):
        self.assertIsInstance(self.internal_user_id.login, str)
        _logger.info('Your test_006_check_if_login_only_contain_character was succesfull!')
        
    # def check_user_persmission_to_create_project(self):
        # with self.assertRaises(AccessError) as e:
        #     self.env['project.project'].with_user(internal_user_id).create({
        #         "name": "Internal User Project",
        #     })
        # print('Your test_001_create_data_from_internal_user was succesfull!')
