from dateutil.parser import isoparse

from hcloud.core.domain import BaseDomain, DomainIdentityMixin


class Volume(BaseDomain, DomainIdentityMixin):
    """Volume Domain

    :param id: int
           ID of the Volume
    :param name: str
           Name of the Volume
    :param server: :class:`BoundServer <hcloud.servers.client.BoundServer>`, None
           Server the Volume is attached to, None if it is not attached at all.
    :param created: datetime
           Point in time when the Volume was created
    :param location: :class:`BoundLocation <hcloud.locations.client.BoundLocation>`
           Location of the Volume. Volume can only be attached to Servers in the same location.
    :param size: int
           Size in GB of the Volume
    :param linux_device: str
           Device path on the file system for the Volume
    :param protection: dict
           Protection configuration for the Volume
    :param labels: dict
           User-defined labels (key-value pairs)
    :param status: str
           Current status of the volume Choices: `creating`, `available`
    :param format: str, None
           Filesystem of the volume if formatted on creation, None if not formatted on creation.
    """

    STATUS_CREATING = "creating"
    """Volume Status creating"""
    STATUS_AVAILABLE = "available"
    """Volume Status available"""

    __slots__ = (
        "id",
        "name",
        "server",
        "location",
        "size",
        "linux_device",
        "format",
        "protection",
        "labels",
        "status",
        "created",
    )

    def __init__(
        self,
        id,
        name=None,
        server=None,
        created=None,
        location=None,
        size=None,
        linux_device=None,
        format=None,
        protection=None,
        labels=None,
        status=None,
    ):
        self.id = id
        self.name = name
        self.server = server
        self.created = isoparse(created) if created else None
        self.location = location
        self.size = size
        self.linux_device = linux_device
        self.format = format
        self.protection = protection
        self.labels = labels
        self.status = status


class CreateVolumeResponse(BaseDomain):
    """Create Volume Response Domain

    :param volume: :class:`BoundVolume <hcloud.volumes.client.BoundVolume>`
           The created volume
    :param action: :class:`BoundAction <hcloud.actions.client.BoundAction>`
           The action that shows the progress of the Volume Creation
    :param next_actions: List[:class:`BoundAction <hcloud.actions.client.BoundAction>`]
           List of actions that are performed after the creation, like attaching to a server
    """

    __slots__ = ("volume", "action", "next_actions")

    def __init__(
        self,
        volume,  # type: BoundVolume
        action,  # type: BoundAction
        next_actions,  # type: List[BoundAction]
    ):
        self.volume = volume
        self.action = action
        self.next_actions = next_actions
