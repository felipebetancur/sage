- David Roe, Frej Drejhammar, Julian Rueth, Martin Raum, Nicolas M. Thiery, R.
  Andrew Ohana, Robert Bradshaw, Timo Kluck: initial version
#       Copyright (C) 2013 David Roe <roed.math@gmail.com>
#                          Frej Drejhammar <frej.drejhammar@gmail.com>
#                          Julian Rueth <julian.rueth@fsfe.org>
#                          Martin Raum <martin@raum-brothers.eu>
#                          Nicolas M. Thiery <Nicolas.Thiery@u-psud.fr>
#                          R. Andrew Ohana <andrew.ohana@gmail.com>
#                          Robert Bradshaw <robertwb@gmail.com>
#                          Timo Kluck <tkluck@infty.nl>
from sage.env import SAGE_VERSION

MASTER_BRANCH = "master"
            self.git = GitInterface(self.config['git'], self._UI, self.upload_ssh_key)
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev.git.silent.commit(allow_empty=True, message="second commit")
            sage: dev.trac._connected = True
            sage: dev.git.super_silent.checkout('HEAD', detach=True)
            sage: UI.append("Summary: ticket detached\ndescription")
            sage: dev.create_ticket()
            6
            sage: dev.git.current_branch()
            'ticket/6'
            sage: dev.git.super_silent.checkout('-b','merge_branch')
            sage: with open('merge', 'w') as f: f.write("version 0")
            sage: dev.git.silent.add('merge')
            sage: dev.git.silent.commit('-m','some change')
            sage: dev.git.super_silent.checkout('ticket/6')
            sage: with open('merge', 'w') as f: f.write("version 1")
            sage: dev.git.silent.add('merge')
            sage: dev.git.silent.commit('-m','conflicting change')
            sage: from sage.dev.git_error import GitError
            sage: try:
            ....:     dev.git.silent.merge('merge_branch')
            ....: except GitError: pass
            sage: UI.append("n")
            sage: UI.append("Summary: ticket merge\ndescription")
            sage: dev.create_ticket()
            Your repository is in an unclean state. It seems you are in the middle of a merge of some sort. To run this command you have to reset your respository to a clean state. Do you want me to reset your respository? (This will discard many changes which are not commited.) [yes/No] n
            Could not switch to branch ticket/7 because your working directory is not clean.
            sage: dev.git.reset_to_clean_state()
            sage: open('tracked', 'w').close()
            sage: dev.git.silent.add('tracked')
            sage: UI.append("keep")
            sage: UI.append("Summary: ticket merge\ndescription")
            sage: dev.create_ticket()
            The following files in your working directory contain uncommitted changes:
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? [discard/Keep/stash] keep
            Could not switch to branch ticket/8 because your working directory is not clean.
            base = self._current_ticket()
        self.git.silent.branch(branch, base)
            self.git.silent.branch(branch, delete=True)
            self._UI.info("Your ticket has been created on trac. However, an error ocurred while switching to your new branch {0}. Use {1} to manually switch to {0}.".format(branch,self._format_command("switch_ticket",str(ticket))))
            sage: from sage.dev.test.sagedev import two_user_setup
            sage: alice, config_alice, bob, config_bob, server = two_user_setup()
            sage: bob.git.super_silent.commit(allow_empty=True,message="empty commit")
            sage: bob._UI.append("y")
            The branch u/bob/ticket/1 does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            sage: alice.git.echo.log('--pretty=%s')
            sage: alice.git.super_silent.checkout('HEAD', detach=True)
            sage: alice.git.super_silent.branch('-d','ticket/1')
            sage: alice.git.echo.log('--pretty=%s')
            sage: alice.git.echo.log('--pretty=%s')
            sage: alice.git.echo.log('--pretty=%s')
            sage: alice.git.super_silent.add("untracked")
            sage: alice.git.super_silent.commit(message="added untracked")
            sage: alice.git.super_silent.add("tracked")
            The following files in your working directory contain uncommitted changes:
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? [discard/Keep/stash] d
            self.git.silent.branch(branch, MASTER_BRANCH)
            self.git.silent.branch("-d",branch)
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev.git.silent.branch("branch1")
            sage: dev.git.silent.branch("branch2")
            sage: dev.git.silent.add("tracked")
            sage: dev.git.silent.commit(message="added tracked")
            sage: UI.append("keep")
            The following files in your working directory contain uncommitted changes:
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? [discard/Keep/stash] keep
            sage: UI.append("s")
            The following files in your working directory contain uncommitted changes:
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? [discard/Keep/stash] s
            stash/1
            sage: UI.append("d")
            The following files in your working directory contain uncommitted changes:
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? [discard/Keep/stash] d
            sage: dev.git.super_silent.checkout('-b','merge_branch')
            sage: with open('merge', 'w') as f: f.write("version 0")
            sage: dev.git.silent.add('merge')
            sage: dev.git.silent.commit('-m','some change')
            sage: dev.git.super_silent.checkout('branch1')
            sage: with open('merge', 'w') as f: f.write("version 1")
            sage: dev.git.silent.add('merge')
            sage: dev.git.silent.commit('-m','conflicting change')
            sage: from sage.dev.git_error import GitError
            sage: try:
            ....:     dev.git.silent.merge('merge_branch')
            ....: except GitError: pass
            sage: UI.append('n')
            sage: dev.switch_branch('merge_branch')
            Your repository is in an unclean state. It seems you are in the middle of a merge of some sort. To run this command you have to reset your respository to a clean state. Do you want me to reset your respository? (This will discard many changes which are not commited.) [yes/No] n
            Could not switch to branch merge_branch because your working directory is not clean.
            sage: dev.git.reset_to_clean_state()

        Switching branches when in a detached HEAD::

            sage: dev.git.super_silent.checkout('branch2', detach=True)
            sage: dev.switch_branch('branch1')

        With uncommitted changes::

            sage: dev.git.super_silent.checkout('branch2', detach=True)
            sage: with open('tracked', 'w') as f: f.write("boo")
            sage: UI.append("discard")
            sage: dev.switch_branch('branch1')
            The following files in your working directory contain uncommitted changes:
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? [discard/Keep/stash] discard
            sage: with open('tracked', 'w') as f: f.write("boo")
            sage: dev.switch_branch('branch2')
            GitError: git exited with a non-zero exit code (1).
            This happened while executing `git checkout branch2`.
            git printed nothing to STDOUT.
            git printed the following to STDERR:
            error: The following untracked working tree files would be overwritten by checkout:
                tracked
            Please move or remove them before you can switch branches.
            Aborting
            self.git.super_silent.checkout(branch)
    def download(self, ticket_or_remote_branch=None, branch=None):
        Download ``ticket_or_remote_branch`` to ``branch``.
        - ``ticket_or_remote_branch`` -- a string or an integer or ``None`` (default:
            sage: from sage.dev.test.sagedev import two_user_setup
            sage: alice, config_alice, bob, config_bob, server = two_user_setup()
            sage: alice.git.super_silent.commit(allow_empty=True, message="alice: empty commit")
            sage: alice._UI.append("y")
            The branch u/alice/ticket/1 does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            sage: bob.git.echo.log('--pretty=%s')
            sage: bob.git.silent.add("bobs_file")
            sage: bob.git.super_silent.commit(message="bob: added bobs_file")
            sage: bob._UI.append("y")
            sage: bob._UI.append("y")
            The branch u/bob/ticket/1 does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            I will now change the branch field of ticket #1 from its current value `u/alice/ticket/1` to `u/bob/ticket/1`. Is this what you want? [Yes/no] y
            sage: alice.git.silent.add("alices_file")
            sage: alice.git.super_silent.commit(message="alice: added alices_file")
            sage: alice.git.echo.log('--pretty=%s')
            sage: bob.git.silent.add("alices_file")
            sage: bob.git.super_silent.commit(message="bob: added alices_file")
            sage: bob._UI.append('y')
            I will now upload the following new commits to the remote branch `u/bob/ticket/1`:
            ...: bob: added alices_file
            Is this what you want? [Yes/no] y
            sage: alice.git.super_silent.reset('HEAD~~', hard=True)
            sage: alice.git.echo.log('--pretty=%s')
            sage: bob.git.super_silent.add("bobs_other_file")
            sage: bob.git.super_silent.commit(message="bob: added bobs_other_file")
            sage: bob._UI.append('y')
            I will now upload the following new commits to the remote branch `u/bob/ticket/1`:
            ...: bob: added bobs_other_file
            Is this what you want? [Yes/no] y
        if ticket_or_remote_branch is None:
            ticket_or_remote_branch = self._current_ticket()
            if branch is not None and branch != self.git.current_branch():
                raise SageDevValueError("local_branch must be None")
        if ticket_or_remote_branch is None:
            raise SageDevValueError("No `ticket_or_remote_branch` specified to download.")
        if self._is_ticket_name(ticket_or_remote_branch):
            ticket = self._ticket_from_ticket_name(ticket_or_remote_branch)
            remote_branch = ticket_or_remote_branch
                self.git.super_silent.pull(self.git._repository, remote_branch)
                self.git.super_silent.fetch(self.git._repository, "{0}:{1}".format(remote_branch, branch))
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev.git.super_silent.checkout('-b','branch1')
            self._UI.info("Use {0} or {1} to switch to a branch.".format(self._format_command("switch_branch"), self._format_command("switch_ticket")))
        self.git.super_silent.reset()
                    if self._UI.confirm("The following files in your working directory are not tracked by git:\n{0}\nDo you want to add any of these files in this commit?".format("\n".join([" "+fname for fname in untracked_files])), default=False):
                            if self._UI.confirm("Do you want to add `{0}`?".format(file), default=False):
                if not self._UI.confirm("Do you want to commit your changes to branch `{0}`? I will prompt you for a commit message if you do.".format(branch), default=True):
                    self._UI.info("If you want to commit to a different branch/ticket, run {0} or {1} first.".format(self._format_command("switch_branch"), self._format_command("switch_ticket")))
            self.git.super_silent.reset()

    def set_remote(self, branch_or_ticket, remote_branch):
        r"""
        Set the remote branch to push to for ``branch_or_ticket`` to
        ``remote_branch``.

        INPUT:

        - ``branch_or_ticket`` -- a string, the name of a local branch, or a
          string or an integer identifying a ticket or ``None``; if ``None``,
          the current branch is used.

        - ``remote_branch`` -- a string, the name of a remote branch (this
          branch may not exist yet)

        .. SEEALSO::

        - :meth:`upload` -- To upload changes after setting the remote branch

        TESTS:

        Set up a single user for doctesting::

            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev._wrap("_remote_branch_for_ticket")

        Create a new branch::

            sage: UI.append("Summary: ticket1\ndescription")
            sage: dev.create_ticket()
            1

        Modify the remote branch for this ticket's branch::

            sage: dev._remote_branch_for_ticket(1)
            'u/doctest/ticket/1'
            sage: dev.set_remote('ticket/1', 'u/doctest/foo')
            sage: dev._remote_branch_for_ticket(1)
            'u/doctest/foo'
            sage: dev.set_remote('ticket/1', 'foo')
            The remote branch `foo` is not in your user scope. You might not have permission to push to that branch. Did you mean to set the remote branch to `u/doctest/foo`?
            sage: dev._remote_branch_for_ticket(1)
            'foo'
            sage: dev.set_remote('#1', 'u/doctest/foo')
            sage: dev._remote_branch_for_ticket(1)
            'u/doctest/foo'

        """
        if branch_or_ticket is None:
            from git_error import DetachedHeadError
            try:
                branch = self.git.current_branch()
            except DetachedHeadError:
                self._UI.error("`branch` must not be None because you are in detached HEAD state.")
                self._UI.info("Switch to a branch with `{0}` or specify branch explicitly.".format(self._format_command('switch_branch')))
                raise OperationCancelledError("detached head state")
        elif self._is_ticket_name(branch_or_ticket):
            ticket = self._ticket_from_ticket_name(branch_or_ticket)
            if not self._has_local_branch_for_ticket(ticket):
                self._UI.error("no local branch for ticket #{0} found. Cannot set remote branch for that ticket.".format(ticket))
                raise OperationCancelledError("no such ticket")
            branch = self._local_branch_for_ticket(ticket)
        else:
            branch = branch_or_ticket

        self._check_local_branch_name(branch, exists=True)
        self._check_remote_branch_name(remote_branch)
        if not remote_branch.startswith('u/{0}/'.format(self.trac._username)):
            self._UI.warning("The remote branch `{0}` is not in your user scope. You might not have permission to push to that branch. Did you mean to set the remote branch to `u/{1}/{0}`?".format(remote_branch, self.trac._username))

        self._set_remote_branch_for_branch(branch, remote_branch)
        Create a doctest setup with two users::

            sage: from sage.dev.test.sagedev import two_user_setup
            sage: alice, config_alice, bob, config_bob, server = two_user_setup()

        Alice tries to upload to ticket 1 which does not exist yet::

            sage: alice._chdir()
            sage: alice.upload(ticket=1)
            ValueError: `1` is not a valid ticket name or ticket does not exist on trac.

        Alice creates ticket 1 and uploads some changes to it::

            sage: alice._UI.append("Summary: summary1\ndescription")
            sage: ticket = alice.create_ticket()
            sage: open("tracked", "w").close()
            sage: alice.git.super_silent.add("tracked")
            sage: alice.git.super_silent.commit(message="alice: added tracked")
            sage: alice._UI.append("y")
            sage: alice.upload()
            The branch u/alice/ticket/1 does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y

        Now Bob can switch to that ticket and upload changes himself::

            sage: bob._chdir()
            sage: bob.switch_ticket(1)
            sage: with open("tracked", "w") as f: f.write("bob")
            sage: bob.git.super_silent.add("tracked")
            sage: bob.git.super_silent.commit(message="bob: modified tracked")
            sage: bob._UI.append("y")
            sage: bob._UI.append("y")
            sage: bob.upload()
            The branch u/bob/ticket/1 does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            I will now change the branch field of ticket #1 from its current value `u/alice/ticket/1` to `u/bob/ticket/1`. Is this what you want? [Yes/no] y

        Now Alice can download these changes::

            sage: alice._chdir()
            sage: alice.download()

        Alice and Bob make non-conflicting changes simultaneously::

            sage: with open("tracked", "w") as f: f.write("alice")
            sage: alice.git.super_silent.add("tracked")
            sage: alice.git.super_silent.commit(message="alice: modified tracked")

            sage: bob._chdir()
            sage: open("tracked2", "w").close()
            sage: bob.git.super_silent.add("tracked2")
            sage: bob.git.super_silent.commit(message="bob: added tracked2")

        After Alice uploaded her changes, Bob can not set the branch field anymore::

            sage: alice._chdir()
            sage: alice._UI.append("y")
            sage: alice._UI.append("y")
            sage: alice.upload()
            I will now upload the following new commits to the remote branch `u/alice/ticket/1`:
            ...: alice: modified tracked
            ...: bob: modified tracked
            Is this what you want? [Yes/no] y
            I will now change the branch field of ticket #1 from its current value `u/bob/ticket/1` to `u/alice/ticket/1`. Is this what you want? [Yes/no] y

            sage: bob._chdir()
            sage: bob._UI.append("y")
            sage: bob.upload()
            I will now upload the following new commits to the remote branch `u/bob/ticket/1`:
            ...: bob: added tracked2
            Is this what you want? [Yes/no] y
            Not setting the branch field for ticket #1 to `u/bob/ticket/1` because `u/bob/ticket/1` and the current value of the branch field `u/alice/ticket/1` have diverged.

        After merging the changes, this works again::

            sage: bob.download()
            sage: bob._UI.append("y")
            sage: bob._UI.append("y")
            sage: bob.upload()
            I will now upload the following new commits to the remote branch `u/bob/ticket/1`:
            ...: Merge branch 'u/alice/ticket/1' of ... into ticket/1
            ...: alice: modified tracked
            Is this what you want? [Yes/no] y
            I will now change the branch field of ticket #1 from its current value `u/alice/ticket/1` to `u/bob/ticket/1`. Is this what you want? [Yes/no] y

        Check that ``ticket`` works::

            sage: bob.upload(2)
            ValueError: `2` is not a valid ticket name or ticket does not exist on trac.

        After creating the ticket, this works with a warning::
            sage: bob._UI.append("Summary: summary2\ndescription")
            sage: bob.create_ticket()
            2
            sage: bob.switch_ticket(1)
            sage: bob._UI.append("y")
            sage: bob._UI.append("y")
            sage: bob.upload(2)
            You are trying to push the branch `ticket/1` to `u/bob/ticket/2` for ticket #2. However, your local branch for ticket #2 seems to be `ticket/2`. Do you really want to proceed? [yes/No] y
            The branch u/bob/ticket/2 does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y

        Check that ``remote_branch`` works::

            sage: bob._UI.append("y")
            sage: bob._UI.append("y")
            sage: bob.upload(remote_branch="u/bob/branch1")
            The branch u/bob/branch1 does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            I will now change the branch field of ticket #1 from its current value `u/bob/ticket/1` to `u/bob/branch1`. Is this what you want? [Yes/no] y

        """
        if ticket is None:
            ticket = self._current_ticket()
        if ticket is not None:
            ticket = self._ticket_from_ticket_name(ticket)
            self._check_ticket_name(ticket, exists=True)
        from git_error import DetachedHeadError
            branch = self.git.current_branch()
        except DetachedHeadError:
            self._UI.error("Cannot upload while in detached HEAD state.")
            raise OperationCancelledError("cannot upload while in detached HEAD state")

        if remote_branch is None:
            if ticket:
                remote_branch = self._remote_branch_for_ticket(ticket)
                if remote_branch is None:
                    raise SageDevValueError("remote_branch must be specified since #{0} has no remote branch set.".format(ticket))
            else:
                remote_branch = self._remote_branch_for_branch(branch)
                if remote_branch is None:
                    raise SageDevValueError("remote_branch must be specified since the current branch has no remote branch set.")

        self._check_remote_branch_name(remote_branch)

        # whether the user already confirmed that he really wants to push and set the branch field
        user_confirmation = force

        if ticket is not None:
            if self._has_local_branch_for_ticket(ticket) and self._local_branch_for_ticket(ticket) == branch:
                pass
            elif self._has_local_branch_for_ticket(ticket) and self._local_branch_for_ticket(ticket) != branch:
                if user_confirmation or self._UI.confirm("You are trying to push the branch `{0}` to `{1}` for ticket #{2}. However, your local branch for ticket #{2} seems to be `{3}`. Do you really want to proceed?".format(branch, remote_branch, ticket, self._local_branch_for_ticket(ticket)), default=False):
                    self._UI.info("To permanently set the branch associated to ticket #{0} to `{1}`, use `{2}`.".format(ticket, branch, self._format_command("switch_ticket",ticket=ticket,branch=branch)))
                    user_confirmation = True
                else:
                    raise OperationCancelledError("user requsted")
            elif self._has_ticket_for_local_branch(branch) and self._ticket_for_local_branch(branch) != ticket:
                if user_confirmation or self._UI.confirm("You are trying to push the branch `{0}` to `{1}` for ticket #{2}. However, that branch is associated to ticket #{3}. Do you really want to proceed?".format(branch, remote_branch, ticket, self._ticket_for_local_branch(branch))):
                    self._UI.info("To permanently set the branch associated to ticket #{0} to `{1}`, use `{2}`. To create a new branch from `{1}` for #{0}, use `{3}` and `{4}`.".format(ticket, branch, self._format_command("switch_ticket",ticket=ticket,branch=branch), self._format_command("switch_ticket",ticket=ticket), self._format_command("merge", branch=branch)))
                    user_confirmation = True

        self._UI.info("Uploading your changes in `{0}` to `{1}`.".format(branch, remote_branch))
            remote_branch_exists = self._is_remote_branch_name(remote_branch, exists=True)
            if not remote_branch_exists:
                if not self._UI.confirm("The branch {0} does not exist on the remote server yet. Do you want to create the branch?".format(remote_branch), default=True):
                    raise OperationCancelledError("User did not want to create remote branch.")
            else:
                self.git.super_silent.fetch(self.git._repository, remote_branch)

            # check whether force is necessary
            if remote_branch_exists and not self.git.is_child_of(branch, 'FETCH_HEAD'):
                if not force:
                    self._UI.error("Not uploading your changes because they would discard some of the commits on the remote branch `{0}`.".format(remote_branch))
                    self._UI.info("If this is really what you want, use `{0}` to upload your changes.".format(remote_branch, self._format_command("upload",ticket=ticket,remote_branch=remote_branch,force=True)))
                    raise OperationCancelledError("not a fast-forward")

            # check whether this is a nop
            if remote_branch_exists and not force and self.git.commit_for_branch(branch) == self.git.commit_for_ref('FETCH_HEAD'):
                self._UI.info("Not uploading your changes because the remote branch `{0}` is idential to your local branch `{1}`. Did you forget to commit your changes with `{2}`?".format(remote_branch, branch, self._format_command("commit")))
            else:
                try:
                    if not force:
                        if remote_branch_exists:
                            commits = self.git.log("{0}..{1}".format('FETCH_HEAD', branch), '--pretty=%h: %s')
                            if not self._UI.confirm("I will now upload the following new commits to the remote branch `{0}`:\n{1}Is this what you want?".format(remote_branch, commits), default=True):
                                raise OperationCancelledError("user requested")

                    self.git.super_silent.push(self.git._repository, "{0}:{1}".format(branch, remote_branch), force=force)
                except GitError as e:
                    # can we give any advice if this fails?
                    raise
            self._UI.info("Your changes in `{0}` have been uploaded to `{1}`.".format(branch, remote_branch))

        except OperationCancelledError:
            self._UI.info("Did not upload any changes.")
            raise
            current_remote_branch = self.trac._branch_for_ticket(ticket)
            if current_remote_branch == remote_branch:
                self._UI.info("Not setting the branch field for ticket #{0} because it already points to your branch `{1}`.".format(ticket, remote_branch))
            else:
                self._UI.info("Setting the branch field of ticket #{0} to `{1}`.".format(ticket, remote_branch))
                if current_remote_branch is not None:
                    self.git.super_silent.fetch(self.git._repository, current_remote_branch)
                    if force or self.git.is_ancestor_of('FETCH_HEAD', branch):
                        pass
                    else:
                        self._UI.error("Not setting the branch field for ticket #{0} to `{1}` because `{1}` and the current value of the branch field `{2}` have diverged.".format(ticket, remote_branch, current_remote_branch))
                        self._UI.info("If you really want to overwrite the branch field use `{0}`. Otherwise, you need to merge in the changes introduced by `{0}` by using `{1}`.".format(self._format_command("upload",ticket=ticket,remote_branch=remote_branch,force=True), self._format_command("download", ticket=ticket)))
                        raise OperationCancelledError("not a fast-forward")

                if current_remote_branch is not None and not force and not user_confirmation:
                    if not self._UI.confirm("I will now change the branch field of ticket #{0} from its current value `{1}` to `{2}`. Is this what you want?".format(ticket, current_remote_branch, remote_branch), default=True):
                        raise OperationCancelledError("user requested")
                attributes = self.trac._get_attributes(ticket)
                attributes['branch'] = remote_branch
                self.trac._authenticated_server_proxy.ticket.update(ticket, "", attributes)
        if ticket:
            old_dependencies = self.trac.dependencies(ticket)
            old_dependencies = ", ".join(["#"+str(dep) for dep in old_dependencies])
            new_dependencies = self._dependencies_for_ticket(ticket)
            new_dependencies = ", ".join(["#"+str(dep) for dep in new_dependencies])
            if old_dependencies != new_dependencies:
                self._UI.info("Uploading your dependencies for ticket #{0}: `{1}` => `{2}`".format(ticket, old_dependencies, new_dependencies))

                attributes = self.trac._get_attributes(ticket)
                attributes['dependencies'] = new_dependencies
                self.trac._authenticated_server_proxy.ticket.update(ticket, "", attributes)
            elif new_dependencies:
                self._UI.info("Not uploading your dependencies for ticket #{0} because the dependencies on trac are already up-to-date.".format(ticket))
        r"""
        Reset the current working directory to a clean state.

        TESTS:

        Set up a single user for doctesting::

            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()

        Nothing happens if the directory is already clean::

            sage: dev.reset_to_clean_state()

        Bring the directory into a non-clean state::

            sage: dev.git.super_silent.checkout(b="branch1")
            sage: with open("tracked", "w") as f: f.write("boo")
            sage: dev.git.silent.add("tracked")
            sage: dev.git.silent.commit(message="added tracked")

            sage: dev.git.super_silent.checkout('HEAD~')
            sage: dev.git.super_silent.checkout(b="branch2")
            sage: with open("tracked", "w") as f: f.write("foo")
            sage: dev.git.silent.add("tracked")
            sage: dev.git.silent.commit(message="added tracked")
            sage: from sage.dev.git_error import GitError
            sage: try:
            ....:     dev.git.silent.merge("branch1")
            ....: except GitError: pass
            sage: UI.append("n")
            sage: dev.reset_to_clean_state()
            Your repository is in an unclean state. It seems you are in the middle of a merge of some sort. To run this command you have to reset your respository to a clean state. Do you want me to reset your respository? (This will discard many changes which are not commited.) [yes/No] n
            sage: UI.append("y")
            sage: dev.reset_to_clean_state()
            Your repository is in an unclean state. It seems you are in the middle of a merge of some sort. To run this command you have to reset your respository to a clean state. Do you want me to reset your respository? (This will discard many changes which are not commited.) [yes/No] y
            sage: dev.reset_to_clean_state()

        A detached HEAD does not count as a non-clean state::

            sage: dev.git.super_silent.checkout('HEAD', detach=True)
            sage: dev.reset_to_clean_state()

        """
        if not self._UI.confirm("Your repository is in an unclean state. It seems you are in the middle of a merge of some sort. To run this command you have to reset your respository to a clean state. Do you want me to reset your respository? (This will discard many changes which are not commited.)", default=False):
        self.git.reset_to_clean_state()
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev.git.silent.add("tracked")
            sage: dev.git.silent.commit(message="added tracked")
            sage: UI.append("discard")
            The following files in your working directory contain uncommitted changes:
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? [discard/Keep/stash] discard
            sage: UI.append("keep")
            The following files in your working directory contain uncommitted changes:
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? [discard/Keep/stash] keep
            sage: UI.append("stash")
            The following files in your working directory contain uncommitted changes:
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? [discard/Keep/stash] stash
        files = "\n".join([line[2:] for line in self.git.status(porcelain=True).splitlines() if not line.startswith('?')])
        sel = self._UI.select("The following files in your working directory contain uncommitted changes:\n{0}\nDo you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later?".format(files), options=('discard','keep','stash'), default=1)
                    self.git.super_silent.stash()
                        self.git.super_silent.stash('branch',branch,'stash@{0}')
                        self.git.super_silent.commit('-a',message="Changes stashed by reset_to_clean_working_directory()")
                        self.git.super_silent.stash('drop')
                        self.git.super_silent.branch("-D",branch)
                self.git.super_silent.checkout(current_branch or current_commit)
        r"""
        Unstash the changes recorded in ``branch``.

        INPUT:

        - ``branch`` -- the name of a local branch or ``None`` (default:
          ``None``), if ``None`` list all stashes.

        TESTS:

        Set up a single user for doctesting::

            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()

        Create some stashes::

            sage: dev.unstash()
            (no stashes)
            sage: with open("tracked", "w") as f: f.write("foo")
            sage: dev.git.silent.add("tracked")
            sage: UI.append("s")
            sage: dev.reset_to_clean_working_directory()
            The following files in your working directory contain uncommitted changes:
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? [discard/Keep/stash] s
            Your changes have been recorded on a new branch `stash/1`.
            sage: with open("tracked", "w") as f: f.write("boo")
            sage: dev.git.silent.add("tracked")
            sage: UI.append("s")
            sage: dev.reset_to_clean_working_directory()
            The following files in your working directory contain uncommitted changes:
             tracked
            Do you want me to discard any changes which are not committed? Should the changes be kept? Or do you want to stash them for later? [discard/Keep/stash] s
            Your changes have been recorded on a new branch `stash/2`.
            sage: dev.unstash()
            stash/1
            stash/2

        Unstash a change::

            sage: dev.unstash("stash/1")

        Unstash something that is not a stash::

            sage: dev.unstash("HEAD")
            ValueError: `HEAD` is not a valid name for a stash.

        Unstash a conflicting change::

            sage: dev.unstash("stash/2")
            The changes recorded in `stash/2` do not apply cleanly to your working directory.

        """
            stashes.sort()
            stashes = stashes or "(no stashes)"
            self._UI.info("Use `{0}` to apply the changes recorded in the stash to your working directory where `name` is one of the following:\n{1}".format(self._format_command("unstash",branch="name"), stashes))
            self._UI.show(stashes)
            self.git.super_silent.cherry_pick(branch, no_commit=True)
            self._UI.error("The changes recorded in `{0}` do not apply cleanly to your working directory.".format(branch))
            self._UI.info("You can try to resolve the conflicts manually with `{0}`.".format(self._format_command("merge", branch_or_ticket=branch)))
            raise OperationCancelledError("unstash failed")
        self.git.super_silent.reset()
        self._UI.info("The changes recorded in `{0}` have been restored in your working directory. If you do not need the stash anymore, you can drop it with `{1}`.".format(branch, self._format_command("abandon",branch=branch)))
          edit the :meth:`_current_ticket`.
        TESTS:
        Set up a single user for doctesting::

            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()

        Create a ticket and edit it::

            sage: UI.append("Summary: summary1\ndescription")
            sage: dev.create_ticket()
            1
            sage: UI.append("Summary: summary1\ndescription...")
            sage: dev.edit_ticket()
            sage: dev.trac._get_attributes(1)
            {'description': 'description...', 'summary': 'summary1'}
            ticket = self._current_ticket()
        self._check_ticket_name(ticket, exists=True)
        self.trac.edit_ticket_interactive(ticket)
          edit the :meth:`_current_ticket`.
        TESTS:

        Set up a single user for doctesting::

            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
        Create a ticket and add a comment::

            sage: UI.append("Summary: summary1\ndescription")
            sage: dev.create_ticket()
            1
            sage: UI.append("comment")
            sage: dev.add_comment()
            sage: server.tickets[1].comments
            ['comment']
            ticket = self._current_ticket()
        self._check_ticket_name(ticket, exists=True)
        self.trac.add_comment_interactive(ticket)
          browse the :meth:`_current_ticket`.
        EXAMPLES::
            sage: dev.browse_ticket(10000) # not tested
            ticket = self._current_ticket()
        self._check_ticket_name(ticket, exists=True)
    def remote_status(self, ticket=None):
        Show information about the status of ``ticket``.
          (default: ``None``), the number of the ticket to edit.  If ``None``,
          show information for the :meth:`_current_ticket`.
        TESTS:
        Set up a single user for doctesting::
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
        It is an error to call this without parameters if not on a ticket::
            sage: dev.remote_status()
            ValueError: ticket must be specified if not currently on a ticket.
        Create a ticket and show its remote status::
            sage: UI.append("Summary: ticket1\ndescription")
            sage: dev.create_ticket()
            1
            sage: dev.remote_status()
            Ticket #1 (https://trac.sagemath.org/ticket/1)
            ==============================================
            Your branch `ticket/1` has 0 commits.
            No branch has been set on the trac ticket yet.
            You have not created a remote branch yet.

        After uploading the local branch::

            sage: UI.append("y")
            sage: dev.upload()
            The branch u/doctest/ticket/1 does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            sage: dev.remote_status()
            Ticket #1 (https://trac.sagemath.org/ticket/1)
            ==============================================
            Your branch `ticket/1` has 0 commits.
            The trac ticket points to the branch `u/doctest/ticket/1` which has 0 commits. It does not differ from `ticket/1`.

        Making local changes::

            sage: open("tracked", "w").close()
            sage: dev.git.silent.add("tracked")
            sage: dev.git.silent.commit(message="added tracked")
            sage: dev.remote_status()
            Ticket #1 (https://trac.sagemath.org/ticket/1)
            ==============================================
            Your branch `ticket/1` has 1 commits.
            The trac ticket points to the branch `u/doctest/ticket/1` which has 0 commits. `ticket/1` is ahead of `u/doctest/ticket/1` by 1 commits:
            ...: added tracked

        Uploading them::

            sage: UI.append("y")
            sage: dev.upload()
            I will now upload the following new commits to the remote branch `u/doctest/ticket/1`:
            ...: added tracked
            Is this what you want? [Yes/no] y
            sage: dev.remote_status()
            Ticket #1 (https://trac.sagemath.org/ticket/1)
            ==============================================
            Your branch `ticket/1` has 1 commits.
            The trac ticket points to the branch `u/doctest/ticket/1` which has 1 commits. It does not differ from `ticket/1`.

        The branch on the ticket is ahead of the local branch::

            sage: dev.git.silent.reset('HEAD~', hard=True)
            sage: dev.remote_status()
            Ticket #1 (https://trac.sagemath.org/ticket/1)
            ==============================================
            Your branch `ticket/1` has 0 commits.
            The trac ticket points to the branch `u/doctest/ticket/1` which has 1 commits. `u/doctest/ticket/1` is ahead of `ticket/1` by 1 commits:
            ...: added tracked

        A mixed case::

            sage: open("tracked2", "w").close()
            sage: dev.git.silent.add("tracked2")
            sage: dev.git.silent.commit(message="added tracked2")
            sage: open("tracked3", "w").close()
            sage: dev.git.silent.add("tracked3")
            sage: dev.git.silent.commit(message="added tracked3")
            sage: open("tracked4", "w").close()
            sage: dev.git.silent.add("tracked4")
            sage: dev.git.silent.commit(message="added tracked4")
            sage: dev._UI.append("y")
            sage: dev.upload(remote_branch="u/doctest/branch1", force=True)
            The branch u/doctest/branch1 does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            sage: dev.git.silent.reset('HEAD~', hard=True)
            sage: dev.remote_status()
            Ticket #1 (https://trac.sagemath.org/ticket/1)
            ==============================================
            Your branch `ticket/1` has 2 commits.
            The trac ticket points to the branch `u/doctest/branch1` which has 3 commits. `u/doctest/branch1` is ahead of `ticket/1` by 1 commits:
            ...: added tracked4
            Your remote branch `u/doctest/ticket/1` has 1 commits. The branches `u/doctest/ticket/1` and `ticket/1` have diverged.
            `u/doctest/ticket/1` is ahead of `ticket/1` by 1 commits:
            ...: added tracked
            `ticket/1` is ahead of `u/doctest/ticket/1` by 2 commits:
            ...: added tracked2
            ...: added tracked3
        if ticket is None:
            ticket = self._current_ticket()

        if ticket is None:
            raise SageDevValueError("ticket must be specified if not currently on a ticket.")

        self._check_ticket_name(ticket, exists=True)
        ticket = self._ticket_from_ticket_name(ticket)

        from sage.env import TRAC_SERVER_URI
        header = "Ticket #{0} ({1})".format(ticket, TRAC_SERVER_URI + '/ticket/' + str(ticket))
        underline = "="*len(header)

        commits = lambda a, b: list(reversed(self.git.log("{0}..{1}".format(a,b), "--pretty=%an <%ae>: %s").splitlines()))

        def detail(a, b, a_to_b, b_to_a):
            if not a_to_b and not b_to_a:
                return "It does not differ from `{0}`.".format(b)
            elif not a_to_b:
                return "`{0}` is ahead of `{1}` by {2} commits:\n{3}".format(a,b,len(b_to_a),"\n".join(b_to_a))
            elif not b_to_a:
                return "`{0}` is ahead of `{1}` by {2} commits:\n{3}".format(b,a,len(a_to_b),"\n".join(a_to_b))
            else:
                return "The branches `{0}` and `{1}` have diverged.\n`{0}` is ahead of `{1}` by {2} commits:\n{3}\n`{1}` is ahead of `{0}` by {4} commits:\n{5}".format(a,b,len(b_to_a),"\n".join(b_to_a),len(a_to_b),"\n".join(a_to_b))

        branch = None
        if self._has_local_branch_for_ticket(ticket):
            branch = self._local_branch_for_ticket(ticket)
            if not self.git.is_ancestor_of(MASTER_BRANCH, branch):
                local_summary = "Your branch is `{0}`.".format(branch)
            else:
                master_to_branch = commits(MASTER_BRANCH, branch)
                local_summary = "Your branch `{0}` has {1} commits.".format(branch, len(master_to_branch))
        else:
            local_summary = "You have no local branch for this ticket"

        ticket_branch = self.trac._branch_for_ticket(ticket)
        if ticket_branch:
            ticket_to_local = None
            local_to_ticket = None
            if not self._is_remote_branch_name(ticket_branch, exists=True):
                ticket_summary = "The trac ticket points to the branch `{0}` which does not exist."
            else:
                self.git.super_silent.fetch(self.git._repository, ticket_branch)
                if not self.git.is_ancestor_of(MASTER_BRANCH, 'FETCH_HEAD'):
                    ticket_summary = "The trac ticket points to the branch `{0}`.".format(ticket_branch)
                    master_to_ticket = commits(MASTER_BRANCH, 'FETCH_HEAD')
                    ticket_summary = "The trac ticket points to the branch `{0}` which has {1} commits.".format(ticket_branch, len(master_to_ticket))
                    if self.git.is_ancestor_of(MASTER_BRANCH, branch):
                        ticket_to_local = commits('FETCH_HEAD', branch)
                        local_to_ticket = commits(branch, 'FETCH_HEAD')
                        ticket_summary += " "+detail(ticket_branch, branch, ticket_to_local, local_to_ticket)
            ticket_summary = "No branch has been set on the trac ticket yet."
        remote_branch = self._remote_branch_for_ticket(ticket)
        if self._is_remote_branch_name(remote_branch, exists=True):
            remote_to_local = None
            local_to_remote = None
            self.git.super_silent.fetch(self.git._repository, remote_branch)
            if not self.git.is_ancestor_of(MASTER_BRANCH, 'FETCH_HEAD'):
                remote_summary = "Your remote branch is `{0}`.".format(remote_branch)
                master_to_remote = commits(MASTER_BRANCH, 'FETCH_HEAD')
                remote_summary = "Your remote branch `{0}` has {1} commits.".format(remote_branch, len(master_to_remote))
                if self.git.is_ancestor_of(MASTER_BRANCH, branch):
                    remote_to_local = commits('FETCH_HEAD', branch)
                    local_to_remote = commits(branch, 'FETCH_HEAD')
                    remote_summary += " "+detail(remote_branch, branch, remote_to_local, local_to_remote)
            remote_summary = "You have not created a remote branch yet."

        show = [header, underline, local_summary, ticket_summary]
        if not self._is_remote_branch_name(remote_branch, exists=True) or remote_branch != ticket_branch:
            show.append(remote_summary)

        self._UI.show("\n".join(show))
        Import a patch into the current branch.
        - ``patchname`` -- a string or ``None`` (default: ``None``), passed on
          to :meth:`download_patch`
        - ``url`` -- a string or ``None`` (default: ``None``), passed on to
          :meth:`download_patch`

        - ``local_file`` -- a string or ``None`` (default: ``None``), if
          specified, ``url`` and ``patchname`` must be ``None``; instead of
          downloading the patch, apply this patch file.

        - ``diff_format`` -- a string or ``None`` (default: ``None``), per
          default the format of the patch file is autodetected; it can be
          specified explicitly with this parameter
        - ``header_format`` -- a string or ``None`` (default: ``None``), per
          default the format of the patch header is autodetected; it can be
          specified explicitly with this parameter

        - ``path_format`` -- a string or ``None`` (default: ``None``), per
          default the format of the paths is autodetected; it can be specified
          explicitly with this parameter

        .. NOTE::

            This method calls :meth:`_rewrite_patch` if necessary to rewrite
            patches which were created for sage before the move to git
            happened. In other words, this is not just a simple wrapper for
            ``git am``.
        - :meth:`download_patch` -- download a patch to a local file.
        - :meth:`download` -- merges in changes from a git branch rather than a
          patch.
        TESTS:
        Set up a single user for doctesting::
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()

        Create a patch::

            sage: open("tracked", "w").close()
            sage: open("tracked2", "w").close()
            sage: import os
            sage: patchfile = os.path.join(dev._sagedev.tmp_dir,"tracked.patch")
            sage: dev.git.silent.add("tracked", "tracked2")
            sage: with open(patchfile, "w") as f: f.write(dev.git.diff(cached=True))
            sage: dev.git.silent.reset()

        Applying this patch fails::

            sage: dev.import_patch(local_file=patchfile, path_format="new") # the autodetection of the path format fails since we are not in a sage repository
            There are untracked files in your working directory:
            tracked
            tracked2
            The patch cannot be imported unless these files are removed.

        After moving away ``tracked`` and ``tracked2``, this works::

            sage: os.unlink("tracked")
            sage: os.unlink("tracked2")
            sage: dev.import_patch(local_file=patchfile, path_format="new")
            Applying: No Subject. Modified: tracked, tracked2

         We create a patch which does not apply::

            sage: with open("tracked", "w") as f: f.write("foo")
            sage: dev.git.silent.add("tracked")
            sage: with open("tracked", "w") as f: f.write("boo")
            sage: with open("tracked2", "w") as f: f.write("boo")
            sage: with open(patchfile, "w") as f: f.write(dev.git.diff())
            sage: dev.git.reset_to_clean_working_directory()
            sage: open("tracked").read()
            ''

         The import fails::

            sage: UI.append("abort")
            sage: UI.append("y")
            sage: dev.import_patch(local_file=patchfile, path_format="new")
            Applying: No Subject. Modified: tracked, tracked2
            error: patch failed: tracked:1
            error: tracked: patch does not apply
            Patch failed at 0001 No Subject. Modified: tracked, tracked2
            The copy of the patch that failed is found in:
               .../rebase-apply/patch
            <BLANKLINE>
            The patch does not apply cleanly. Would you like to apply it anyway and create reject files for the parts that do not apply? [yes/No] y
            Checking patch tracked...
            error: while searching for:
            foo
            error: patch failed: tracked:1
            Checking patch tracked2...
            Applying patch tracked with 1 reject...
            Rejected hunk #1.
            Applied patch tracked2 cleanly.
            The patch did not apply cleanly. Please integrate the `.rej` files that were created and resolve conflicts. After you do, type `resolved`. If you want to abort this process, type `abort`. [resolved/abort] abort
            Removing tracked.rej
            sage: open("tracked").read()
            ''

            sage: UI.append("resolved")
            sage: UI.append("y")
            sage: dev.import_patch(local_file=patchfile, path_format="new")
            Applying: No Subject. Modified: tracked, tracked2
            error: patch failed: tracked:1
            error: tracked: patch does not apply
            Patch failed at 0001 No Subject. Modified: tracked, tracked2
            The copy of the patch that failed is found in:
               .../rebase-apply/patch
            <BLANKLINE>
            The patch does not apply cleanly. Would you like to apply it anyway and create reject files for the parts that do not apply? [yes/No] y
            Checking patch tracked...
            error: while searching for:
            foo
            error: patch failed: tracked:1
            Checking patch tracked2...
            Applying patch tracked with 1 reject...
            Rejected hunk #1.
            Applied patch tracked2 cleanly.
            The patch did not apply cleanly. Please integrate the `.rej` files that were created and resolve conflicts. After you do, type `resolved`. If you want to abort this process, type `abort`. [resolved/abort] resolved
            Removing tracked.rej
            sage: open("tracked").read() # we did not actually incorporate the .rej files in this doctest, so nothing has changed
            ''
            sage: open("tracked2").read()
            'boo'

        """
        untracked = self.git.untracked_files()
        # do not exclude .patch files here: they would be deleted by reset_to_clean_working_directory() later
        if untracked:
            self._UI.error("There are untracked files in your working directory:\n{0}\nThe patch cannot be imported unless these files are removed.".format("\n".join(untracked)))
            raise OperationCancelledError("untracked files make import impossible")

            local_file = sel.download_patch(patchname=patchname, url=url)
            try:
                return self.import_patch(
                        local_file=local_file,
                        diff_format=diff_format, header_format=header_format, path_format=path_format)
            finally:
                import os
                os.unlink(local_file)
                self.git.echo.am(outfile, "--resolvemsg= ", ignore_whitespace=True)
                if not self._UI.confirm("The patch does not apply cleanly. Would you like to apply it anyway and create reject files for the parts that do not apply?", default=False):
                    self.git.reset_to_clean_working_directory(remove_untracked_files=True)
                    try:
                        self.git.silent.apply(outfile, ignore_whitespace=True, reject=True)
                    except GitError:
                        if self._UI.select("The patch did not apply cleanly. Please integrate the `.rej` files that were created and resolve conflicts. After you do, type `resolved`. If you want to abort this process, type `abort`.", ("resolved","abort")) == "abort":
                            self.git.reset_to_clean_state()
                            self.git.reset_to_clean_working_directory(remove_untracked_files=True)
                            raise OperationCancelledError("User requested to cancel the apply.")
                    else:
                        self._UI.show("It seemed that the patch would not apply, but in fact it did.")
                        return
                    self.git.super_silent.add(update=True)
                    untracked = [fname for fname in self.git.untracked_files() if not fname.endswith(".rej")]
                    if untracked:
                        self._UI.confirm("The patch will introduce the following new files to the repository:\n{0}\nIs this correct?".format("\n".join(untracked)), default=True)
                        self.git.super_silent.add(*untracked)
                    self.git.am('--resolvemsg= ', resolved=True)
                    self._UI.info("A commit on the current branch has been created from the patch.")
                finally:
                    self.git.reset_to_clean_working_directory(remove_untracked_files=True)
        EXAMPLES::

            sage: dev.download_patch(ticket=14882) # optional: internet
            ValueError: Ticket #14882 has more than one attachment but parameter `patchname` is not present, please set it to one of: trac_14882-backtrack_longtime-dg.patch, trac_14882-backtrack_longtime-dg-v2.patch, trac_14882-spelling_in_backtrack-dg.patch
            sage: dev.download_patch(ticket=14882, patchname='trac_14882-backtrack_longtime-dg.patch') # optional: internet
            ...

        TESTS:

        Set up a single user for doctesting::

            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()

        Create a new ticket::

            sage: UI.append("Summary: summary1\ndescription")
            sage: dev.create_ticket()
            1

        There are no attachment to download yet::

            sage: dev.download_patch(ticket=1)
            ValueError: Ticket #1 has no attachments.

        After adding one attachment, this works::
            sage: server.tickets[1].attachments['first.patch'] = ''
            sage: dev.download_patch(ticket=1) # not tested, download_patch tries to talk to the live server

        After adding another attachment, this does not work anymore, one needs
        to specify which attachment should be downloaded::

            sage: server.tickets[1].attachments['second.patch'] = ''
            sage: dev.download_patch(ticket=1)
            ValueError: Ticket #1 has more than one attachment but parameter `patchname` is not present, please set it to one of: first.patch, second.patch
            sage: dev.download_patch(ticket=1, patchname = 'second.patch') # not tested, download_patch tries to talk to the live server
            import urllib
            return urllib.urlretrieve(url)[0]
                    raise SageDevValueError("Ticket #%s has more than one attachment but parameter `patchname` is not present, please set it to one of: %s"%(ticket,", ".join(sorted(attachments))))
            return self.download_patch(ticket=self._current_ticket())
    def prune_closed_tickets(self):
        Remove branches for tickets that are already merged into master.

        .. SEEALSO::

            :meth:`abandon` -- Abandon a single ticket or branch.

        TESTS:

        Create a single user for doctesting::

            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()

        Create a ticket branch::

            sage: UI.append("Summary: summary\ndescription")
            sage: dev.create_ticket()
            1
            sage: dev.local_tickets()
              : master
            #1: ticket/1

        With a commit on it, the branch is not abandoned::

            sage: open("tracked","w").close()
            sage: dev.git.silent.add("tracked")
            sage: dev.git.super_silent.commit(message="added tracked")
            sage: dev.prune_closed_tickets()
            sage: dev.local_tickets()
              : master
            #1: ticket/1

        After merging it to the master branch, it is abandoned. This does not
        work, because we cannot move the current branch::

            sage: dev.git.super_silent.checkout("master")
            sage: dev.git.super_silent.merge("ticket/1")

            sage: dev.git.super_silent.checkout("ticket/1")
            sage: dev.prune_closed_tickets()
            Abandoning #1.
            Can not delete `ticket/1` because you are currently on that branch.

        Now, the branch is abandoned::

            sage: dev.vanilla()
            sage: dev.prune_closed_tickets()
            Abandoning #1.
            Moved your branch `ticket/1` to `trash/ticket/1`.
            sage: dev.local_tickets()
            : master
            sage: dev.prune_closed_tickets()

        """
        for branch in self.git.local_branches():
            if self._has_ticket_for_local_branch(branch):
                ticket = self._ticket_for_local_branch(branch)
                if self.git.is_ancestor_of(branch, MASTER_BRANCH):
                    self._UI.show("Abandoning #{0}.".format(ticket))
                    self.abandon(ticket)

    def abandon(self, ticket_or_branch=None):
        r"""
        Abandon a ticket or branch.
        - ``ticket_or_branch`` -- an integer or string identifying a ticket or
          the name of a local branch or ``None`` (default: ``None``), remove
          the branch ``ticket_or_branch`` or the branch for the ticket
          ``ticket_or_branch`` (or the current branch if ``None``). Also
          removes the users remote tracking branch.
        - :meth:`prune_closed_tickets` -- abandon tickets that have
          been closed.
        - :meth:`local_tickets` -- list local non-abandoned tickets.
        TESTS:

        Create a single user for doctesting::
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()

        Create a ticket branch and abandon it::

            sage: UI.append("Summary: summary\ndescription")
            sage: dev.create_ticket()
            1
            sage: dev.abandon(1)
            Can not delete `ticket/1` because you are currently on that branch.
            sage: dev.vanilla()
            sage: dev.abandon(1)
            Moved your branch `ticket/1` to `trash/ticket/1`.
        if self._is_ticket_name(ticket_or_branch):
            ticket = self._ticket_from_ticket_name(ticket_or_branch)

            if not self._has_local_branch_for_ticket(ticket):
                raise SageDevValueError("Can not abandon #{0}. You have no local branch for this ticket.".format(ticket))
            ticket_or_branch = self._local_branch_for_ticket(ticket)

        if self._is_local_branch_name(ticket_or_branch):
            branch = ticket_or_branch
            self._check_local_branch_name(branch, exists=True)

            if branch == MASTER_BRANCH:
                self._UI.error("I will not delete the master branch.")
                raise OperationCancelledError("protecting the user")

            if not self.git.is_ancestor_of(branch, MASTER_BRANCH):
                if not self._UI.confirm("I will delete your local branch `{0}`. Is this what you want?".format(branch), default=False):
                    raise OperationCancelledError("user requested")
            from git_error import DetachedHeadError
                if self.git.current_branch() == branch:
                    self._UI.error("Can not delete `{0}` because you are currently on that branch.".format(branch))
                    self._UI.info("Use {0} to move to a different branch.".format(self._format_command("vanilla")))
                    raise OperationCancelledError("can not delete current branch")
            except DetachedHeadError:
                pass

            new_branch = self._new_local_branch_for_trash(branch)
            self.git.super_silent.branch("-m", branch, new_branch)
            self._UI.show("Moved your branch `{0}` to `{1}`.".format(branch, new_branch))
            raise SageDevValueError("ticket_or_branch must be the name of a ticket or a local branch")
    def gather(self, branch, *tickets_or_branches):
        Create a new branch ``branch`` with ``tickets_or_remote_branches``
        applied.

        INPUT:

        - ``branch`` -- a string, the name of the new branch

        - ``tickets_or_branches`` -- a list of integers and strings; for an
          integer or string identifying a ticket, the branch on the trac ticket
          gets merged, for the name of a local or remote branch, that branch
          gets merged.
        - :meth:`merge` -- merge into the current branch rather than creating a
          new one
        TESTS:

        Create a doctest setup with a single user::

            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()

        Create tickets and branches::

            sage: dev._UI.append("Summary: summary1\ndescription")
            sage: dev.create_ticket()
            1
            sage: open("tracked","w").close()
            sage: dev.git.silent.add("tracked")
            sage: dev.git.super_silent.commit(message="added tracked")
            sage: dev._UI.append("y")
            sage: dev._UI.append("y")
            sage: dev.upload()
            The branch u/doctest/ticket/1 does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
        Gather all these branches::

            sage: dev.gather("gather_branch", "#1", "ticket/1", "u/doctest/ticket/1")
            Merging the remote branch `u/doctest/ticket/1` into the local branch `gather_branch`.
            Merging the remote branch `u/doctest/ticket/1` into the local branch `gather_branch`.
            Merging the remote branch `u/doctest/ticket/1` into the local branch `gather_branch`.
        try:
            self.reset_to_clean_state()
            self.reset_to_clean_working_directory()
        except OperationCancelledError:
            self._UI.error("Cannot gather branches because working directory is not in a clean state.")
            raise OperationCancelledError("working directory not clean")

        self._check_local_branch_name(branch, exists=False)

        branches = []
        for ticket_or_branch in tickets_or_branches:
            local_branch = None
            remote_branch = None
            if self._is_ticket_name(ticket_or_branch):
                ticket = self._ticket_from_ticket_name(ticket_or_branch)
                remote_branch = self.trac._branch_for_ticket(ticket)
                if remote_branch is None:
                    raise SageDevValueError("Ticket #{0} does not have a branch set yet.".format(ticket))
            elif self._is_local_branch_name(ticket_or_branch, exists=True):
                local_branch = ticket_or_branch
            else:
                remote_branch = ticket_or_branch
            if local_branch:
                self._check_local_branch_name(local_branch, exists=True)
                branches.append(("local",local_branch))
            if remote_branch:
                self._check_remote_branch_name(remote_branch, exists=True)
                branches.append(("remote",remote_branch))

        self._UI.info("Creating a new branch `{0}`.".format(branch))
        self.git.super_silent.branch(branch, MASTER_BRANCH)
        self.git.super_silent.checkout(branch)

        try:
            for local_remote,branch in branches:
                self._UI.info("Merging {2} branch `{0}` into `{1}`.".format(remote_branch, branch, local_remote))
                self.merge(remote_branch, download=True)
        except:
            self.git.reset_to_clean_state()
            self.git.reset_to_clean_working_directory()
            self.vanilla()
            self.git.super_silent.branch("-D", branch)
            self._UI.info("Deleted branch `{0}`.".format(branch))

    def merge(self, ticket_or_branch=MASTER_BRANCH, download=None, create_dependency=None):
        Merge changes from ``ticket_or_branch`` into the current branch.
        - ``ticket_or_branch`` -- an integer or strings (default:
          ``'master'``); for an integer or string identifying a ticket, the
          branch on the trac ticket gets merged (or the local branch for the
          ticket, if ``download`` is ``False``), for the name of a local or
          remote branch, that branch gets merged. If ``'dependencies'``, the
          dependencies are merged in one by one, starting with one listed first
          in the dependencies field on trac.

        - ``download`` -- a boolean or ``None`` (default: ``None``); if
          ``ticket_or_branch`` identifies a ticket, whether to download the
          latest branch on the trac ticket (the default); if
          ``ticket_or_branch`` is a remote branch, whether to download that
          remote branch (the default); if ``ticket_or_branch`` is a local
          branch, whether to download its remote branch (not the default)

        - ``create_dependency`` -- a boolean or ``None`` (default: ``None``),
          wether to create a dependency to ``ticket_or_branch``. If ``None``,
          then a dependency is created if ``ticket_or_branch`` identifies a
          ticket and if the current branch is associated to a ticket.

        .. NOTE::

            Dependencies are stored locally and only updated with respect to
            the remote server during :meth:`upload` and :meth:`download`.

            Adding a dependency has some consequences:

            - the other ticket must be positively reviewed and merged before
              this ticket may be merged into the official release of sage.  The
              commits included from a dependency don't need to be reviewed in
              this ticket, whereas commits reviewed in this ticket from a
              non-dependency may make reviewing the other ticket easier.

            - you can more easily merge in future changes to dependencies.  So
              if you need a feature from another ticket it may be appropriate
              to create a dependency to that you may more easily benefit
              from others' work on that ticket.

            - if you depend on another ticket then you need to worry about the
              progress on that ticket.  If that ticket is still being actively
              developed then you may need to make many merges to keep up.
        - :meth:`show_dependencies` -- see the current dependencies.

        - :meth:`GitInterface.merge` -- git's merge command has more options
          and can merge multiple branches at once.
        - :meth:`gather` -- creates a new branch to merge into rather than
          merging into the current branch.
        Create a doctest setup with two users::

            sage: from sage.dev.test.sagedev import two_user_setup
            sage: alice, config_alice, bob, config_bob, server = two_user_setup()

        Create tickets and branches::

            sage: alice._chdir()
            sage: alice._UI.append("Summary: summary1\ndescription")
            sage: alice.create_ticket()
            1
            sage: alice._UI.append("Summary: summary2\ndescription")
            sage: alice.create_ticket()
            2

        Alice creates two branches and merges them::

            sage: alice.switch_ticket(1)
            sage: open("alice1","w").close()
            sage: alice.git.silent.add("alice1")
            sage: alice.git.super_silent.commit(message="added alice1")
            sage: alice.switch_ticket(2)
            sage: with open("alice2","w") as f: f.write("alice")
            sage: alice.git.silent.add("alice2")
            sage: alice.git.super_silent.commit(message="added alice2")

        When merging for a ticket, the branch on the trac ticket matters::

            sage: alice.merge("#1")
            Can not merge remote branch for #1. No branch has been set on the trac ticket.
            sage: alice.switch_ticket(1)
            sage: alice._UI.append("y")
            sage: alice.upload()
            The branch u/alice/ticket/1 does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            sage: alice.switch_ticket(2)
            sage: alice.merge("#1", download=False)
            Merging the local branch `ticket/1` into the local branch `ticket/2`.
            Added dependency on #1 to #2.

        Merging local branches::

            sage: alice.merge("ticket/1")
            Merging the local branch `ticket/1` into the local branch `ticket/2`.

        A remote branch for a local branch is only merged in if ``download`` is set::

            sage: alice._sagedev._set_remote_branch_for_branch("ticket/1", "nonexistant")
            sage: alice.merge("ticket/1")
            Merging the local branch `ticket/1` into the local branch `ticket/2`.
            sage: alice.merge("ticket/1", download=True)
            Can not merge remote branch `nonexistant`. It does not exist.

        Bob creates a conflicting commit::

            sage: bob._chdir()
            sage: bob.switch_ticket(1)
            sage: with open("alice2","w") as f: f.write("bob")
            sage: bob.git.silent.add("alice2")
            sage: bob.git.super_silent.commit(message="added alice2")
            sage: bob._UI.append("y")
            sage: bob._UI.append("y")
            sage: bob.upload()
            The branch u/bob/ticket/1 does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            I will now change the branch field of ticket #1 from its current value `u/alice/ticket/1` to `u/bob/ticket/1`. Is this what you want? [Yes/no] y

        The merge now requires manual conflict resolution::

            sage: alice._chdir()
            sage: alice._UI.append("abort")
            sage: alice.merge("#1")
            Merging the remote branch `u/bob/ticket/1` into the local branch `ticket/2`.
            There was an error during the merge. Most probably there were conflicts when merging. The following should make it clear which files are affected:
            Auto-merging alice2
            CONFLICT (add/add): Merge conflict in alice2
            Please fix conflicts in the affected files (in a different terminal) and type 'resolved'. Or type 'abort' to abort the merge. [resolved/abort] abort
            sage: alice._UI.append("resolved")
            sage: alice.merge("#1")
            Merging the remote branch `u/bob/ticket/1` into the local branch `ticket/2`.
            There was an error during the merge. Most probably there were conflicts when merging. The following should make it clear which files are affected:
            Auto-merging alice2
            CONFLICT (add/add): Merge conflict in alice2
            Please fix conflicts in the affected files (in a different terminal) and type 'resolved'. Or type 'abort' to abort the merge. [resolved/abort] resolved

        """
        try:
            self.reset_to_clean_state()
            self.reset_to_clean_working_directory()
        except OperationCancelledError:
            self._UI.error("Cannot merge because working directory is not in a clean state.")
            raise OperationCancelledError("working directory not clean")

        from git_error import DetachedHeadError
        try:
            current_branch = self.git.current_branch()
        except DetachedHeadError:
            self._UI.error("You are currently not on any branch. Use `{0}` or `{1}` to switch to a branch.".format(self._format_command("switch_branch"), self._format_command("switch_ticket")))
            raise OperationCancelledError("detached head")

        current_ticket = self._current_ticket()

        ticket = None
        branch = None
        remote_branch = None

        if self._is_local_branch_name(ticket_or_branch, exists=True):
            branch = ticket_or_branch
            if download is None:
                download = False
            if self._has_ticket_for_local_branch(branch):
                ticket = self._ticket_for_local_branch(branch)
                if create_dependency is None:
                    create_dependency = False
            else:
                if create_dependency:
                    raise SageDevValueError("Can not create a dependency to `{0}` because it is not associated to a ticket.".format(branch))
                create_dependency = False
            remote_branch = self._remote_branch_for_branch(branch)
        elif self._is_ticket_name(ticket_or_branch):
            ticket = self._ticket_from_ticket_name(ticket_or_branch)
            self._check_ticket_name(ticket, exists=True)
            if download is None:
                download = True
            if create_dependency is None:
                create_dependency = True
            if self._has_local_branch_for_ticket(ticket):
                branch = self._local_branch_for_ticket(ticket)
            if download:
                remote_branch = self.trac._branch_for_ticket(ticket)
                if remote_branch is None:
                    self._UI.error("Can not merge remote branch for #{0}. No branch has been set on the trac ticket.".format(ticket))
                    raise OperationCancelledError("remote branch not set on trac")
        else:
            remote_branch = ticket_or_branch
            if download is None:
                download = True
            if download == False:
                raise SageDevValueError("download must be `True` for a remote branch")
            if create_dependency is None:
                create_dependency = False
            if create_dependency == True:
                raise SageDevValueError("Can not create a dependency to the remote branch `{0}`.".format(remote_branch))

        local_merge_branch = branch

        if download:
            assert remote_branch
            if not self._is_remote_branch_name(remote_branch, exists=True):
                self._UI.error("Can not merge remote branch `{0}`. It does not exist.".format(remote_branch))
                raise OperationCancelledError("no such branch")
            self._UI.show("Merging the remote branch `{0}` into the local branch `{1}`.".format(remote_branch, current_branch))
            self.git.super_silent.fetch(self.git._repository, remote_branch)
            local_merge_branch = 'FETCH_HEAD'
        else:
            assert branch
            self._UI.show("Merging the local branch `{0}` into the local branch `{1}`.".format(branch, current_branch))

        from git_error import GitError
        try:
            self.git.super_silent.merge(local_merge_branch)
        except GitError as e:
            try:
                lines = e.stdout.splitlines() + e.stderr.splitlines()
                lines = [line for line in lines if line != "Automatic merge failed; fix conflicts and then commit the result."]
                lines.insert(0, "There was an error during the merge. Most probably there were conflicts when merging. The following should make it clear which files are affected:")
                lines.append("Please fix conflicts in the affected files (in a different terminal) and type 'resolved'. Or type 'abort' to abort the merge.")
                if self._UI.select("\n".join(lines),['resolved','abort']) == 'resolved':
                    self.git.silent.commit(a=True, no_edit=True)
                    self._UI.info("Created a commit from your conflict resolution.")
                else:
                    raise OperationCancelledError("user requested")
            except Exception as e:
                self.git.reset_to_clean_state()
                self.git.reset_to_clean_working_directory()
                raise

        if create_dependency:
            assert ticket and current_ticket
            dependencies = list(self._dependencies_for_ticket(current_ticket))
            if ticket in dependencies:
                self._UI.info("Not recording dependency on #{0} because #{1} already depends on #{0}.".format(ticket, current_ticket))
            else:
                self._UI.show("Added dependency on #{0} to #{1}.".format(ticket, current_ticket))
                self._set_dependencies_for_ticket(current_ticket, dependencies+[ticket])

    def local_tickets(self, include_abandoned=False):
        r"""
        Print the tickets currently being worked on in your local
        repository.

        This function shows the branch names as well as the ticket numbers for
        all active tickets.  It also shows local branches that are not
        associated to ticket numbers.

        INPUT:

        - ``include_abandoned`` -- boolean (default: ``False``), whether to
          include abandoned branches.

        .. SEEALSO::

        - :meth:`abandon_ticket` -- hide tickets from this method.

        - :meth:`remote_status` -- also show status compared to the
          trac server.

        - :meth:`current_ticket` -- get the current ticket.

        TESTS:

        Create a doctest setup with a single user::

            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()

        Create some tickets::

            sage: dev.local_tickets()
            : master

            sage: UI.append("Summary: summary\ndescription")
            sage: dev.create_ticket()
            1
            sage: UI.append("Summary: summary\ndescription")
            sage: dev.create_ticket()
            2
            sage: dev.local_tickets()
              : master
            #1: ticket/1
            #2: ticket/2
        branches = self.git.local_branches()
        branches = [ branch for branch in branches if include_abandoned or not self._is_trash_name(branch) ]
        if not branches:
            return
        branches = [ "{0:>7}: {1}".format("#"+str(self._ticket_for_local_branch(branch)) if self._has_ticket_for_local_branch(branch) else "", branch) for branch in branches ]
        while all([branch.startswith(' ') for branch in branches]):
            branches = [branch[1:] for branch in branches]
        branches = sorted(branches)
        self._UI.show("\n".join(branches))
    def vanilla(self, release=SAGE_VERSION):
        Returns to an official release of Sage.
        - ``release`` -- a string or decimal giving the release name.
          In fact, any tag, commit or branch will work.  If the tag
          does not exist locally an attempt to fetch it from the
          server will be made.

        Git equivalent::

            Checks out a given tag, commit or branch in detached head mode.

        .. SEEALSO::

        - :meth:`switch_ticket` -- switch to another branch, ready to
          develop on it.

        - :meth:`download` -- download a branch from the server and
          merge it.

        TESTS:

        Create a doctest setup with a single user::

            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()

        Go to a sage release::

            sage: dev.git.current_branch()
            'master'
            sage: dev.vanilla()
            sage: dev.git.current_branch()
            Traceback (most recent call last):
            ...
            DetachedHeadError: unexpectedly, git is in a detached HEAD state

        """
        if hasattr(release, 'literal'):
            release = release.literal

        try:
            self.reset_to_clean_state()
            self.reset_to_clean_working_directory()
        except OperationCancelledError:
            self._UI.error("Cannot switch to a release while your working directory is not clean.")
            raise OperationCancelledError("working directory not clean")

        # we do not do any checking on the argument here, trying to be liberal
        # about what are valid inputs
        try:
            self.git.super_silent.checkout(release, detach=True)
        except GitError as e:
            try:
                self.git.super_silent.fetch(self.git._repository, release)
            except GitError as e:
                self._UI.error("`{0}` does not exist locally or on the remote server.".format(release))
                raise OperationCancelledError("no such tag/branch/...")

            self.git.super_silent.checkout('FETCH_HEAD', detach=True)

    def diff(self, base='commit'):
        r"""
        Show how the current file system differs from ``base``.

        INPUT:

        - ``base`` -- a string; show the differences against the latest
          ``'commit'`` (the default), against the branch ``'master'`` (or any
          other branch name), or the merge of the ``'dependencies'`` of the
          current ticket (if the dependencies merge cleanly)

        .. SEEALSO::

        - :meth:`commit` -- record changes into the repository.

        - :meth:`local_tickets` -- list local tickets (you may want to commit
          your changes to a branch other than the current one).
        TESTS:
        Create a doctest setup with a single user::
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
        Create some tickets and make one depend on the others::
            sage: UI.append("Summary: summary\ndescription")
            sage: dev.create_ticket()
            1
            sage: UI.append("y")
            sage: dev.upload()
            The branch u/doctest/ticket/1 does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            sage: UI.append("Summary: summary\ndescription")
            sage: dev.create_ticket()
            2
            sage: UI.append("y")
            sage: dev.upload()
            The branch u/doctest/ticket/2 does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            sage: UI.append("Summary: summary\ndescription")
            sage: dev.create_ticket()
            3
            sage: UI.append("y")
            sage: dev.upload()
            The branch u/doctest/ticket/3 does not exist on the remote server yet. Do you want to create the branch? [Yes/no] y
            sage: dev.merge("#1")
            Merging the remote branch `u/doctest/ticket/1` into the local branch `ticket/3`.
            Added dependency on #1 to #3.
            sage: dev.merge("#2")
            Merging the remote branch `u/doctest/ticket/2` into the local branch `ticket/3`.
            Added dependency on #2 to #3.

        Make some non-conflicting changes on the tickets::

            sage: dev.switch_ticket("#1")
            sage: with open("ticket1","w") as f: f.write("ticket1")
            sage: dev.git.silent.add("ticket1")
            sage: dev.git.super_silent.commit(message="added ticket1")

            sage: dev.switch_ticket("#2")
            sage: with open("ticket2","w") as f: f.write("ticket2")
            sage: dev.git.silent.add("ticket2")
            sage: dev.git.super_silent.commit(message="added ticket2")
            sage: UI.append("y")
            sage: dev.upload()
            I will now upload the following new commits to the remote branch `u/doctest/ticket/2`:
            ...: added ticket2
            Is this what you want? [Yes/no] y

            sage: dev.switch_ticket("#3")
            sage: open("ticket3","w").close()
            sage: dev.git.silent.add("ticket3")
            sage: dev.git.super_silent.commit(message="added ticket3")
            sage: UI.append("y")
            sage: dev.upload()
            I will now upload the following new commits to the remote branch `u/doctest/ticket/3`:
            ...: added ticket3
            Is this what you want? [Yes/no] y

        A diff against the previous commit::

            sage: dev.diff()

        A diff against a ticket will always take the branch on trac::

            sage: dev.diff("#1")
            diff --git a/ticket3 b/ticket3
            new file mode ...
            index ...
            sage: dev.diff("ticket/1")
            diff --git a/ticket1 b/ticket1
            deleted file mode ...
            index ...
            diff --git a/ticket3 b/ticket3
            new file mode ...
            index ...
            sage: dev.switch_ticket("#1")
            sage: UI.append("y")
            sage: dev.upload()
            I will now upload the following new commits to the remote branch `u/doctest/ticket/1`:
            ...: added ticket1
            Is this what you want? [Yes/no] y
            sage: dev.switch_ticket("#3")
            sage: dev.diff("#1")
            diff --git a/ticket1 b/ticket1
            deleted file mode ...
            index ...
            diff --git a/ticket3 b/ticket3
            new file mode ...
            index ...

        A diff against the dependencies::

            sage: dev.diff("dependencies")
            Dependency #1 has not been merged into `ticket/3` (at least not its latest version). Use `...` to merge it.
            Dependency #2 has not been merged into `ticket/3` (at least not its latest version). Use `...` to merge it.
            diff --git a/ticket1 b/ticket1
            deleted file mode ...
            index ...
            diff --git a/ticket2 b/ticket2
            deleted file mode ...
            index ...
            diff --git a/ticket3 b/ticket3
            new file mode ...
            index ...
            sage: dev.merge("#1")
            Merging the remote branch `u/doctest/ticket/1` into the local branch `ticket/3`.
            sage: dev.merge("#2")
            Merging the remote branch `u/doctest/ticket/2` into the local branch `ticket/3`.
            sage: dev.diff("dependencies")
            diff --git a/ticket3 b/ticket3
            new file mode ...
            index ...

        This does not work if the dependencies do not merge::

            sage: dev.switch_ticket("#1")
            sage: with open("ticket2","w") as f: f.write("foo")
            sage: dev.git.silent.add("ticket2")
            sage: dev.git.super_silent.commit(message="added ticket2")
            sage: UI.append("y")
            sage: dev.upload()
            I will now upload the following new commits to the remote branch `u/doctest/ticket/1`:
            ...: added ticket2
            Is this what you want? [Yes/no] y

            sage: dev.switch_ticket("#3")
            sage: dev.diff("dependencies")
            Dependency #1 has not been merged into `ticket/3` (at least not its latest version). Use `sage --dev merge --ticket=1` to merge it.
            #2 does not merge cleanly with the other dependencies. Your diff could not be computed.
        """
        if base == "dependencies":
            current_ticket = self._current_ticket()
            if current_ticket is None:
                raise SageDevValueError("'dependencies' are only supported if currently on a ticket.")
            try:
                self.reset_to_clean_state()
                self.reset_to_clean_working_directory()
            except OperationCancelledError:
                self._UI.error("Cannot create merge of dependencies because working directory is not clean.")
                raise
            branch = self.git.current_branch()
            temporary_branch = self._new_local_branch_for_trash("diff")
            self.git.super_silent.branch(temporary_branch, MASTER_BRANCH)
            try:
                self.git.super_silent.checkout(temporary_branch)
                try:
                    self._UI.info("Merging dependencies of #{0}.".format(current_ticket))
                    for dependency in self._dependencies_for_ticket(current_ticket):
                        self._check_ticket_name(dependency, exists=True)
                        remote_branch = self.trac._branch_for_ticket(dependency)
                        self._check_remote_branch_name(remote_branch, exists=True)
                        self.git.super_silent.fetch(self.git._repository, remote_branch)
                        if self.git.is_child_of(MASTER_BRANCH, 'FETCH_HEAD'):
                            self._UI.info("Dependency #{0} has already been merged into the master branch.".format(dependency))
                        else:
                            if not self.git.is_child_of(branch, 'FETCH_HEAD'):
                                self._UI.warning("Dependency #{0} has not been merged into `{1}` (at least not its latest version). Use `{2}` to merge it.".format(dependency, branch, self._format_command("merge",ticket_or_branch="{0}".format(dependency))))
                            from git_error import GitError
                            try:
                                self.git.super_silent.merge('FETCH_HEAD')
                            except GitError as e:
                                self._UI.error("#{0} does not merge cleanly with the other dependencies. Your diff could not be computed.".format(dependency))
                                raise OperationCancelledError("merge failed")

                    self.git.echo.diff("{0}..{1}".format(temporary_branch, branch))
                    return
                finally:
                    self.git.reset_to_clean_state()
                    self.git.reset_to_clean_working_directory()
                    self.git.super_silent.checkout(branch)
            finally:
                self.git.super_silent.branch("-D", temporary_branch)
        if base == "commit":
            base = "HEAD"
            if self._is_ticket_name(base):
                ticket = self._ticket_from_ticket_name(base)
                self._check_ticket_name(ticket, exists=True)
                base = self.trac._branch_for_ticket(ticket)
                if base is None:
                    self._UI.error("Ticket #{0} has no branch set on trac.".format(ticket))

            if self._is_local_branch_name(base, exists=True):
                pass
            else:
                self._check_remote_branch_name(base, exists=True)
                self.git.super_silent.fetch(self.git._repository, base)
                base = 'FETCH_HEAD'

        self.git.echo.diff(base)
        Create a doctest setup with a single user::
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
        Create some tickets and add dependencies::
            sage: UI.append("Summary: summary\ndescription")
            sage: dev.create_ticket()
            1
            sage: UI.append("Summary: summary\ndescription")
            sage: dev.create_ticket()
            2
            sage: UI.append("Summary: summary\ndescription")
            sage: dev.create_ticket()
            3
            sage: UI.append("Summary: summary\ndescription")
            sage: dev.create_ticket()
            4
            sage: dev.merge('ticket/2',create_dependency=True)
            Merging the local branch `ticket/2` into the local branch `ticket/4`.
            Added dependency on #2 to #4.
            sage: dev.merge('ticket/3',create_dependency=True)
            Merging the local branch `ticket/3` into the local branch `ticket/4`.
            Added dependency on #3 to #4.
            sage: dev.switch_ticket('#2')
            sage: dev.merge('ticket/1', create_dependency=True)
            Merging the local branch `ticket/1` into the local branch `ticket/2`.
            Added dependency on #1 to #2.
            sage: dev.switch_ticket('#3')
            sage: dev.merge('ticket/1', create_dependency=True)
            Merging the local branch `ticket/1` into the local branch `ticket/3`.
            Added dependency on #1 to #3.

        Check that the dependencies show correctly::

            sage: dev.switch_ticket('#4')
            sage: dev.show_dependencies()
            Ticket #4 depends on #2, #3.
            sage: dev.show_dependencies('#4')
            Ticket #4 depends on #2, #3.
            sage: dev.show_dependencies('#3')
            Ticket #3 depends on #1.
            sage: dev.show_dependencies('#2')
            Ticket #2 depends on #1.
            sage: dev.show_dependencies('#1')
            Ticket #1 has no dependencies.
            sage: dev.show_dependencies('#4', all=True)
            Ticket #4 depends on #3, #1, #2.
        if ticket is None:
            ticket = self._current_ticket()
        if ticket is None:
            raise SageDevValueError("ticket must be specified")
        self._check_ticket_name(ticket)
        ticket = self._ticket_from_ticket_name(ticket)
        if not self._has_local_branch_for_ticket(ticket):
            raise SageDevValueError("ticket must be a ticket with a local branch. Use `{0}` to download the ticket first.".format(self._format_command("switch_ticket",ticket=ticket)))
        branch = self._local_branch_for_ticket(ticket)
        if all:
            ret = []
            stack = [ticket]
            while stack:
                t = stack.pop()
                if t in ret: continue
                ret.append(t)
                if not self._has_local_branch_for_ticket(t):
                    self._UI.warning("no local branch for ticket #{0} present, some dependencies might be missing in the output.".format(t))
                    continue
                deps = self._dependencies_for_ticket(t)
                for d in deps:
                    if d not in stack and d not in ret:
                        stack.append(d)
            ret = ret[1:]
            ret = self._dependencies_for_ticket(ticket)
        if ret:
            self._UI.show("Ticket #{0} depends on {1}.".format(ticket,", ".join(["#{0}".format(d) for d in ret])))
        else:
            self._UI.show("Ticket #{0} has no dependencies.".format(ticket))
        TESTS::
            sage: dev = dev._sagedev
            Traceback (most recent call last):
            ...
            SageDevValueError: File appears to have mixed diff formats.
        r"""
        Return a list of files which are modified by the patch in ``lines``.

        TESTS::

            sage: dev._wrap("_detect_patch_modified_files")
            sage: import os.path
            sage: from sage.env import SAGE_SRC
            sage: dev._detect_patch_modified_files(
            ....:     open(os.path.join(
            ....:             SAGE_SRC,"sage","dev","test","data","trac_8703-trees-fh.patch"
            ....:         )).read().splitlines())
            ['ordered_tree.py', 'binary_tree.pyx', 'list_clone.pyx', 'permutation.py', 'index.rst', 'abstract_tree.py', 'all.py', 'binary_tree.py']

        """
                subject = 'No Subject. Modified: %s'%(", ".join(sorted(self._detect_patch_modified_files(lines))))
        r"""
        Rewrite the patch in ``lines`` to the path format given in
        ``to_path_format`` and the header format given in ``to_header_format``.

        TESTS::

            sage: dev._wrap("_rewrite_patch")
            sage: import os.path
            sage: from sage.env import SAGE_SRC
            sage: git_lines = open(
            ....:     os.path.join(SAGE_SRC, "sage", "dev", "test", "data", "git.patch")
            ....:     ).read().splitlines()
            sage: dev._rewrite_patch(git_lines, "new", "git") == git_lines
            True

        """
    def upload_ssh_key(self, public_key=None, create_key_if_not_exists=True):
        Upload ``public_key`` to gitolite through the trac interface.
        - ``public_key`` -- a string or ``None`` (default: ``None``), the path
          of the key file, defaults to ``~/.ssh/id_rsa.pub``.
        - ``create_key_if_not_exists`` -- use ``ssh-keygen`` to create a public
          if key if none exists.
        TESTS:
        Create a doctest setup with a single user::
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
        Create and upload a key file::
            sage: import os
            sage: public_key = os.path.join(dev._sagedev.tmp_dir,"id_rsa.pub")
            sage: dev.upload_ssh_key(public_key=public_key, create_key_if_not_exists=False)
            ValueError: create_key_if_not_exists is not set but there is no key at ....
            sage: dev.upload_ssh_key(public_key=public_key, create_key_if_not_exists=True)
            Generating ssh key.
            Your key has been uploaded.
            sage: dev.upload_ssh_key(public_key=public_key, create_key_if_not_exists=False)
            Your key has been uploaded.
        """
        import os
        if public_key is None:
            public_key = os.path.expanduser("~/.ssh/id_rsa.pub")

        if not os.path.exists(public_key):
            if not create_key_if_not_exists:
                raise SageDevValueError("create_key_if_not_exists is not set but there is no key at {0}.".format(public_key))
            self._UI.show("Generating ssh key.")
            from subprocess import call
            success = call(["ssh-keygen", "-q", "-f", public_key, "-P", ""])
            if success == 0:
                self._UI.info("Key generated.")
                self._UI.error("Key generation failed.")
                self._UI.info("Please create a key in `{0}` and retry.".format(public_key))
                raise OperationCancelledError("ssh-keygen failed")
        with open(public_key, 'r') as F:
            public_key = F.read().strip()
        self.trac._authenticated_server_proxy.sshkeys.addkey(public_key)
        self._UI.show("Your key has been uploaded.")
            sage: dev._is_ticket_name('')
            False
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()

            if isinstance(ticket, str) and ticket and ticket[0] == "#":
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev = dev._sagedev
            sage: dev.git.silent.branch('ticket/1')
        # branches which could be tickets are calling for trouble - cowardly refuse to accept them
        if self._is_ticket_name(name):
            return False
    def _is_trash_name(self, name, exists=any):
        r"""
        Return whether ``name`` is a valid name for an abandoned branch.

        INPUT:

        - ``name`` -- a string

        - ``exists`` - a boolean or ``any`` (default: ``any``), if ``True``,
          check whether ``name`` is the name of an existing branch; if
          ``False``, check whether ``name`` is the name of a branch that does
          not exist yet.

        TESTS::

            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev = dev._sagedev

            sage: dev._is_trash_name("branch1")
            False
            sage: dev._is_trash_name("trash")
            False
            sage: dev._is_trash_name("trash/")
            False
            sage: dev._is_trash_name("trash/1")
            True
            sage: dev._is_trash_name("trash/1", exists=True)
            False

        """
        if not isinstance(name, str):
            raise ValueError("name must be a string")

        if not name.startswith("trash/"):
            return False

        return self._is_local_branch_name(name, exists)

            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev = dev._sagedev
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev = dev._sagedev
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev = dev._sagedev
        # branches which could be tickets are calling for trouble - cowardly refuse to accept them
        if self._is_ticket_name(name):
            return False
            self.git.super_silent.ls_remote(self.git._repository, name, exit_code=True)
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev = dev._sagedev
            sage: dev.git.silent.branch('ticket/1')
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev = dev._sagedev
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev = dev._sagedev
            sage: UI.append("Summary: summary1\ndescription")
    def _ticket_for_local_branch(self, branch):
        r"""
        Return the ticket associated to the local ``branch``.

        INPUT:

        - ``branch`` -- a string, the name of a local branch

        TESTS::

            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: UI.append("Summary: summary\ndescription")
            sage: dev.create_ticket()
            1
            sage: dev._sagedev._ticket_for_local_branch("ticket/1")
            1

        """
        self._check_local_branch_name(branch, exists=True)

        if not self._has_ticket_for_local_branch(branch):
            raise SageDevValueError("branch must be associated to a ticket")

        return self.__branch_to_ticket[branch]

    def _has_ticket_for_local_branch(self, branch):
        r"""
        Return whether ``branch`` is associated to a ticket.

        INPUT:

        - ``branch`` -- a string, the name of a local branch

        TESTS::

            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: UI.append("Summary: summary\ndescription")
            sage: dev.create_ticket()
            1
            sage: dev._sagedev._has_ticket_for_local_branch("ticket/1")
            True

        """
        self._check_local_branch_name(branch, exists=True)

        return branch in self.__branch_to_ticket

            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev._sagedev._has_local_branch_for_ticket(1)
            sage: from sage.dev.test.sagedev import two_user_setup
            sage: alice, config_alice, bob, config_bob, server = two_user_setup()
            sage: alice._chdir()
            sage: alice._UI.append("Summary: ticket1\ndescription")
            sage: ticket = alice.create_ticket()
            sage: alice._sagedev._local_branch_for_ticket(ticket)
            sage: bob._chdir()
            sage: bob._sagedev._local_branch_for_ticket(ticket)
            sage: bob._sagedev._local_branch_for_ticket(ticket, download_if_not_found=True)
            sage: attributes = alice.trac._get_attributes(ticket)
            sage: alice.trac._authenticated_server_proxy.ticket.update(ticket, "", attributes)
            sage: bob._sagedev._local_branch_for_ticket(ticket, download_if_not_found=True)
            sage: server.git.silent.branch('public/ticket/1')
            sage: bob._chdir()
            sage: bob._sagedev._local_branch_for_ticket(ticket, download_if_not_found=True)
            sage: bob._sagedev._local_branch_for_ticket(ticket)
    def _new_local_branch_for_trash(self, branch):
        r"""
        Return a new local branch name to trash ``branch``.

        TESTS::

            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev = dev._sagedev

            sage: dev._new_local_branch_for_trash('branch')
            'trash/branch'
            sage: dev.git.silent.branch('trash/branch')
            sage: dev._new_local_branch_for_trash('branch')
            'trash/branch_'

        """
        while True:
            trash_branch = 'trash/{0}'.format(branch)
            if self._is_trash_name(trash_branch, exists=False):
                return trash_branch
            branch = branch + "_"

            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev = dev._sagedev
            sage: dev.git.silent.branch('stash/1')
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev = dev._sagedev
            sage: dev.git.silent.branch('ticket/1')
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev = dev._sagedev

            sage: UI.append("Summary: ticket1\ndescription")
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev = dev._sagedev

            sage: UI.append("Summary: ticket1\ndescription")
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev = dev._sagedev
            sage: dev.git.silent.branch('ticket/1')
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev = dev._sagedev
            sage: dev.git.silent.branch('ticket/1')
        if branch == MASTER_BRANCH:
            return MASTER_BRANCH
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev = dev._sagedev
            sage: dev.git.silent.branch('ticket/1')
            kwargs = [ "--{0}={1}".format(str(key.split("_or_")[0]).replace("_","-"),kwargs[key]) for key in kwargs ]
            sage: from sage.dev.test.sagedev import single_user_setup
            sage: dev, config, UI, server = single_user_setup()
            sage: dev = dev._sagedev
            sage: UI.append("Summary: ticket1\ndescription")
        sage: from sage.dev.test.sagedev import single_user_setup
        sage: dev, config, UI, server = single_user_setup()
