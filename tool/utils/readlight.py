import json


class Lighthouseraport():
    def __init__(self,path):
        self.path = path
        self.raport = self.readfile(path)

    def readfile(self,path):
        filejson = path
        with open(filejson, 'r', encoding='UTF-8') as read_file:
            data = json.load(read_file)
            return data

    def readproperty(self,property):
        properties = ['is-on-https','redirects-http', 'service-worker', 'works-offline', 'without-javascript', 'first-contentful-paint',
                      'first-meaningful-paint', 'load-fast-enough-for-pwa', 'speed-index', 'screenshot-thumbnails',
                      'final-screenshot', 'estimated-input-latency', 'errors-in-console', 'time-to-first-byte', 'first-cpu-idle',
                      'interactive', 'user-timings', 'critical-request-chains', 'redirects', 'webapp-install-banner',
                      'splash-screen', 'themed-omnibox','manifest-short-name-length', 'content-width', 'image-aspect-ratio',
                      'deprecations', 'mainthread-work-breakdown', 'bootup-time', 'uses-rel-preload', 'uses-rel-preconnect',
                      'font-display', 'network-requests', 'metrics', 'pwa-cross-browser', 'pwa-page-transitions',
                      'pwa-each-page-has-url', 'accesskeys', 'aria-allowed-attr', 'aria-required-attr', 'aria-required-children',
                      'aria-required-parent', 'aria-roles', 'aria-valid-attr-value', 'aria-valid-attr', 'audio-caption', 'button-name',
                      'bypass', 'color-contrast', 'definition-list', 'dlitem', 'document-title', 'duplicate-id', 'frame-title',
                      'html-has-lang', 'html-lang-valid', 'image-alt', 'input-image-alt', 'label', 'layout-table', 'link-name',
                      'list', 'listitem', 'meta-refresh', 'meta-viewport', 'object-alt', 'tabindex', 'td-headers-attr',
                      'th-has-data-cells', 'valid-lang', 'video-caption', 'video-description', 'custom-controls-labels',
                      'custom-controls-roles', 'focus-traps', 'focusable-controls', 'heading-levels', 'interactive-element-affordance',
                      'logical-tab-order', 'managed-focus', 'offscreen-content-hidden', 'use-landmarks', 'visual-order-follows-dom',
                      'uses-long-cache-ttl', 'total-byte-weight', 'offscreen-images', 'render-blocking-resources', 'unminified-css',
                      'unminified-javascript', 'unused-css-rules', 'uses-webp-images', 'uses-optimized-images', 'uses-text-compression',
                      'uses-responsive-images', 'efficient-animated-content', 'appcache-manifest', 'doctype', 'dom-size',
                      'external-anchors-use-rel-noopener', 'geolocation-on-start', 'no-document-write', 'no-vulnerable-libraries',
                      'js-libraries', 'no-websql', 'notification-on-start', 'password-inputs-can-be-pasted-into', 'uses-http2',
                      'uses-passive-event-listeners', 'meta-description', 'http-status-code', 'font-size', 'link-text',
                      'is-crawlable', 'robots-txt', 'hreflang', 'plugins', 'canonical', 'mobile-friendly', 'structured-data']
        if property not in properties:
            return 'Błędny parametr'

        return self.raport['audits'][property]




            # first_meaningful_paint = data['audits']['first-meaningful-paint']
            # estimated_input_latency = data['audits']['estimated-input-latency']
            # errors_in_console = data['audits']['errors-in-console']
            # time_to_first_byte = data['audits']['time-to-first-byte']
            # first_cpu_idle = data['audits']['first-cpu-idle']
            # interactive = data['audits']['interactive']
            # user_timings= data['audits']['user-timings']
            # critical_request_chains = data['audits']['critical-request-chains']
            # redirects = data['audits']['redirects']
            #
            # uses_rel_preload = data['audits']['uses-rel-preload']
            # uses_rel_preconnect= data['audits']['uses-rel-preconnect']
            # font_display = data['audits']['font-display']
            # network_requests = data['audits']['network-requests']
            # image_alt = data['audits']['image-alt']
            #
            # uses_webp_images = data['audits']['uses-webp-images']
            # uses_optimized_images= data['audits']['uses-optimized-images']
            # uses_text_compression= data['audits']['uses-text-compression']
            # uses_responsive_images = data['audits']['uses-responsive-images']
            # external_anchors_use_rel_noopener = data['audits']['external-anchors-use-rel-noopener']


# raport = Lighthouseraport('E:\lighthouse\\axa.pl\\5-10-2018\\axa.pl.json')
# print(raport.readproperty('uses-responsive-images'))