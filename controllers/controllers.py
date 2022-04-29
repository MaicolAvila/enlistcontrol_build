from odoo import http


class EnlistControlRender(http.Controller):
    @http.route(['/enlistcontrol'], auth="public", website=True)
    def portal_home_index(self, **kw):
        return http.request.render("enlistcontrol_build.enlist_control_build")
