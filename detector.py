from ryu.base import app_manager
from ryu.controller.handler import set_ev_cls
from ryu.topology import event

class TopologyDetector(app_manager.RyuApp):
    def __init__(self, *args, **kwargs):
        super(TopologyDetector, self).__init__(*args, **kwargs)
        self.name = 'topology_detector'

    @set_ev_cls(event.EventSwitchEnter)
    def switch_enter_handler(self, ev):
        switch = ev.switch.dp
        self.logger.info("Switch connected: %s", switch.id)

    @set_ev_cls(event.EventSwitchLeave)
    def switch_leave_handler(self, ev):
        switch = ev.switch.dp
        self.logger.info("Switch disconnected: %s", switch.id)

    @set_ev_cls(event.EventLinkAdd)
    def link_add_handler(self, ev):
        link = ev.link
        self.logger.info("Link Up: s%s (port %s) <-> s%s (port %s)", 
                         link.src.dpid, link.src.port_no, link.dst.dpid, link.dst.port_no)

    @set_ev_cls(event.EventLinkDelete)
    def link_delete_handler(self, ev):
        link = ev.link
        self.logger.info("Link Down: s%s (port %s) <-> s%s (port %s)", 
                         link.src.dpid, link.src.port_no, link.dst.dpid, link.dst.port_no)
