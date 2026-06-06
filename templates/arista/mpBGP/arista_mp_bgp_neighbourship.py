neighbourship_template = """
{% for neighbour, neighbour_val in bgp_config_dict.items() %}
{# only if neighbour ip is defined, go for config generation or else skip #}
{% if neighbour_val["neighbour_ip"] != "" %}
{# configuring the neighbour's remote as #}
{% if neighbour_val["neighbour_peer_group"] != "" %}
    neighbour {{ neighbour_val["neighbour_ip"] }} peer group {{ neighbour_val["neighbour_peer_group"] }}
    neighbour peer group {{ neighbour_val["neighbour_peer_group"] }} remote-as {{ neighbour_val["neighbour_remote_as"] }}
{% else %}
    neighbour {{ neighbour_val["neighbour_ip"] }} remote-as {{ neighbour_val["neighbour_remote_as"] }}
{% endif %} 
{% endif %}
{% if neighbour_val["neighbour_update_source"] != "" %}
    neighbour {{ neighbour_val["neighbour_ip"] }} update-source {{ neighbour_val["neighbour_update_source"] }}
{% endif %}
{% if neighbour_val["is_ebgp_mulithop_set"] == True %}
    neighbour {{ neighbour_val["neighbour_ip"] }} ebgp-multihop 10
{% endif %}
{% if neighbour_val["neighbour_route_maps"] %}
{% for key, val in neighbour_val["neighbour_route_maps"].items() %}
    neighbour {{ neighbour_val["neighbour_ip"] }} route-map {{ key }} {{ val }}
{% endfor %}
{% endif %}
!
{% endfor %}
"""

address_family_template = """
{# setting the address family list in the jinja template #}
{% set address_families = ["ipv4", "evpn", "vpnv4"] %} 
{# configuring the neighbourship in the user-inputted address-family #}
{% for AF in address_families %}
    address-family {{ AF }}
{% for neighbour, neighbour_val in bgp_config_dict.items() %}
{% if AF == neighbour_val["neighbour_address_family"] %}
{% if neighbour_val["neighbour_peer_group"] != "" %}
        neighbour {{ neighbour_val["neighbour_peer_group"] }} activate
{% else %}
        neighbour {{ neighbour_val["neighbour_ip"] }} activate
{% endif %}
{% else %}
{% if neighbour_val["neighbour_peer_group"] != "" %}
        no neighbour {{ neighbour_val["neighbour_peer_group"] }} activate
{% else %}
        no neighbour {{ neighbour_val["neighbour_ip"] }} activate
{% endif %}
{% endif %}
{% endfor %}
{% endfor %}
"""