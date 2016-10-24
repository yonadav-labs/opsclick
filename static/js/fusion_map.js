/**
 * Fusion Maps
 */
(function(d, l, h, m) {
    function e(a, c) { this.element = a;
        this.settings = d.extend({}, k, c);
        this._defaults = k;
        this._name = "fusion_maps";
        this.geocoder = new google.maps.Geocoder;
        this.next_address = 0;
        this.infowindow = new google.maps.InfoWindow;
        this.markers = [];
        this.init() }
    var k = {
        addresses: {},
        address_pin: !0,
        animations: !0,
        delay: 10,
        infobox_background_color: !1,
        infobox_styling: "default",
        infobox_text_color: !1,
        map_style: "default",
        map_type: "roadmap",
        marker_icon: !1,
        overlay_color: !1,
        overlay_color_hsl: {},
        pan_control: !0,
        show_address: !0,
        scale_control: !0,
        scrollwheel: !0,
        zoom: 9,
        zoom_control: !0
    };
    d.extend(e.prototype, {
        init: function() {
            var a = { zoom: this.settings.zoom, mapTypeId: this.settings.map_type, scrollwheel: this.settings.scrollwheel, scaleControl: this.settings.scale_control, panControl: this.settings.pan_control, zoomControl: this.settings.zoom_control },
                c;
            c = 640 < d(h).width() ? !0 : !1;
            this.settings.scrollwheel && (a.draggable = c);
            this.settings.address_pin || (this.settings.addresses = [this.settings.addresses[0]]);
            this.settings.addresses = this.settings.addresses.reverse();
            this.settings.addresses[0].coordinates && (c = new google.maps.LatLng(this.settings.addresses[0].latitude, this.settings.addresses[0].longitude), a.center = c);
            this.map = new google.maps.Map(this.element, a);
            this.settings.overlay_color && "custom" == this.settings.map_style && (a = [{ stylers: [{ hue: this.settings.overlay_color }, { lightness: 2 * this.settings.overlay_color_hsl.lum - 100 }, { saturation: 2 * this.settings.overlay_color_hsl.sat - 100 }] }, { featureType: "road", elementType: "geometry", stylers: [{ visibility: "simplified" }] }, {
                featureType: "road",
                elementType: "labels"
            }], this.map.setOptions({ styles: a }));
            this.next_geocode_request()
        },
        geocode_address: function(a) {
            var c = this,
                b;
            b = !0 === a.coordinates ? { latLng: new google.maps.LatLng(a.latitude, a.longitude) } : { address: a.address };
            this.geocoder.geocode(b, function(b, d) {
                var f, g;
                d == google.maps.GeocoderStatus.OK ? (g = b[0].geometry.location, f = g.lat(), g = g.lng(), !0 === a.coordinates && "" === a.infobox_content && (a.geocoded_address = b[0].formatted_address), 1 != c.next_address || a.coordinates || c.map.setCenter(b[0].geometry.location),
                    c.settings.address_pin && c.create_marker(a, f, g), c.map.setCenter(b[0].geometry.location)) : d == google.maps.GeocoderStatus.OVER_QUERY_LIMIT && (c.next_address--, c.settings.delay++);
                c.next_geocode_request()
            })
        },
        create_marker: function(a, c, b) {
            b = { position: new google.maps.LatLng(c, b), map: this.map };
            a.infobox_content ? c = a.infobox_content : (c = a.address, !0 === a.coordinates && a.geocoded_address && (c = a.geocoded_address));
            this.settings.animations && (b.animation = google.maps.Animation.DROP);
            "custom" == this.settings.map_style &&
                "theme" == this.settings.marker_icon ? b.icon = new google.maps.MarkerImage(a.marker, null, null, null, new google.maps.Size(37, 55)) : "custom" == this.settings.map_style && a.marker && (b.icon = a.marker);
            a = new google.maps.Marker(b);
            this.markers.push(a);
            this.create_infowindow(c, a)
        },
        create_infowindow: function(a, c) {
            var b, d, e, f = this;
            "custom" == this.settings.infobox_styling && "custom" == this.settings.map_style ? (d = h.createElement("div"), e = {
                content: d,
                disableAutoPan: !1,
                maxWidth: 150,
                pixelOffset: new google.maps.Size(-125, 10),
                zIndex: null,
                boxStyle: { background: "none", opacity: 1, width: "250px" },
                closeBoxMargin: "2px 2px 2px 2px",
                closeBoxURL: "//www.google.com/intl/en_us/mapfiles/close.gif",
                infoBoxClearance: new google.maps.Size(1, 1)
            }, d.className = "fusion-info-box", d.style.cssText = "background-color:" + this.settings.infobox_background_color + ";color:" + this.settings.infobox_text_color + ";", d.innerHTML = a, b = new InfoBox(e), b.open(this.map, c), this.settings.show_address || b.setVisible(!1), google.maps.event.addListener(c, "click", function() {
                b.getVisible() ?
                    b.setVisible(!1) : b.setVisible(!0)
            })) : (b = new google.maps.InfoWindow({ content: a }), this.settings.show_address && (b.show = !0, b.open(this.map, c)), google.maps.event.addListener(c, "click", function() { b.show ? (b.close(f.map, this), b.show = !1) : (b.open(f.map, this), b.show = !0) }))
        },
        next_geocode_request: function() {
            var a = this;
            this.next_address < this.settings.addresses.length && setTimeout(function() { a.geocode_address(a.settings.addresses[a.next_address]);
                a.next_address++ }, this.settings.delay) }
    });
    d.fn.fusion_maps = function(a) {
        this.each(function() {
            d.data(this,
                "plugin_fusion_maps") || d.data(this, "plugin_fusion_maps", new e(this, a))
        });
        return this
    }
})(jQuery, window, document);
