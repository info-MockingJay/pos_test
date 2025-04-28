/** @odoo-module **/

import { PartnerLine } from "@point_of_sale/app/screens/partner_list/partner_line/partner_line";
import { patch } from "@web/core/utils/patch";

patch(PartnerLine.prototype, {
    get highlight() {
        var self = this;
        var dateOfBirth = []
        self.env.services.pos.partner.forEach(function(items){
            var partner = items.partner_ids
            partner.forEach(function(item){
                if (self.props.partner.id == item){
                    dateOfBirth.push(items.date_of_birth)
                }
            });
        });
        this.props.partner['date_of_birth'] = dateOfBirth
    },
});