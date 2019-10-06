from nornir.core.task import Result, Task


def netconf_capabilities(task: Task) -> Result:
    """
    Gather Netconf capabilities from device
    """
    manager = task.host.get_connection("netconf", task.nornir.config)
    capabilities = [capability for capability in manager.server_capabilities]
    return Result(host=task.host, result=capabilities)
