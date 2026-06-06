neighbourship_template = """
!
{# only if neighbour ip is defined, go for config generation or else skip #}
{% if neighbour_ip != "" %}
{# configuring the neighbour's remote as #}
{% if peer_group != "" %}
    neighbour {{ neighbour_ip }} peer group {{ peer_group }}
    neighbour peer group {{ peer_group }} remote-as {{ neighbour_remote_as }}
{% else %}
    neighbour {{ neighbour_ip }} remote-as {{ neighbour_remote_as }}
{% endif %} 
{# setting the address family list in the jinja template #}
{% set address_families = ["ipv4", "evpn", "vpnv4"] %} 
{# configuring the neighbourship in the user-inputted address-family #}
{% for AF in address_families %}
{% if AF == neighbour_address_family %}
    address-family {{ AF }}
{% if peer_group != "" %}
        neighbour {{ peer_group }} activate
{% else %}
        neighbour {{ neighbour_ip }} activate
{% endif %}
{% else %}
    address-family {{ AF }}
{% if peer_group != "" %}
        no neighbour {{ peer_group }} activate
{% else %}
        no neighbour {{ neighbour_ip }} activate
{% endif %}
{% endif %}
{% endfor %}
{% endif %}
!
"""