# TEST
# odoo.define('lead.opportunity_examples', function (odoo.require) {
# 'use strict';

# var core = require('web.core');
# var kanbanExamplesRegistry = require('web.kanban_examples_registry');

# var _t = core._t;

# /**
#  * Helper function to escape a text before formatting it.
#  *
#  * First argument is the string to format and the other arguments are the values
#  * to inject into the string.
#  *
#  * @returns {string} the formatted and escaped string
#  */
# function escFormat() {
#     arguments[0] = _.escape(arguments[0]);
#     return _.str.sprintf.apply(_.str, arguments);
# }

# kanbanExamplesRegistry.add('opportunity', [{
#     name: _t('Opportunities'),
#     stage_id: [_t('Assessment'), _t('Prospect'), _t('Win'), _t('Lost')],
# }])

# })