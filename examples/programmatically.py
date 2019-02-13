import sphinx_automated as sa

# ============================================================================
# EDIT THIS
PRJ_DIR = "path"
PRJ_NAME = "pkg_name"
AUTHOR = "autor"
# ============================================================================

try:
    sa.remove_doc_structure.main(PRJ_DIR)
except:
    pass

sa.make_doc_structure.main(PRJ_DIR, PRJ_NAME, AUTHOR)
sa.customize_conf.main(PRJ_DIR)
sa.generate_rst.main(PRJ_DIR)
sa.process_templates.main(PRJ_DIR)
sa.update_index.main(PRJ_DIR)
sa.generate_html.main(PRJ_DIR)

