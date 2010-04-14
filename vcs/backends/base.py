#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Marcin Kuzminski,Lukasz Balcerzak.  All rights reserved.
#
"""
Created on Apr 8, 2010

@author: marcink,lukaszb
"""

class BaseRepository(object):
    """
    Base Repository for final backends

    @attr repo: object from external api
    @attr revisions: list of all available revisions' ids
    @attr changesets: storage dict caching returned changesets
    @attr path: absolute local path to the repository
    """

    def __init__(self, repo_path, create=False, **kwargs):
        """
        Initializes repository. Raises RepositoryError if repository could
        not be find at the given ``repo_path``.

        @param repo_path: local path of the repository
        @param create=False: if set to True, would try to craete repository if
           it does not exist rather than raising exception
        """
        raise NotImplementedError

    def is_valid(self):
        """
        Validates repository.
        """
        raise NotImplementedError

    def get_owner(self):
        raise NotImplementedError

    def get_last_change(self):
        self.get_changesets(limit=1)

    def get_description(self):
        raise NotImplementedError

    def get_name(self):
        raise NotImplementedError

    #===========================================================================
    # CHANGESETS
    #===========================================================================
    def get_changeset(self, revision=None):
        """
        Returns instance of ``Changeset`` class. If ``revision`` is None, most
        recenent changeset is returned.
        """
        raise NotImplementedError

    def get_changesets(self, since=None, limit=None):
        """
        Returns all commits since given ``since`` parameter. If ``since`` is
        None it returns all commits limited by ``limit``, or all commits if
        ``limit`` is None.

        @param since: datetime
        @param limit: integer value for limit
        """
        raise NotImplementedError

    #===========================================================================
    # TAGS
    #===========================================================================
    def get_tags(self, since, limit):
        raise NotImplementedError

    def get_tag_by_name(self, tag_name):
        raise NotImplementedError

    def get_tag(self, tag_id):
        raise NotImplementedError

    #===========================================================================
    # BRANCHES
    #===========================================================================
    def get_branches(self, since, limit):
        raise NotImplementedError

    def get_branch_by_name(self, branch_name):
        raise NotImplementedError

    def get_branch(self, branch_id):
        raise NotImplementedError

    def get_files(self, limit):
        raise NotImplementedError

class BaseChangeset(object):
    """
    Each backend should implement it's changeset representation.

    @attr revision: revision number as integer
    @attr files: list of ``Node`` objects with NodeKind.FILE
    @attr dirs: list of ``Node`` objects with NodeKind.DIR
    @attr nodes: combined list of ``Node`` objects
    @attr author: author of the changeset
    @attr message: message of the changeset
    @attr size: integer size in bytes
    """

    def get_node(self, path):
        """
        Returns ``Node`` object from the given path.
        """
        raise NotImplementedError

    def get_root(self):
        """
        Returns ``RootNode`` object for this changeset.
        """
        return self.get_node('')

