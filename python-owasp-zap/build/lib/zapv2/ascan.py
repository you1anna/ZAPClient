# Zed Attack Proxy (ZAP) and its related class files.
#
# ZAP is an HTTP/HTTPS proxy for assessing web application security.
#
# Copyright 2015 the ZAP development team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
This file was automatically generated.
"""

class ascan(object):

    def __init__(self, zap):
        self.zap = zap

    def status(self, scanid=None):
        params = {}
        if scanid is not None:
            params['scanId'] = scanid
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/status/', params).values()))

    def scan_progress(self, scanid=None):
        params = {}
        if scanid is not None:
            params['scanId'] = scanid
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/scanProgress/', params).values()))

    def messages_ids(self, scanid):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/messagesIds/', {'scanId' : scanid}).values()))

    def alerts_ids(self, scanid):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/alertsIds/', {'scanId' : scanid}).values()))

    @property
    def scans(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/scans/').values()))

    @property
    def scan_policy_names(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/scanPolicyNames/').values()))

    @property
    def excluded_from_scan(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/excludedFromScan/').values()))

    def scanners(self, scanpolicyname=None, policyid=None):
        params = {}
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        if policyid is not None:
            params['policyId'] = policyid
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/scanners/', params).values()))

    def policies(self, scanpolicyname=None, policyid=None):
        params = {}
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        if policyid is not None:
            params['policyId'] = policyid
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/policies/', params).values()))

    @property
    def attack_mode_queue(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/attackModeQueue/').values()))

    @property
    def option_attack_policy(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/optionAttackPolicy/').values()))

    @property
    def option_default_policy(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/optionDefaultPolicy/').values()))

    @property
    def option_delay_in_ms(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/optionDelayInMs/').values()))

    @property
    def option_excluded_param_list(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/optionExcludedParamList/').values()))

    @property
    def option_handle_anti_csrf_tokens(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/optionHandleAntiCSRFTokens/').values()))

    @property
    def option_host_per_scan(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/optionHostPerScan/').values()))

    @property
    def option_max_chart_time_in_mins(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/optionMaxChartTimeInMins/').values()))

    @property
    def option_max_results_to_list(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/optionMaxResultsToList/').values()))

    @property
    def option_max_scans_in_ui(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/optionMaxScansInUI/').values()))

    @property
    def option_target_params_enabled_rpc(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/optionTargetParamsEnabledRPC/').values()))

    @property
    def option_target_params_injectable(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/optionTargetParamsInjectable/').values()))

    @property
    def option_thread_per_host(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/optionThreadPerHost/').values()))

    @property
    def option_allow_attack_on_start(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/optionAllowAttackOnStart/').values()))

    @property
    def option_inject_plugin_id_in_header(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/optionInjectPluginIdInHeader/').values()))

    @property
    def option_prompt_in_attack_mode(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/optionPromptInAttackMode/').values()))

    @property
    def option_prompt_to_clear_finished_scans(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/optionPromptToClearFinishedScans/').values()))

    @property
    def option_rescan_in_attack_mode(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/optionRescanInAttackMode/').values()))

    @property
    def option_show_advanced_dialog(self):
        return next(iter(self.zap._request(self.zap.base + 'ascan/view/optionShowAdvancedDialog/').values()))

    def scan(self, url, recurse=None, inscopeonly=None, scanpolicyname=None, method=None, postdata=None, apikey=''):
        params = {'url' : url, 'apikey' : apikey}
        if recurse is not None:
            params['recurse'] = recurse
        if inscopeonly is not None:
            params['inScopeOnly'] = inscopeonly
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        if method is not None:
            params['method'] = method
        if postdata is not None:
            params['postData'] = postdata
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/scan/', params).values()))

    def scan_as_user(self, url, contextid, userid, recurse=None, scanpolicyname=None, method=None, postdata=None, apikey=''):
        """
        Active Scans from the perspective of a User, obtained using the given Context ID and User ID. See 'scan' action for more details.
        """
        params = {'url' : url, 'contextId' : contextid, 'userId' : userid, 'apikey' : apikey}
        if recurse is not None:
            params['recurse'] = recurse
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        if method is not None:
            params['method'] = method
        if postdata is not None:
            params['postData'] = postdata
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/scanAsUser/', params).values()))

    def pause(self, scanid, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/pause/', {'scanId' : scanid, 'apikey' : apikey}).values()))

    def resume(self, scanid, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/resume/', {'scanId' : scanid, 'apikey' : apikey}).values()))

    def stop(self, scanid, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/stop/', {'scanId' : scanid, 'apikey' : apikey}).values()))

    def remove_scan(self, scanid, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/removeScan/', {'scanId' : scanid, 'apikey' : apikey}).values()))

    def pause_all_scans(self, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/pauseAllScans/', {'apikey' : apikey}).values()))

    def resume_all_scans(self, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/resumeAllScans/', {'apikey' : apikey}).values()))

    def stop_all_scans(self, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/stopAllScans/', {'apikey' : apikey}).values()))

    def remove_all_scans(self, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/removeAllScans/', {'apikey' : apikey}).values()))

    def clear_excluded_from_scan(self, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/clearExcludedFromScan/', {'apikey' : apikey}).values()))

    def exclude_from_scan(self, regex, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/excludeFromScan/', {'regex' : regex, 'apikey' : apikey}).values()))

    def enable_all_scanners(self, scanpolicyname=None, apikey=''):
        params = {'apikey' : apikey}
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/enableAllScanners/', params).values()))

    def disable_all_scanners(self, scanpolicyname=None, apikey=''):
        params = {'apikey' : apikey}
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/disableAllScanners/', params).values()))

    def enable_scanners(self, ids, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/enableScanners/', {'ids' : ids, 'apikey' : apikey}).values()))

    def disable_scanners(self, ids, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/disableScanners/', {'ids' : ids, 'apikey' : apikey}).values()))

    def set_enabled_policies(self, ids, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setEnabledPolicies/', {'ids' : ids, 'apikey' : apikey}).values()))

    def set_policy_attack_strength(self, id, attackstrength, scanpolicyname=None, apikey=''):
        params = {'id' : id, 'attackStrength' : attackstrength, 'apikey' : apikey}
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setPolicyAttackStrength/', params).values()))

    def set_policy_alert_threshold(self, id, alertthreshold, scanpolicyname=None, apikey=''):
        params = {'id' : id, 'alertThreshold' : alertthreshold, 'apikey' : apikey}
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setPolicyAlertThreshold/', params).values()))

    def set_scanner_attack_strength(self, id, attackstrength, scanpolicyname=None, apikey=''):
        params = {'id' : id, 'attackStrength' : attackstrength, 'apikey' : apikey}
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setScannerAttackStrength/', params).values()))

    def set_scanner_alert_threshold(self, id, alertthreshold, scanpolicyname=None, apikey=''):
        params = {'id' : id, 'alertThreshold' : alertthreshold, 'apikey' : apikey}
        if scanpolicyname is not None:
            params['scanPolicyName'] = scanpolicyname
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setScannerAlertThreshold/', params).values()))

    def add_scan_policy(self, scanpolicyname, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/addScanPolicy/', {'scanPolicyName' : scanpolicyname, 'apikey' : apikey}).values()))

    def remove_scan_policy(self, scanpolicyname, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/removeScanPolicy/', {'scanPolicyName' : scanpolicyname, 'apikey' : apikey}).values()))

    def set_option_attack_policy(self, string, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setOptionAttackPolicy/', {'String' : string, 'apikey' : apikey}).values()))

    def set_option_default_policy(self, string, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setOptionDefaultPolicy/', {'String' : string, 'apikey' : apikey}).values()))

    def set_option_allow_attack_on_start(self, boolean, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setOptionAllowAttackOnStart/', {'Boolean' : boolean, 'apikey' : apikey}).values()))

    def set_option_delay_in_ms(self, integer, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setOptionDelayInMs/', {'Integer' : integer, 'apikey' : apikey}).values()))

    def set_option_handle_anti_csrf_tokens(self, boolean, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setOptionHandleAntiCSRFTokens/', {'Boolean' : boolean, 'apikey' : apikey}).values()))

    def set_option_host_per_scan(self, integer, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setOptionHostPerScan/', {'Integer' : integer, 'apikey' : apikey}).values()))

    def set_option_inject_plugin_id_in_header(self, boolean, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setOptionInjectPluginIdInHeader/', {'Boolean' : boolean, 'apikey' : apikey}).values()))

    def set_option_max_chart_time_in_mins(self, integer, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setOptionMaxChartTimeInMins/', {'Integer' : integer, 'apikey' : apikey}).values()))

    def set_option_max_results_to_list(self, integer, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setOptionMaxResultsToList/', {'Integer' : integer, 'apikey' : apikey}).values()))

    def set_option_max_scans_in_ui(self, integer, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setOptionMaxScansInUI/', {'Integer' : integer, 'apikey' : apikey}).values()))

    def set_option_prompt_in_attack_mode(self, boolean, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setOptionPromptInAttackMode/', {'Boolean' : boolean, 'apikey' : apikey}).values()))

    def set_option_prompt_to_clear_finished_scans(self, boolean, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setOptionPromptToClearFinishedScans/', {'Boolean' : boolean, 'apikey' : apikey}).values()))

    def set_option_rescan_in_attack_mode(self, boolean, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setOptionRescanInAttackMode/', {'Boolean' : boolean, 'apikey' : apikey}).values()))

    def set_option_show_advanced_dialog(self, boolean, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setOptionShowAdvancedDialog/', {'Boolean' : boolean, 'apikey' : apikey}).values()))

    def set_option_target_params_enabled_rpc(self, integer, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setOptionTargetParamsEnabledRPC/', {'Integer' : integer, 'apikey' : apikey}).values()))

    def set_option_target_params_injectable(self, integer, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setOptionTargetParamsInjectable/', {'Integer' : integer, 'apikey' : apikey}).values()))

    def set_option_thread_per_host(self, integer, apikey=''):
        return next(iter(self.zap._request(self.zap.base + 'ascan/action/setOptionThreadPerHost/', {'Integer' : integer, 'apikey' : apikey}).values()))


