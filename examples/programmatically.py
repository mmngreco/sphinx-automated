import sphinx_automated as sa
prj_dir = "path"
prj_name = "pkg_name"
author = "autor"
try:
    sa.remove_doc_structure.main(prj_dir)
except:
    pass
sa.make_doc_structure.main(prj_dir, prj_name, author)
sa.customize_conf.main(prj_dir)
sa.generate_rst.main(prj_dir)
sa.process_templates.main(prj_dir)
sa.update_index.main(prj_dir)
sa.generate_html.main(prj_dir)

