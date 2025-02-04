# -*- coding: utf-8 -*-
"""
    mackerel.host
    ~~~~~~~~~~~~~

    Mackerel client implemented by Python.

    Ported from `mackerel-client-ruby`.
    <https://github.com/mackerelio/mackerel-client-ruby>

    :copyright: (c) 2014 Hatena, All rights reserved.
    :copyright: (c) 2015 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import re


class Host(object):
    MACKEREL_INTERFACE_NAME_PATTERN = re.compile(r'^eth\d')

    def __init__(self, **kwargs):
        """Construct a host.

        :param name: Host name
        :param display_name: Host display name
        :param meta: Host metadata
        :param type: Host type
        :param status: Host status
        :param memo: Host memo
        :param is_retired: Retired flag
        :param id: Host id
        :param created_at: Created datetime
        :param roles: Host roles
        :param interfaces: Host interfaces
        """
        self.args = kwargs
        self.name = kwargs.get('name', None)
        self.display_name = kwargs.get('displayName', None)
        self.meta = kwargs.get('meta', None)
        self.type = kwargs.get('type', None)
        self.status = kwargs.get('status', None)
        self.memo = kwargs.get('memo', None)
        self.is_retired = kwargs.get('isRetired', None)
        self.id = kwargs.get('id', None)
        self.created_at = kwargs.get('createdAt', None)
        self.roles = kwargs.get('roles', None)
        self.interfaces = kwargs.get('interfaces', None)

    def ip_addr(self):
        """Get ipaddress."""
        for i in self.interfaces:
            if self.MACKEREL_INTERFACE_NAME_PATTERN.search(i['name']):
                return i['ipAddress']

    def mac_addr(self):
        """Get MAC address."""
        for i in self.interfaces:
            if self.MACKEREL_INTERFACE_NAME_PATTERN.search(i['name']):
                return i['macAddress']

    def __repr__(self):
        repr = '<Host('
        repr += 'name={0}, display_name={1}, meta={2}, type={3}, status={4},'
        repr += 'memo={5}, is_retired={6}, id={7}, created_at={8}, roles={9},'
        repr += 'interfaces={10})'
        return repr.format(self.name, self.display_name, self.meta, self.type,
                           self.status, self.memo, self.is_retired, self.id,
                           self.created_at, self.roles, self.interfaces)
