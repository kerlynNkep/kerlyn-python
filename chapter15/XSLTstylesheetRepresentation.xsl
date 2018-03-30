<?xml version= "1.0"?>
<xsl:stylesheet version = "1.0" xmlns:xsl = "http://www.w3.org/1999/XSL/Transform">

<!-- write XML declaration and DOCTYPE DTD information-->
<xsl:output method= "xml" omit-xml-declaration = "no" 
			doctype-system = "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"
			doctype-public = "-//W3C//DTD XHTML 1.0 Strict//EN" />

<!--Match document root-->
<xsl:template match="/">
	<html xmlns = "http://www.w3.org/1999/xhtml">
		<xsl:apply-templates />
	</html>
</xsl:template>

<!--Match Product-->
<xsl:template match="product">
	<head>
		<servingsize>Cookies
			<xsl:value-of select = "servingsize"/></servingsize>
	</head>

	<body>
		<h1 style = "color:blue">
			<xsl:value-of select="servingsize"/></h1>

		<table style="border-style: groove; background-color: wheat">
			<xsl:for-each select = "Calories">
				<tr>
					<td style="text-align: right">
						<xsl:value-of select="total"/>
					</td>
					<td style="text-align: right">
						<xsl:value-of select="fat"/>
					</td>
				</tr>
			</xsl:for-each>

			<xsl:for-each select = "fat">
				<tr>
					<td style="text-align: right">
						<xsl:value-of select="total"/>
					</td>
					<td style="text-align: right">
						<xsl:value-of select="saturated"/>
					</td>
				</tr>
			</xsl:for-each>

			<xsl:value-of select = "Cholesterol">
				<tr>
					<td style="text-align: right">
						<xsl:value-of select="Cholesterol"/>
					</td>
				</tr>
			</xsl:value-of>

			<xsl:value-of select = "Soduim">
				<tr>
					<td style="text-align: right">
						<xsl:value-of select="Soduim"/>
					</td>
				</tr>
			</xsl:value-of>

			<xsl:for-each select = "Carbohydrate">
				<tr>
					<td style="text-align: right">
						<xsl:value-of select="total"/>
					</td>
					<td style="text-align: right">
						<xsl:value-of select="fiber"/>
					</td>
					<td style="text-align: right">
						<xsl:value-of select="sugar"/>
					</td>
				</tr>
			</xsl:for-each>
		</table>
		</body>
	</xsl:template>

</xsl:stylesheet>





